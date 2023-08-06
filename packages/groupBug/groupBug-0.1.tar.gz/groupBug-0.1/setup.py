#!/usr/bin/env python3
from setuptools import setup, find_packages
import glob

install_requires = [
'pandas',
'ete3',
'matplotlib',
'seaborn',
'six']

setup(
     name='groupBug',
     version='0.1',
     description='Clustering heatmap tool for kraken-style reports',
     author=['Nick Sanderson'],
     author_email='nicholas.sanderson@ndm.ox.ac.uk',
     scripts=['groupBug/groupBug.py'],
     packages=find_packages('groupBug'),
     package_dir = {'': 'groupBug'},
     include_package_data=True,
     license='MIT',
     url='https://gitlab.com/ModernisingMedicalMicrobiology/groupBug',
     test_suite='nose.collector',
     tests_require=['nose'],
     install_requires=install_requires
 )

