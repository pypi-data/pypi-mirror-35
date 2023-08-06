import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="agora_demo",
    version="0.1.0",
    author="Neelesh Dodda",
    author_email="ndodda@berkeley.edu",
    description="A demo testing configuration and dataset management.",
    packages=setuptools.find_packages()
)
