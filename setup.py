from setuptools import setup, find_packages
from typing import List

HYPEN_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    This functions reads the requirements file
    but removes the -e . line if it exists.
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements


setup(
    name='pygpt4all',
    version='0.1.0',
    author='Bhuwan',
    author_email='joshibhuwan078@gmail.com',
    description='A Python wrapper for the GPT-4 All API',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
