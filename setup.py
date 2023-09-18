from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='recursion_trace',
    version='0.2.0',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['graphviz', 'matplotlib', 'pydot', 'networkx'],
    author='Swayam Singh',
    author_email='hawkempire007@gmail.com',
    description='A package to trace recursive function calls and generate a recursion tree'
)
