#!/usr/bin/env python

from os import path

from setuptools import setup, find_packages

pwd = path.abspath(path.dirname(__file__))
with open(path.join(pwd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='OpenVAS Reporting',
    version='1.0.1a',
    description='Convert OpenVAS XML report files to Excel reports.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='TheGroundZero',
    author_email='2406013+TheGroundZero@users.noreply.github.com',
    url='https://github.com/TheGroundZero/openvas_to_report',
    packages=find_packages(exclude=['tests', 'tests.*', 'venv', '*git*']),
    requires=['xlsxwriter'],
    entry_points={
        'console_scripts': [
            'openvas_reporting = openvasreporting:main'
        ]
    },
    project_urls={
        'Source Code': 'https://github.com/TheGroundZero/openvas_to_report',
        'Documentation GitHub': 'https://openvas-reporting.stijncrevits.be/en/latest/',
        'Issues': 'https://github.com/TheGroundZero/openvas_to_report/issues/',
    },
    license='GPL-3.0-or-later',
    keywords='OpenVAS OpenVAS-reports Excel xlsxwriter xlsx reporting reports report',
)
