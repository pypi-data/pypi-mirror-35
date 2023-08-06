import os
import re
import sys
import platform
import subprocess
import pathlib

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from distutils.version import LooseVersion


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir]
        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]
        cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
        build_args += ['--', '-j2']

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        env = os.environ.copy()
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp, env=env)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
    name='dhan16opm_libecl',
    version='0.1',
    author_email='chandan.nath@gmail.com',
    description='libecl',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dhan16opm/libecl",
    license="GNU General Public License, Version 3, 29 June 2007",
    packages=find_packages(where='python', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={'': 'python'},
    ext_package='ecl',
    ext_modules=[CMakeExtension('libecl')],
    cmdclass=dict(build_ext=CMakeBuild),
    install_requires=[
        'cwrap',
        'numpy',
        'pandas',
    ],
)
