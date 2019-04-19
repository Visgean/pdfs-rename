#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='pdfs-rename',
    version='0.1',
    description="Makes geojson from EXIF data.",
    author="Visgean",
    author_email='visgean@gmail.com',
    url='https://github.com/visgean/pdfs-rename',
    packages=[
        'rename',
    ],
    package_dir={'pdfs-rename': 'pdfs-rename'},
    license="MIT",
    keywords='photos geojson exif',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'pdftotext',
        'python-slugify',
        'PyPDF2',
    ],
    entry_points={
        'console_scripts': [
            'pdfs-rename = rename.main:main'
        ]
    },
)