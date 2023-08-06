import sys
from setuptools import setup

requires = []
if sys.version < '3.5':
    requires.append('typing')

setup(
    name='pypledge',
    maintainer='Andrew Aldridge',
    maintainer_email='i80and@foxquill.com',
    description='Binding for the OpenBSD pledge(2) system call',
    long_description=open('README.rst').read(),
    version='0.3',
    license='MIT',
    url='https://gitlab.com/i80and/pypledge',
    packages=['pypledge'],
    package_data={'pypledge': ['py.typed']},
    test_suite=None,
    install_requires=requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: BSD :: OpenBSD',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])
