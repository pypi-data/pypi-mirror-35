from setuptools import setup, find_packages
from codecs import open
from os import path
import pytopplot.version
import sys


here = path.abspath(path.dirname(__file__))

if not sys.version_info[0] == 3 and \
       sys.version_info[1] >= 5:
    sys.exit("Sorry, Python 3.5 or higher only")

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytopplot',
    version=pytopplot.version.version,
    description='GUI for ABCI program',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://bitbucket.com/seregaxvm/pytopplot',
    author='S.V. Matsievskiy',
    author_email='matsievskiysv@gmail.com',
    license='GPLv3+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public \
License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    keywords='wakefields accelerators particles GUI',
    packages=find_packages(exclude=["*.tests",
                                    "*.tests.*",
                                    "tests.*",
                                    "tests"]),
    include_package_data=True,
    install_requires=['numpy', 'PyQt5', 'matplotlib', 'PyYAML'],
    extras_require={
        'dev': ['check-manifest'],
    },
    entry_points={
        'console_scripts': ['pytopplot = pytopplot.__main__:main']
    }
)
