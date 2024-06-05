from setuptools import setup, find_packages

setup(
    name="encryption_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "cryptography",
    ],
   
     description="A simple encryption and decryption library",
   
)
