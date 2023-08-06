from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='commitcollector',
    version='2.0.2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['commitcollector'],
    entry_points={
        'console_scripts': [
            'commitcollector = commitcollector:main'
        ]
    })