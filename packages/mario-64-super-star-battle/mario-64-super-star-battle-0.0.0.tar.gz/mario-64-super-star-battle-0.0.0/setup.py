#!/usr/bin/env python3

from setuptools import setup
from mario_battle.version import NAME, DESCRIPTION, VERSION


# Parse readme to include in PyPI page
with open('README.md') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION.capitalize(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mwiens91/twitch-game-notify',
    author='Branko Bajcetic, Matt Wiens',
    author_email='bajcetic.branko@gmail.com, mwiens91@gmail.com',
    license='BSD 3-clause "New" or "Revised License"',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=['mario_battle'],
    entry_points={
        'console_scripts': ['m64ssb = mario_battle.main:main'],
    },
    python_requires='>=3',
    install_requires=[
        'colorama',
    ],
)
