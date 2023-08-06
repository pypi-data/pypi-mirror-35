
import io
import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='paggcerto-python',
    version='0.0.3',
    description='Python bindings for Paggcerto API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tassio/paggcerto-python',
    author='Tássio Guimarães',
    author_email='tassio.acg@gmail.com',
    license='Apache License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='paggcerto api rest payment',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'python-http-client',
        'dataclasses'
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/tassio/paggcerto-python/issues'
    },
)
