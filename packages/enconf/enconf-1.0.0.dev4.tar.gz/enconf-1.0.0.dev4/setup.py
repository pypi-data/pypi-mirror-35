from setuptools import setup, find_packages

import enconf

setup(
    name='enconf',
    version=enconf.__version__,
    description='Easy config setup from the environment',
    url='https://github.com/danielunderwood/enconf',
    author='Daniel Underwood',
    license='MIT',

    packages=find_packages(),

    extras_require={
        'test': ['pytest']
    },
)