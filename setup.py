from setuptools import find_packages , setup
from typing import List



def get_requirements()-> List[str]:

    requirements_list : List[str] =[]

    return requirements_list



setup(

name='Sensor',
version='0.0.1',
author='Sandhya Kushwaha',
author_email="sanidhisuman25@gmail.com",
packages= find_packages(),

install_requires =["pymongo"]



)