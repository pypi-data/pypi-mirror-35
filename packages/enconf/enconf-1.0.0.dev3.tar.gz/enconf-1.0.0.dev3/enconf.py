import os
import re

__version__ = '1.0.0dev3'

# Dictionary to get a config class based on key. This is automatically
# populated on class creation by ConfigMeta. Keys are the name of the class
# before Config suffix in uppercase
CONFIGS = {}


def first_key(d):
    """
    Gets the first key of a dictionary
    :param d: Dictionary
    :return: First key in dictionary
    """
    return list(d.keys())[0]


def get_index_type(iterable):
    """
    Gets the index type of an iterable. Note that iterables with multiple
    index types are not supported
    :param iterable: Iterable to get index type of
    :return: Type of index of iterable
    """
    if isinstance(iterable, (tuple, list)):
        return int
    elif isinstance(iterable, dict):
        return type(first_key(iterable)) if iterable else None
    else:
        raise ValueError()


def get_value_type(iterable):
    """
    Gets the value type of an iterable. Note that iterables with multiple
    value types are not supported
    :param iterable: Iterable to get value type of
    :return: Value type of iterable
    """
    if isinstance(iterable, (tuple, list)):
        return type(iterable[0])
    elif isinstance(iterable, dict):
        return type(iterable.get(first_key(iterable)))
    else:
        raise ValueError()


def get_nested(iterable, indices, fail_return_first=False):
    """
    Gets a nested value of a series of indices
    :param iterable: Iterable to get value from
    :param indices: Sequence of indices to follow
    :param fail_return_first: Returns first key if an index doesn't exist.
            This is a somewhat dirty way of getting what we need for config.
            Defaults to False
    :return: Value at sequence of indices
    """
    index = get_index_type(iterable)(indices[0])
    if len(indices) > 1:
        return get_nested(iterable[index], indices[1:])
    else:
        if fail_return_first:
            try:
                return iterable[index]
            except IndexError:
                return iterable[0]
            except KeyError:
                return iterable[first_key(iterable)]
        else:
            return iterable[index]


def set_nested(iterable, indices, value):
    """
    Sets a nested value of a series of indices. Note that this will
    edit the iterable in-place since all iterables should be references
    :param iterable: Iterable to set value in
    :param indices: Indices to follow
    :param value: Value to set
    :return:
    """
    index = get_index_type(iterable)(indices[0])
    if len(indices) > 1:
        set_nested(iterable[index], indices[1:], value)
    else:
        if isinstance(iterable, dict):
            iterable.update({index: value})
        elif isinstance(iterable, list):
            if index < len(iterable):
                iterable[index] = value
            else:
                # Add Nones if we have a list. Note that we can't do
                # this for tuples since they're immutable
                set_nested(iterable.append(None), indices, value)
        else:
            iterable[index] = value


def split_camel_case(string):
    """
    Splits camel case string into list of strings
    :param string: String to split
    :returns: List of substrings in CamelCase
    """
    return re.sub('([a-z])([A-Z])', r'\1 \2', string).split()


def split_escaped(string, split_char=' ', escape_char='\\'):
    """
    Splits escaped string
    :param string: String to split
    :param split_char: Character to split on. Defaults to single space
    :param escape_char: Character to escape with. Defaults to \
    """
    ret = []
    current = ''
    skip = False
    for char in string:
        if skip:
            skip = False
            continue
        elif char == escape_char:
            current += split_char
            skip = True
        elif char == split_char:
            if current:
                ret.append(current)

            current = ''
        else:
            current += char

    if current:
        ret.append(current)

    return ret


def print_config(config):
    """
    Utility function for printing out all variables of a config
    :param config: Config to print
    """
    for key in dir(config):
        if key == key.upper():
            value = getattr(config, key)
            print('\t{:24s}{:30s}{}'.format(key, str(type(value)), value))


class ConfigMeta(type):
    """
    Config metaclass to register config classes
    """

    def __init__(cls, name, bases, attr):
        """
        Called upon the creation of a new class
        """
        # Parent initialization
        type.__init__(cls, name, bases, attr)

        # Get key for name
        substrings = split_camel_case(name)
        substrings = substrings[
                     :-1] if substrings[-1].lower() == 'config' else substrings
        key = '_'.join([s.upper() for s in substrings])

        # Register class
        CONFIGS[key] = cls


class ConfigBase(object):
    # Instance so we don't create a new config every time (singleton)
    __instance = None

    def __init__(self):
        """
        Initialization. Uses instance if there is one, otherwise replaces class variables with environment variables
        """
        if self.__instance:
            self = self.__instance
        else:
            for var in dir(self):
                # Make sure it isn't a python special attribute
                if var.upper() != var:
                    continue

                self._set_env_override(var, getattr(self, var))

            self.__instance = self

    @staticmethod
    def _search_env(name):
        """
        Searches env variables for variables matching name and returns a list of indices
        :param name: Name to match
        :return: List of (var, value, [indices]) tuples
        """
        envs = filter(lambda k: k.split('__')[0] == name, os.environ.keys())
        return [{'config_var': var.split('__')[0],
                 'env_var': var,
                 'env_setting': os.getenv(var),
                 'indices': var.split('__')[1:]}
                for var in envs]

    def _set_env_override(self, var, original):
        """
        Gets the environment variable override value for a variable if it exists or returns the original value
        :param var: Name of variable to check. It will check the environment variable of the same name
        :return: Environment variable of object or original value if environment variable does not exist
        """
        original_type = type(original) if original is not None else str

        envs = self._search_env(var)
        override = None
        for env in envs:
            if env['indices']:
                original_value = get_nested(original, env['indices'], True)
                set_nested(original, env['indices'],
                           self._parse_env_value(env['env_setting'], type(original_value), original_value))
            else:
                setting = self._parse_env_value(env['env_setting'], original_type, original)
                setattr(self, var, setting)

        return override

    @classmethod
    def _parse_env_value(cls, env_setting, original_type, original_value):
        """
        Parses the value of an environment variable according to the type of the original variable
        :param env_setting: Environment setting as string
        :param original_type: Type of original variable
        :param original_value: Value of original variable
        :return:
        """
        # No override if there is no env setting
        if not env_setting:
            return original_value

        if isinstance(original_value, (list, tuple)):
            # Lists are separated with colons such as a:b:c -> ['a', 'b', 'c']
            list_item_type = type(original_value[0]) if original_value else str
            items = split_escaped(env_setting, split_char=':')
            override = original_type(map(list_item_type, items))
        elif isinstance(original_value, bool):
            return env_setting.lower() == 'true'
        else:
            override = original_type(env_setting)
        return override
