from setuptools import setup, find_packages

setup(
    name='analysepredmpw',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    url='https://github.com/MartinPWierzbicki/EDSA-predict-package',
    author='MartinPWierzbicki',
    author_email='martin.piotr.wierzbicki@gmail.com'
)
