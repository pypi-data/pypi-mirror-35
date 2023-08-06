from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='wsgimagic',
      version='0.1.0',
      description='Serverless WSGI apps made easy',
      packages=['wsgimagic'],
      author = "Kyle Hinton",
      license = "MIT",
      long_description=long_description,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"])

