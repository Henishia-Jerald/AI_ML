from setuptools import setup, find_packages 
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requitements(file_path:str) -> list[str]:
    with open(file_path,'r') as file_obj:
        requirements = file_obj.readline()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip()!= HYPHEN_E_DOT]
    return requirements

setup(
    name= "CyberSecurity",
    version= "0.0.1",
    author= "Arockia Henishia",
    author_email="henishiaj@gmail.com",
    install_requires = get_requitements('requirements.txt')

)