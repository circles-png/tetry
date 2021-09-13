from setuptools import find_packages, setup

with open('readme.md') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

__version__ = ''
__licence__ = ''
__author__ = ''
__name__ = ''

with open('tetry/__init__.py') as f:
    for line in f.read().splitlines():
        if line.startswith('__'):
            exec(line)

source = 'https://github.com/apes0/tetry'

setup(
    url=source,
    name=__name__,
    license=__licence__,
    project_urls={
        'Source': source,
        'Tracker': f'{source}/issues',
    },
    packages=find_packages(
        include=['tetry', 'tetry.api', 'tetry.oldApi', 'tetry.bot', ]),
    version=__version__,
    description='tetr.io api wrapper',
    long_description=readme,
    long_description_content_type='text/markdown',
    author=__author__,
    python_requires='>=3.6',
    install_requires=requirements
)
