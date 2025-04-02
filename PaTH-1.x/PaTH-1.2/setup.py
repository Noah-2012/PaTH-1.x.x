from setuptools import setup, find_packages

setup(
    name="PaTH",
    version="1.3",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'PaTH=PaTH.cli:main',
        ],
    },
    install_requires=[],
    author="Noadsch12",
    description="Tool zum anzeigen eines vollständigen Trees.",
    license="GNU",
)
