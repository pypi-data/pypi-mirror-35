from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.txt'), encoding='utf-8') as f:
	long_description = f.read()

setup(name='pyvie',version='1.0.0',description='A module for making videos in Python',long_description = long_description,long_description_type='text/plain',author_email='davidbutts96@gmail.com',keywords='Python movies animation',py_modules=['pyvie'],install_requires=['matplotlib','Ipython'])
