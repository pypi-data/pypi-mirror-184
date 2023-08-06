from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A basic package for a customized workflow using quantum espresso or abinit.'
LONG_DESCRIPTION = 'A basic package for a customized workflow using quantum espresso or abinit.'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Setting up
setup(
    name="minflow",
    version=VERSION,
    author="Rogerio Gouvea",
    author_email="<rogeriog.em@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=requirements,
    long_description_content_type="text/markdown",
    long_description=long_description,
    keywords=['python', 'dft', 'workflow', 'quantumespresso', 'abinit'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)
