# coding: utf-8
import codecs

from setuptools import setup, find_packages

with codecs.open('README.md', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='stellar-sdk',
    version='0.1.9',
    description='stellar-base in python.',
    long_description=long_description,
    url='http://github.com/stellarCN/py-stellar-base/',
    license='Apache',
    author='Eno',
    author_email='appweb.cn@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'ed25519', 'crc16', 'requests', 'SSEClient', 'numpy', 'toml', 'mnemonic'
    ]
)
