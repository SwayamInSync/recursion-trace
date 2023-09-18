from setuptools import setup, find_packages

setup(
    name='recursion_trace',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'graphviz',
    ],
    author='Swayam Singh',
    author_email='hawkempire007@gmail.com',
    description='A package to trace recursive function calls and generate a recursion tree'
)
