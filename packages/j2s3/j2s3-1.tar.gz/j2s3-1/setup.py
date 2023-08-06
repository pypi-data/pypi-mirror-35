from setuptools import setup

setup(
    name='j2s3',
    version='1',
    packages=['j2s3'],
    url='',
    license='Apache 2.0',
    author='jackmahoney',
    author_email='jackmahoney212@gmail.com',
    description='A lib for publishing Java maven projects to an S3 maven repository',
    install_requires=[
        'pytest==3.8.0',
        'lxml==4.2.4'
    ]
)
