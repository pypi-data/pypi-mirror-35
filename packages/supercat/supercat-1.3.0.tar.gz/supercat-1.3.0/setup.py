from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

with open(path.join(here, 'supercat', 'version.txt')) as f:
    version = f.read().strip()

setup(
    name='supercat',
    description='Librería y réferi para el juego de gato anidado',
    long_description=long_description,
    url='https://github.com/categulario/supercat',

    version=version,

    author='Abraham Toriz Cruz',
    author_email='categulario@gmail.com',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='tictactoe, gato, ultimate tictactoe',

    packages=[
        'supercat',
        'supercat.players',
    ],

    package_data={
        'supercat': ['assets/*.png', 'version.txt'],
    },

    entry_points={
        'console_scripts': [
            'referi = supercat.main:referi',
        ],
    },

    install_requires=[
        'pygame',
    ],

    setup_requires=[
        'pytest-runner',
    ],

    extras_require={
        'test': [
            'pytest',
            'flake8',
        ]
    },
)
