import re
from os.path import join, dirname

from setuptools import setup, find_packages


# reading package version (without reloading it)
with open(join(dirname(__file__), 'restfulpy', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S) \
        .match(v_file.read()) \
        .group(1)


dependencies = [
    'nanohttp >= 1.3.0',
    'argcomplete',
    'ujson',
    'appdirs',
    'sqlalchemy',
    'alembic',
    'itsdangerous',
    'mako',
    'psycopg2-binary',
    'redis',
    'pyyaml',
    'ua-parser',
    'user-agents',
    'pycrypto',
    'python-dateutil',

    # Testing
    'requests',
    'pytest',
    'bddrest >= 1.15.2b'
]


setup(
    name='restfulpy',
    version=package_version,
    description='A toolchain for developing REST APIs',
    author='Vahid Mardani',
    author_email='vahid.mardani@gmail.com',
    install_requires=dependencies,
    packages=find_packages(),
    test_suite='restfulpy.tests',
    license='MIT'
)
