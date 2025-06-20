from setuptools import setup, find_packages
from typing import List

HYPEN_DOT = '-e.'


def get_requirements(file_path: str) -> List[str]:
    """"
    This function reads the requirements file but removes the hypen_dot i.e. -e. if present
    """
    requirements = []
    with open(file_path, 'r') as file:
    requirements = file.readlines()
    requirements = [req.repplace('\n', '') for req in requirements]
    if HYPEN_DOT in requirements:
    requirements.remove(HYPEN_DOT)
    return requirements


setup(
    name='temp_now',
    version=0.0.1,
    author='00bhuwan',
    author_email='joshibhuwan078@gmail.com',
    description="A temperature prediction project",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
