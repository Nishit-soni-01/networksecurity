from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function returns a list of requirements from requirements.txt.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and the editable install flag '-e .'
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Nishit Soni",
    author_email="ns2004.soni@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)