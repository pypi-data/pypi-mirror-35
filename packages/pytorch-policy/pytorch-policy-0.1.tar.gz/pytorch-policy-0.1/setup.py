from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pytorch-policy',
      version='0.1',
      description='Reinforcement Learning in Pytorch',
      url='https://github.com/navneet-nmk/pytorch-rl',
      author='Navneet M Kumar',
      author_email='navneet.nmk@gmail.com',
      packages=setuptools.find_packages(),
      license='MIT',
      zip_safe=False)