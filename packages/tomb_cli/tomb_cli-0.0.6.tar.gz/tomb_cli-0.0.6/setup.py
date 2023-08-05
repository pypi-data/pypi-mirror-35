from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open

import os

# As of pip 10.0.0 pip no longer keeps their internal
# APIs in the same place, and suggests not using them.
with open('requirements/install.txt', 'r') as f:
    reqs = f.readlines()

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

about = {}

with open(os.path.join(here, "tomb_cli", "__about__.py")) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=about['__version__'],
    description=about['__summary__'],
    long_description=long_description,
    url=about['__uri__'],
    author=about['__author__'],
    author_email=about['__email__'],
    license=about['__license__'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    zip_safe=True,
    install_requires=reqs,
    setup_requires=['setuptools-git'],
    entry_points={
        'console_scripts': [
            'tomb = tomb_cli.main:cli'
        ],
        'montague.config_loader': [
            'yaml = tomb_cli.config:YAMLConfigLoader'
        ],
        'tomb.commands': [
            'routes = tomb_cli.routes:routes',
            'serve = tomb_cli.serve:serve',
        ]
    },
)
