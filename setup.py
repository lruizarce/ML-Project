from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """_summary_
        This function will return the list of requirements.
    Args:
        file_path (str): path to requirements file

    Returns:
        List[str]: returns a list of requirements
    """
    requirements = []
    with open("requirements.txt") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Luis Ruiz",
    author_email="luisruizarce@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
