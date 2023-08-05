#!/usr/bin/env python

import sys

from setuptools import setup

from subprocess import check_output
import platform

def get_version():
    """Get the current version from a git tag, or by reading tdl/version.py"""
    try:
        tag = check_output(['git', 'describe', '--abbrev=0'],
                           universal_newlines=True).strip()
        assert not tag.startswith('v')
        version = tag

        # add .devNN if needed
        log = check_output(['git', 'log', '%s..HEAD' % tag, '--oneline'],
                           universal_newlines=True)
        commits_since_tag = log.count('\n')
        if commits_since_tag:
            version += '.dev%i' % commits_since_tag

        # update tdl/version.py
        open('tdl/version.py', 'w').write('__version__ = %r\n' % version)
        return version
    except:
        exec(open('tdl/version.py').read(), globals())
        return __version__

is_pypy = platform.python_implementation() == 'PyPy'

def get_package_data():
    '''get data files which will be included in the main tcod/ directory'''
    BITSIZE, LINKAGE = platform.architecture()
    files = [
        'lib/LIBTCOD-CREDITS.txt',
        'lib/LIBTCOD-LICENSE.txt',
        'lib/README-SDL.txt'
        ]
    if 'win32' in sys.platform:
        if BITSIZE == '32bit':
            files += ['x86/SDL2.dll']
        else:
            files += ['x64/SDL2.dll']
    if sys.platform == 'darwin':
        files += ['SDL2.framework/Versions/A/SDL2']
    return files

setup(
    name='tdl',
    version='6.0.0',
    author='Kyle Stewart',
    author_email='4B796C65+tdl@gmail.com',
    description='legacy package',
    long_description="""
        This package has moved to https://pypi.org/project/tcod/
    """,
    url='https://github.com/libtcod/python-tcod',
    install_requires=['tcod'],
    license='Simplified BSD License',
    )
