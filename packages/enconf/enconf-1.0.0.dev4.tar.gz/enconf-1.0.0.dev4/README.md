# enconf
![Build Status](https://api.travis-ci.org/danielunderwood/envconf.svg?branch=master)

This library is meant to make configuration from environment variables as easy as possible.

## Installing

You may install from PyPI with `pip install enconf`.

## Creating a config

To create a config, you just need to create a class with metaclass `ConfigMeta` that inherits from `ConfigBase`. For
example, using six's `with_metaclass`:

```
import six
import envconf

class SampleConfig(six.with_metaclass(envconf.ConfigMeta, envconf.ConfigBase)):
    INT = 0
    STR = 'abc'
    LIST = [1, 2]
    DICT = {'A': 1}
```

This class will automatically parse the `INT`, `STR`, `LIST`, and `DICT` environment variables if they are set. If not,
it will use the default values defined in the class. The types interpreted from the environment will be the same type as
the original declaration in the class, with the exception of values that are originally `None` will have their
environment settings parsed as strings.

## Lists and dictionaries

List environment variables will be separated by `:`. For example:

```
ENV=a:b:c -> ENV = ['a', 'b', 'c']
```

Lists will interpret their types as the types in the original list.

Specific items may be changed by a double underscore:
```
LIST = [1, 2, 3]
LIST__1 = 4 -> LIST = [1, 4, 3]
```

Dictionaries may be accessed with the same double underscore method, but can also have access strings. If the key does
not exist in the dictionary, it will be added.