#!/usr/bin/env python3
from setuptools import setup, find_packages
import glob

install_requires = [
'pandas',
'ete3',
'matplotlib',
'seaborn',
'six']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='groupBug',
     version='0.2',
     description='Clustering heatmap tool for kraken-style reports',
     author=['Nick Sanderson'],
     author_email='nicholas.sanderson@ndm.ox.ac.uk',
     scripts=['groupBug/groupBug.py'],
     packages=find_packages('groupBug'),
     package_dir = {'': 'groupBug'},
     include_package_data=True,
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT',
     url='https://gitlab.com/ModernisingMedicalMicrobiology/groupBug',
     test_suite='nose.collector',
     tests_require=['nose'],
     install_requires=install_requires
 )

