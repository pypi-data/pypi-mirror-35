from setuptools import setup, find_packages
import os

datadir = os.path.join('scripts','templates')
datafiles = [(d, [os.path.join(d,f) for f in files])
    for d, folders, files in os.walk(datadir)]

setup(
    name='spankins',
    author='jamesrobertalbert@gmail.com',
    version='0.0.4',
    url='https://github.com/jamesalbert/spankins',
    long_description='',
    packages=['spankins'],
    install_requires=[
        'docopt',
        'requests',
        'jinja2'
    ],
    entry_points={
        'console_scripts': [
            'spankins=spankins.__init__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    data_files = datafiles
)
