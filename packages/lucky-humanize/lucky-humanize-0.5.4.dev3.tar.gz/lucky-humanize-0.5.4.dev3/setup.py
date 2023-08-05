#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for humanize."""

from setuptools import setup, find_packages
import sys, os
import io

version = '0.5.4.dev3'

# some trove classifiers:


import pypandoc, re
long_description = pypandoc.convert('README.md', 'rst')
long_description = long_description.replace("\r","")
#long_description = re.sub(r'<!--.*?-->', '', long_description)
import restructuredtext_lint
errors = restructuredtext_lint.lint(long_description)
print("\n".join("{i}: {l}".format(i=i,l=l) for i, l in enumerate(long_description.split('\n'))))
print("\n".join('{err.type} {err.source}:{err.line} {err.message}\n'.format(err=e) for e in errors))
assert(not errors)

setup(
    name='lucky-humanize',
    version=version,
    description="python humanize utilities",
    long_description=long_description,
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
    ],
    keywords='humanize time size',
    author='Jason Moiron',
    author_email='jmoiron@jmoiron.net',

    url='http://github.com/luckydonald-forks/humanize',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    tests_require=['mock'],
    install_requires=[
      # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
