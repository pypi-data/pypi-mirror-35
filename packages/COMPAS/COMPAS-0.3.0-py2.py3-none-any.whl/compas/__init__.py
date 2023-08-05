"""
********************************************************************************
compas
********************************************************************************

.. currentmodule:: compas


.. toctree::
    :maxdepth: 1

    compas.com
    compas.datastructures
    compas.files
    compas.geometry
    compas.interop
    compas.numerical
    compas.plotters
    compas.robots
    compas.topology
    compas.utilities
    compas.viewers

"""

from __future__ import print_function

import os
import sys


__author__    = ['Tom Van Mele', ]
__copyright__ = 'Copyright 2017 - Block Research Group, ETH Zurich'
__license__   = 'MIT License'
__email__     = 'vanmelet@ethz.ch'
__version__   = '0.3.0'


PY3 = sys.version_info.major == 3

HERE = os.path.dirname(__file__)
HOME = os.path.abspath(os.path.join(HERE, '../..'))
DATA = os.path.abspath(os.path.join(HERE, '../../data'))
TEMP = os.path.abspath(os.path.join(HERE, '../../temp'))


def get(filename):
    filename = filename.strip('/')
    localpath = os.path.abspath(os.path.join(DATA, filename))
    if os.path.exists(localpath):
        return localpath
    else:
        return "https://raw.githubusercontent.com/compas-dev/compas/develop/data/{}".format(filename)


def get_bunny():
    import urllib
    import tarfile
    bunny = os.path.abspath(os.path.join(DATA, 'bunny/reconstruction/bun_zipper.ply'))
    if not os.path.exists(bunny):
        url = 'http://graphics.stanford.edu/pub/3Dscanrep/bunny.tar.gz'
        print('Getting the bunny from {} ...'.format(url))
        print('This will take a few seconds...')
        destination = os.path.abspath(os.path.join(DATA, 'bunny.tar.gz'))
        urllib.urlretrieve(url, destination)
        with tarfile.open(destination) as file:
            file.extractall(DATA)
        os.remove(destination)
        print('Got it!\n')
    return bunny


def get_armadillo():
    import urllib
    import gzip
    import shutil
    armadillo = os.path.abspath(os.path.join(DATA, 'armadillo/Armadillo.ply'))
    if not os.path.exists(armadillo):
        url = 'http://graphics.stanford.edu/pub/3Dscanrep/armadillo/Armadillo.ply.gz'
        print('Getting the armadillo from {} ...'.format(url))
        print('This will take a few seconds...')
        destination = os.path.abspath(os.path.join(DATA, 'Armadillo.ply.gz'))
        urllib.urlretrieve(url, destination)
        with gzip.open(destination, 'rb') as ifile, open(armadillo, 'wb+') as ofile:
            shutil.copyfileobj(ifile, ofile)
        os.remove(destination)
        print('Got it!\n')
    return armadillo


def is_windows():
    return os.name == 'nt'


def is_linux():
    return os.name == 'posix'


def is_mono():
    return 'mono' in sys.version.lower()


def is_ironpython():
    return 'ironpython' in sys.version.lower()


def raise_if_not_ironpython():
    if not is_ironpython():
        raise


def raise_if_ironpython():
    if is_ironpython():
        raise


def license():
    with open(os.path.join(HOME, 'LICENSE')) as fp:
        return fp.read()


def version():
    return __version__


def help():
    return 'http://compas-dev.github.io'


def copyright():
    return __copyright__


def credits():
    pass


def verify():
    requirements = [
        'numpy',
        'scipy',
        'matplotlib',
    ]
    optional = [
        'cvxopt',
        'cvxpy',
        'Cython',
        'imageio',
        'networkx',
        'numba',
        'pandas',
        'paramiko',
        'pycuda',
        'PyOpenGL',
        'PySide',
        'Shapely',
        'sympy',
    ]
    current = installed()

    print('=' * 80)
    print('Checking required packages...\n')
    issues = []
    for package in requirements:
        if package not in current:
            issues.append(package)
    if issues:
        print('The following required packages are not installed:')
        for package in issues:
            print('- {}'.format(package))
    else:
        print('All required packages are installed.')

    print('\nChecking optional packages...\n')
    issues = []
    for package in optional:
        if package not in current:
            issues.append(package)
    if issues:
        print('The following optional packages are not installed:')
        for package in issues:
            print('- {}'.format(package))
    else:
        print('All optional packages are installed.')
    print('=' * 80)
    print()


def installed():
    import pkg_resources
    installed_packages = pkg_resources.working_set
    flat_installed_packages = [package.project_name for package in installed_packages]
    return sorted(flat_installed_packages, key=str.lower)


def requirements():
    with open(os.path.join(HERE, '../requirements.txt')) as f:
        for line in f:
            print(line.strip())


__all__ = [
    'get',
    'license',
    'version',
    'help',
    'copyright',
    'credits',
    'verify',
    'installed',
    'requirements',
    'raise_if_ironpython',
    'raise_if_not_ironpython',
]
