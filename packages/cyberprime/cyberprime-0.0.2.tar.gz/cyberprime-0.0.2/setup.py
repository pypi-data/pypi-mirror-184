from setuptools import setup, find_packages
import os

VERSION = '0.0.2'
DESCRIPTION = 'test buiding packages'
LONG_DESCRIPTION = 'A package that allows to ___.'

# Setting up
setup(
    name="cyberprime",
    version=VERSION,
    author="Blank",
    author_email="<blank@dineonwine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(
        where='src/cyberprime',
        include='utils'
    ),
    install_requires=['numpy', 'matplotlib'],
    keywords=['python', 'useless'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)