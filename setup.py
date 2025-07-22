from setuptools import find_packages, setup
from typing import List


HYPHEN_E__DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements: List[str]=[]
    with open("requirements.txt") as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E__DOT in requirements:
            requirements.remove(HYPHEN_E__DOT)

    return requirements



setup(
    name="mlproject",
    version="0.0.1",
    author="Sufyan",
    author_email="sufyan.abdulrahman55@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
