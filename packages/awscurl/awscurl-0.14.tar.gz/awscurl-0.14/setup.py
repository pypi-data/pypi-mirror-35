__author__ = 'iokulist'

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='awscurl',
    version='0.14',
    description='Curl like tool with AWS request signing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/okigan/awscurl',
    author='Igor Okulist',
    author_email='okigan@gmail.com',
    license='MIT',
    packages=['awscurl'],
    entry_points={
        'console_scripts': [
            'awscurl = awscurl.__main__:main',
        ],
    },
    zip_safe=False,
    install_requires=[
        'requests',
        'configargparse',
        'configparser',
        'urllib3[secure]'
    ]
)
