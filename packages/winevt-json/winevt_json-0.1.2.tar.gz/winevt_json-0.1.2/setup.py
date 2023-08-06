from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="winevt_json",
    version="0.1.2",
    author="Rob Noeth",
    author_email="oss@leveleffect.com",
    description="A utility to convert windows system event logs into json objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LevelEffect/winevt_json",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: System :: Logging",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='infosec forensics threathunting',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    
    # Required Packages
    install_requires=[
        'click>=6'
        'lxml>=4', 
        'python-evtx<1', 
        ],


    # Console entry point
    entry_points=
    {
        'console_scripts': 
        [
            'winevt_json=winevt_json:main'
        ]
    },

    # URLs
    project_urls = {
        'Bug Reports':  'https://github.com/LevelEffect/winevt_json/issues',
        'Source':       'https://github.com/LevelEffect/winevt_json/'
    }

)
