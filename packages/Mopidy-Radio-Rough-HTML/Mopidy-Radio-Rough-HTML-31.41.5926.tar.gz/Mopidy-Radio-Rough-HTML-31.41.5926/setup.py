from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']


setup(
    name='Mopidy-Radio-Rough-HTML',
    version=get_version('mopidy_radio_rough_html/__init__.py'),
    url='https://github.com/unusualcomputers/unusualcomputers/tree/master/code/mopidy/mopidyradioroughhtml',
    license='Apache License, Version 2.0',
    author='Unusual Computers',
    author_email='unusual.computers@gmail.com',
    description='Rough html gui for listening to internet',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
        'Mopidy-Podcast-iTunes',
        'Mopidy-Youtube',
        'Mopidy-Rough-Base >= 3.14.15',
        'Mopidy-TuneIn',
        'Mopidy-Mixcloud',
    ],
    entry_points={
        'mopidy.ext': [
            'radio_rough_html = mopidy_radio_rough_html:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
