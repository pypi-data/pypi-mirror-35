from setuptools import setup

setup(
    name='pyjvmgui',
    version='1.0',
    packages=['gui', 'gui.abstractions', 'pyjvm', 'pyjvm.ops', 'pyjvm.operands', 'pyjvm.platform', 'pyjvm.platform.sun',
              'pyjvm.platform.sun.misc', 'pyjvm.platform.sun.reflect', 'pyjvm.platform.java', 'pyjvm.platform.java.io',
              'pyjvm.platform.java.lang', 'pyjvm.platform.java.security'],
    url='https://github.com/MatevzFa/pyjvm',
    license='GPL-3.0',
    author='matevz',
    author_email='matevz.fabjancic@gmail.com',
    description=''
)
