#!/bin/env python
# -*- coding: utf-8 -*-
# Author: Laurent Pointal <laurent.pointal@limsi.fr>

#from distutils.core import setup
import io
from setuptools import setup

setup(
    name='sunfluidhbox',
    version='0.2.0',
    author='Laurent Pointal',
    author_email='laurent.pointal@limsi.fr',
    url='https://perso.limsi.fr/pointal/dev:sunfluidhbox',
    download_url='https://sourcesup.renater.fr/projects/sunfluidhbox/',
    description='Python3 package to interface sunfluidh with external control program in Python.',
    packages=['sunfluidhbox'],
    keywords=['communication', 'sunfluidh', 'control'],
    license='CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)',
    classifiers=[
                'Development Status :: 4 - Beta',
                'Intended Audience :: Science/Research',
                'Natural Language :: English',
                'Operating System :: POSIX',
                'Programming Language :: Python :: 3',
                'License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)',
                'Topic :: Scientific/Engineering :: Physics',
                'Topic :: Software Development :: Libraries :: Python Modules',
             ],
    long_description=io.open("README.txt", encoding='utf-8').read(),
    )

