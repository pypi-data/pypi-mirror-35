#!/usr/bin/env python
import os
import io
import re
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


VERSION = find_version('pytext', '__init__.py')
long_description = read('README.rst')

setup_info = dict(
    # Metadata
    name='pytexttool',
    version=VERSION,
    author='Clementine',
    author_email='iclementine@outlook.com',
    url='https://github.com/iclementine/text',
    description='Text utilities and datasets for generic deep learning, Fork from torchtext but uses numpy to store datasets for more generic use.',
    long_description=long_description,
    license='BSD',

    install_requires=[
        'tqdm', 'requests'
    ],

    # Package info
    packages=find_packages(exclude=('test',)),

    zip_safe=True,
)

setup(**setup_info)
