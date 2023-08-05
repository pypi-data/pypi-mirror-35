from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jupyterlab_autoversion',
    version='0.0.1',
    description='Automatically version notebooks from JupyterLab',
    long_description=long_description,
    url='https://github.com/timkpaine/jupyterlab_autoversion',
    download_url='https://github.com/timkpaine/jupyterlab_autoversion/archive/v0.0.1.tar.gz',
    author='Tim Paine',
    author_email='t.paine154@gmail.com',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='jupyter jupyterlab',

    packages=find_packages(exclude=['tests', ]),
    include_package_data=True,
    zip_safe=False,
)
