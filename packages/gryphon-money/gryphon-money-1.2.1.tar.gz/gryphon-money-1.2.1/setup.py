import sys
import setuptools


DESCRIPTION = """
A very slight fork of the Python Money class, https://github.com/carlospalol/money,
with different behaviour on arithmatic operations. This package is intended for use
with the Gryphon trading framework.
"""

SOURCE_ROOT = 'src'

# Python 2 backwards compatibility
if sys.version_info[0] == 2:
    SOURCE_ROOT = 'src-py2'


setuptools.setup(
    name='gryphon-money',
    description='Python Money Class',
    long_description=DESCRIPTION,
    version='1.2.1',
    author='MacLeod & Robinson, Inc.',
    author_email='hello@tinkercoin.com',
    url='https://github.com/TinkerWork/money',
    package_dir={'': SOURCE_ROOT},
    packages=[
        'money',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ]
)
