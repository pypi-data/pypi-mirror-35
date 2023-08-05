#!/usr/bin/env python
"""Setup for ddl package."""
from __future__ import division, print_function

import os
import sys

# Optional setuptools features
# We need to import setuptools early, if we want setuptools features,
# as it monkey-patches the 'setup' function
# For some commands, use setuptools
SETUPTOOLS_COMMANDS = {'develop', 'release', 'bdist_egg', 'bdist_rpm', 'bdist_wininst',
                       'install_egg_info', 'build_sphinx', 'egg_info', 'easy_install', 'upload',
                       'bdist_wheel', '--single-version-externally-managed'}
if SETUPTOOLS_COMMANDS.intersection(sys.argv):
    pass


def configuration(parent_package='', top_path=None):
    """Creates `configuration` parameter for setup function.

    Parameters
    ----------
    parent_package : str, optional
    top_path : str or None, optional

    Returns
    -------
    config
        `configuration` parameter for setup function call
    """
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    from numpy.distutils.misc_util import Configuration

    config = Configuration(None, parent_package, top_path)

    # Avoid non-useful msg:
    # "Ignoring attempt to set 'name' (from ... "
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('ddl')
    config.add_subpackage('ddl.tests')
    config.add_subpackage('ddl.externals')

    # I think this should automatically call setup.py in mlpack
    config.add_subpackage('ddl.externals.mlpack')

    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup

    metadata = dict(
        name='ddl',
        packages=['ddl'],
        version='0.0.2',
        description='Destructive deep learning estimators and functions. Estimators are compatible '
                    'with scikit-learn.',
        url='https://github.com/davidinouye/destructive-deep-learning',
        author='David I. Inouye',
        author_email='dinouye@cs.cmu.edu',
        license='BSD 3-clause',
        zip_safe=False,
        # Nose needed by 0.19.1 version of scikit-learn for importing testing module
        # I think this was fixed for upcoming version 0.20.X to avoid dependency
        install_requires=['numpy', 'scipy', 'scikit-learn'],
        # OPTIONAL: ['matplotlib', 'pot', 'seaborn']
        # Cython, numpy and pypandoc needed to install pot package
        # (bug in installing pot from scratch)
        # Should do the following before trying to install
        # $ pip install setuptools
        # $ pip install Cython
        # $ pip install numpy
        # $ pip install pypandoc
        setup_requires=['numpy', 'Cython'],
        extras_require={
            'test': ['pytest', 'pytest-cov', 'codecov', 'nose', 'pot', 'isort', 'flake8',
                     'pydocstyle'],
            # Testing framework
        },
    )

    metadata['configuration'] = configuration

    setup(**metadata)
