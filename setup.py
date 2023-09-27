from setuptools import setup, find_packages

setup(
    name="Fight",
    version="0.1",
    packages=find_packages(),
    description="""Vechtspel met Tygo""",
    install_requires=[
            "pygame==2.5.2"
    ],
    entry_points={
        'console_scripts': [
            'pyfight = main:main',
        ],
    }
)
