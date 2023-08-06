from os import path
from sys import path as sys_path

from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install

this_directory = path.abspath(path.dirname(__file__))
srcdir = path.join(this_directory, "src/")
sys_path.insert(0, srcdir)

import rt.get_rt as get_rt

class DevelopWithRt(develop):
    def run(self):
        develop.run(self)
        get_rt.download()


class InstallWithRt(install):
    def run(self):
        install.run(self)
        get_rt.download()


setup(
    name='pyjvmgui',
    version='1.2.5',
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

    install_requires=['PySide2'],

    cmdclass={
        'install': InstallWithRt,
        'develop': DevelopWithRt,
    },
)
