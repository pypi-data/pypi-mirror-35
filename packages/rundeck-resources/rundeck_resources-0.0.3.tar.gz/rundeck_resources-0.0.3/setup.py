from os import path
from setuptools import setup
from rundeck_resources import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements/requirements.txt'),
          encoding='utf-8') as f:
    install_requires = f.read()

description = 'Rundeck Resources Generator'

setup(
    name='rundeck_resources',
    version=__version__,
    license='BSD',
    author='Elia El Lazkani',
    author_email='eliaellazkani@gmail.com',
    url='https://gitlab.com/elazkani/rundeck-resources',
    description=description,
    long_description=long_description,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'rundeck-resources = rundeck_resources.cli:main'
        ],
        'Importers': [
            'ChefImporter = rundeck_resources.chef_importer:ChefImporter'
        ],
        'Exporters': [
            'YAMLExporter = rundeck_resources.yaml_exporter:YAMLExporter'
        ]
    },
    packages=['rundeck_resources'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators'
    ],
    zip_safe=False
)
