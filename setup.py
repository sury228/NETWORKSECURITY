from setuptools import setup, find_packages
from typing import List

requirement_list: List[str] = []
def get_requirements()-> List[str]:
    try:
        with open('requirements.txt', 'r') as file:
          lines = file.readlines()

          for line in lines:
             requirement=line.strip()
             if requirement and requirement != '-e .':
                requirement_list.append(requirement)
    except FileNotFoundError:
           print("requirements.txt file not found. Please make sure it exists in the project directory.")


    return requirement_list

print(get_requirements())

    
setup(
    name='networksecurity',
    version='0.0.1',
    author='Suryansh jha',
    author_email="suryanshjha0705@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)  
