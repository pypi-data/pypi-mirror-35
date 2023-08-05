#!/usr/bin/env python

import os, sys, glob, subprocess
from setuptools import setup, find_packages, Extension
from distutils.command.build_ext import build_ext as _build_ext
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    has_wheel = True
except ImportError:
    has_wheel = False
from codecs import open


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

_is_manylinux = None
def is_manylinux():
    global _is_manylinux
    if _is_manylinux is None:
        _is_manylinux = False
        try:
            for line in open('/etc/redhat-release').readlines():
                if 'CentOS release 5.11' in line:
                    _is_manylinux = True
                    break
        except (OSError, IOError):
            pass
    return _is_manylinux

try:
    root_install = os.environ["ROOTSYS"]
except KeyError:
    root_install = None

def get_cflags():
    config_exec = 'cling-config'
    if root_install:
        config_exec = 'root-config'
    cli_arg = subprocess.check_output([config_exec, '--auxcflags'])
    return cli_arg.decode("utf-8").strip()

class my_build_extension(_build_ext):
    def build_extension(self, ext):
        ext.extra_compile_args += ['-O2']+get_cflags().split()
        if 'linux' or 'darwin' in sys.platform:
            ext.extra_compile_args += \
                ['-Wno-cast-function-type',      # g++ >8.2, complaint of CPyFunction cast
                 '-Wno-bad-function-cast',       # clang for same
                 '-Wno-register',                # C++17, Python headers
                 '-Wno-unknown-warning']         # since clang/g++ don't have the same options
        if 'linux' in sys.platform:
            ext.extra_link_args += ['-Wl,-Bsymbolic-functions']
        return _build_ext.build_extension(self, ext)

cmdclass = { 'build_ext': my_build_extension }
if has_wheel:
    class my_bdist_wheel(_bdist_wheel):
        def run(self, *args):
         # wheels do not respect dependencies; make this a no-op, unless it is
         # explicit building for manylinux
            if is_manylinux():
                return _bdist_wheel.run(self, *args)
    cmdclass['bdist_wheel'] = my_bdist_wheel


setup(
    name='CPyCppyy',
    version='1.3.6',
    description='Cling-based Python-C++ bindings for CPython',
    long_description=long_description,

    url='http://cppyy.readthedocs.io/',

    # Author details
    author='Wim Lavrijsen',
    author_email='WLavrijsen@lbl.gov',

    license='LBNL BSD',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'Topic :: Software Development',
        'Topic :: Software Development :: Interpreters',

        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: C',
        'Programming Language :: C++',

        'Natural Language :: English'
    ],

    setup_requires=['wheel'],
    install_requires=['cppyy-backend>=1.3'],

    keywords='C++ bindings data science',

    cmdclass = cmdclass,

    ext_modules=[Extension('libcppyy',
        sources=glob.glob('src/*.cxx'),
        include_dirs=['include'])],
)
