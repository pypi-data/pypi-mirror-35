#!/usr/bin/env python
# coding: utf-8

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function

# the name of the package
name = 'dfkernel'

#-----------------------------------------------------------------------------
# Minimal Python version sanity check
#-----------------------------------------------------------------------------

import sys

v = sys.version_info
if v[:2] < (3,3):
    error = "ERROR: %s requires Python version 3.3 or above." % name
    print(error, file=sys.stderr)
    sys.exit(1)

PY3 = (sys.version_info[0] >= 3)

#-----------------------------------------------------------------------------
# get on with it
#-----------------------------------------------------------------------------

from glob import glob
import os
import shutil

from distutils.core import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))
pkg_root = pjoin(here, name)

packages = []
for d, _, _ in os.walk(pjoin(here, name)):
    if os.path.exists(pjoin(d, '__init__.py')):
        packages.append(d[len(here)+1:].replace(os.path.sep, '.'))

package_data = {
    'dfkernel': ['resources/*.js',
                 'resources/*.png',
                 'resources/df-notebook/*.js',
                 'resources/df-notebook/css/*.css',
                 'resources/df-notebook/lib/*/*.js'],
}

version_ns = {}
with open(pjoin(here, name, '_version.py')) as f:
    exec(f.read(), {}, version_ns)


setup_args = dict(
    name            = name,
    version         = version_ns['__version__'],
    scripts         = glob(pjoin('scripts', '*')),
    packages        = packages,
    py_modules      = ['dfkernel_launcher'],
    package_data    = package_data,
    description     = "Dataflow Python Kernel for Jupyter",
    author          = 'Dataflow Notebook Development Team',
    author_email    = 'dataflownb@users.noreply.github.com',
    url             = 'http://dataflownb.github.io/',
    license         = 'BSD',
    platforms       = "Linux, Mac OS X, Windows",
    keywords        = ['Dataflow', 'Interactive', 'Interpreter', 'Shell', 'Web'],
    classifiers     = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)

if 'develop' in sys.argv or any(a.startswith('bdist') for a in sys.argv):
    import setuptools

setuptools_args = {}
install_requires = setuptools_args['install_requires'] = [
    'ipython>=6.3.0',
    'traitlets>=4.1.0',
    'jupyter_client',
    'tornado>=4.0',
    'ipykernel>=4.8.2',
    'notebook>=5.0'
]

if any(a.startswith(('bdist', 'build', 'install')) for a in sys.argv):
    from dfkernel.kernelspec import write_kernel_spec, make_ipkernel_cmd, KERNEL_NAME

    argv = make_ipkernel_cmd(executable='python')
    dest = os.path.join(here, 'data_kernelspec')
    if os.path.exists(dest):
        shutil.rmtree(dest)
    write_kernel_spec(dest, overrides={'argv': argv})

    setup_args['data_files'] = [
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME), [f for f in glob(pjoin(dest, '*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook'), [f for f in glob(pjoin(dest, 'df-notebook', '*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook','lib'),[f for f in glob(pjoin(dest, 'df-notebook', 'lib','*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook', 'lib','d3'),
         [f for f in glob(pjoin(dest, 'df-notebook', 'lib', 'd3','*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook', 'lib','d3-graphviz'),
         [f for f in glob(pjoin(dest, 'df-notebook', 'lib', 'd3-graphviz','*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook', 'lib','graphlib'),
         [f for f in glob(pjoin(dest, 'df-notebook', 'lib', 'graphlib','*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook', 'lib','graphlib-dot'),
         [f for f in glob(pjoin(dest, 'df-notebook', 'lib', 'graphlib-dot','*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook', 'lib','lodash'),
         [f for f in glob(pjoin(dest, 'df-notebook', 'lib', 'lodash','*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook', 'lib', 'viz'),
         [f for f in glob(pjoin(dest, 'df-notebook', 'lib', 'viz', '*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook','css'),[f for f in glob(pjoin(dest, 'df-notebook', 'css','*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook', 'img'),
         [f for f in glob(pjoin(dest, 'df-notebook', 'css', '*')) if not os.path.isdir(f)]),
        (pjoin('share', 'jupyter', 'kernels', KERNEL_NAME, 'df-notebook', 'img','fa'),
         [f for f in glob(pjoin(dest, 'df-notebook', 'img', 'fa', '*')) if not os.path.isdir(f)]),

    ]

extras_require = setuptools_args['extras_require'] = {
    'test': ['nose_warnings_filters', 'nose-timer'],
}

if 'setuptools' in sys.modules:
    setup_args.update(setuptools_args)

if __name__ == '__main__':
    setup(**setup_args)
