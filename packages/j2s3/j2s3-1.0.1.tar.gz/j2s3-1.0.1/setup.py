from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='j2s3',
    version='1.0.1',
    packages=['j2s3'],
    url='',
    license='Apache 2.0',
    author='jackmahoney',
    author_email='jackmahoney212@gmail.com',
    description='A lib for publishing Java maven projects to an S3 maven repository',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'pytest==3.8.0',
        'lxml==4.2.4'
    ]
)
