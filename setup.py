from setuptools import find_packages
from setuptools import setup


def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='emplocity',
    packages=find_packages(),
    include_package_data=True,
    author='Marcin Koprek',
    entry_points={'console_scripts': ['emplocity_server = emplocity:get_app']},
    install_requires=read_requirements()
)
