from os import path
from sys import path as sys_path

from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
srcdir = path.join(this_directory, "src/")
sys_path.insert(0, srcdir)

setup(
    name='pyjvmgui',
    version='1.2.3',
    url='https://github.com/MatevzFa/pyjvm',
    license='GPL-3.0',
    author='matevz',
    author_email='mf6422@student.uni-lj.si',
    description='A GUI for the PyJVM',

    packages=find_packages('src'),
    py_modules=['pyjvmgui'],

    package_dir={'': 'src'},

    entry_points={
        'console_scripts': ['pyjvmgui=pyjvmgui:main']
    },

    install_requires=['PySide2']
)
