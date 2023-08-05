# --------------------------------------------------------------------------- #
#                                                                             #
# Integrated Urban Water Model (IUWM)                                         #
#     Forecast urban water demands driven by land, climate, and technology    #
#     Defer expensive infrastructure investments                              #
#                                                                             #
# Authors:                                                                    #
#     Andre Dozier (andre.dozier@colostate.edu)                               #
#     Brad Reichel                                                            #
#     Sybil Sharvelle                                                         #
#     Larry Roesner                                                           #
#     Mazdak Arabi                                                            #
#                                                                             #
# The Integrated Urban Water Model has been developed by Colorado State       #
# University and is copyrighted; however, code is open-source so that         #
# users may examine and modify the code to suit their specific application    #
# needs, subject to the conditions below.                                     #
#                                                                             #
# Copyright 2018 Colorado State University                                    #
#                                                                             #
# Licensed under the Apache License, Version 2.0 (the "License");             #
# you may not use this file except in compliance with the License.            #
# You may obtain a copy of the License at                                     #
#                                                                             #
#     http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS,           #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
# See the License for the specific language governing permissions and         #
# limitations under the License.                                              #
#                                                                             #
# --------------------------------------------------------------------------- #
# from distutils.core import setup
import glob
from setuptools import setup
import os
import re

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION_FILE = os.path.join(THIS_DIR, 'iuwm', 'version.py')

with open("README.md", "r") as fh:
    long_description = fh.read()

MPL_FILES = []
PY2EXE_EXISTS = True
try:
    import py2exe
    import matplotlib
    MPL_FILES = matplotlib.get_py2exe_datafiles()
except:
    PY2EXE_EXISTS = False

if PY2EXE_EXISTS:
    EXTRAS = {
        'console': ['iuwm/console.py'],
    }
else:
    EXTRAS = {
        'scripts': ['iuwm/console.py'],
    }


def version():
    s = open(VERSION_FILE, 'r').read()
    m = re.search(r'''^__version__ = ["'](.*?)["']\s*$''', s, flags=re.M)
    if m:
        return m.group(1)
    raise AssertionError('Could not find version number!')


def find_data_files(source, target, patterns):
    """Locates the specified data-files and returns the matches
    in a data_files compatible format.

    source is the root of the source data tree.
       Use '' or '.' for current directory.
    target is the root of the target data tree.
       Use '' or '.' for the distribution directory.
    patterns is a sequence of glob-patterns for the
       files you want to copy.
    """
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError("Magic not allowed in src, target")
    ret = {}
    for pattern in patterns:
        pattern = os.path.join(source, pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(target, os.path.relpath(filename, source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path, []).append(filename)
    return sorted(ret.items())


setup(
    name="iuwm",
    version=version(),
    description="Forecasts municipal water demand with changes in population, land use, climate, water use "
                "behavior, and use of alternative sources of water.",
    long_description=long_description,
    author="Andre Dozier, Bradley Reichel, Sybil Sharvelle, Larry Roesner, Mazdak Arabi",
    author_email="adozier@razixsolutions.com",
    license="Apache 2.0",
    data_files=MPL_FILES + find_data_files(THIS_DIR, THIS_DIR, ['core/data/*']),
    install_requires=[s.strip().replace('-', '_') for s in open('requirements.txt', 'r').readlines()],
    **EXTRAS
)
