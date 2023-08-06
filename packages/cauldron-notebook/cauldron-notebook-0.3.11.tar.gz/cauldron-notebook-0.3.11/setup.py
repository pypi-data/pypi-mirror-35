import glob
import json
import os

from setuptools import find_packages
from setuptools import setup

# python3 setup.py register -r pypitest

# UNIX:
# rm -rf ./dist
# python3 setup.py sdist bdist_wheel
# twine upload dist/cauldron*
# python3 conda-recipe/conda-builder.py

# WINDOWS:
# rmdir dist /s /q
# python setup.py sdist bdist_wheel
# twine upload dist/cauldron*
# python conda-recipe\conda-builder.py

MY_DIRECTORY = os.path.dirname(__file__)
with open(os.path.join(MY_DIRECTORY, 'cauldron', 'settings.json'), 'r') as f:
    settings = json.load(f)


def populate_extra_files():
    """
    Creates a list of non-python data files to include in package distribution
    """

    out = ['cauldron/settings.json']

    for entry in glob.iglob('cauldron/resources/examples/**/*', recursive=True):
        out.append(entry)

    for entry in glob.iglob('cauldron/resources/templates/**/*', recursive=True):
        out.append(entry)

    for entry in glob.iglob('cauldron/resources/web/**/*', recursive=True):
        out.append(entry)

    return out

setup(
    name='cauldron-notebook',
    version=settings['version'],
    description='The Unnotebook: Scientific Analysis Environment',
    url='https://github.com/sernst/cauldron',
    author='Scott Ernst',
    author_email='swernst@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={'': populate_extra_files()},
    include_package_data=True,
    zip_safe=False,
    entry_points=dict(
        console_scripts=['cauldron=cauldron.invoke:run']
    ),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    install_requires=[
        'pandas',
        'numpy',
        'jinja2',
        'markdown',
        'pygments',
        'beautifulsoup4',
        'flask',
        'requests'
    ],
    extras_require={
        'plotly': ['plotly'],
        'matplotlib': ['matplotlib'],
        'bokeh': ['bokeh'],
        'seaborn': ['seaborn']
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov']
)
