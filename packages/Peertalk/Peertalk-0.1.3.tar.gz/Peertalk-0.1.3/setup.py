import yaml

from setuptools import setup, find_packages
from os import path

# read the contents of README file
this_dir = path.abspath(path.dirname(__file__))

with open(path.join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="Peertalk",
    version=yaml.load(open("changelog.yml"))['versions'][-1]['name'],
    packages=["peertalk"],
    
    # metadata to display on PyPI
    author="Gustavo6046",
    author_email="gugurehermann@gmail.com",
    description="An experimental, demonstrative chat protocol and implementation for use in Peertable networks",
    license="MIT",
    keywords=" ".join(['p2p', 'peer-to-peer', 'peer', 'network', 'infrastructure', 'chat', 'test', 'experimental', 'protocol', 'demo', 'talk']),
    
    long_description=long_description,
    long_description_content_type='text/markdown'
)