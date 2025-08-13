from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e . '
def get_requirements(file_path:str) -> List[str]:
    # this will return all the requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # to remove /n as readlines also add /n after every line in requirements.txt
        for i in range(len(requirements)):
            requirements[i] = requirements[i].replace("\n", "")
        # hyphen_e_dot is used in req.txt to initialize setup.py so we have to remove it from requirements as it is of no use.
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name = 'MLPROJECT',
    version = '0.0.1',
    author='Kunal',
    author_email = 'kunal964121@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
) 