from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of all the requirements in the requirements.txt file
    """
    requirement=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        if '-e .' in requirements:
            requirements.remove("-e .")   
    return requirements         

setup(
name='mlproject',
version='0.0.1',
author='Ashish',
author_email='ashishaggarwal1036@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)