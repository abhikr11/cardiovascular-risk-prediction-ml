from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file:
        requirements = [line.strip()
                        for line in file
                        if line.strip() and                    # only include non empty lines
                        not line.startswith("#") and           # not include comments
                        not line.strip().startswith("-e .")]   # not include lines with -e .
    return requirements


setup(
    name = "cardio-risk-prediction",
    version = "0.0.1",
    description="Cardiovascular Risk Prediction using Machine Learning",
    author = "Abhijeet Kumar",
    author_email = "abhijeet.kr7252@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)