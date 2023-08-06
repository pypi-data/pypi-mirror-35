import yaml

from setuptools import setup, find_packages
from os import path

# read the contents of README file
this_dir = path.abspath(path.dirname(__file__))

with open(path.join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="tradeoftimes",
    version=yaml.load(open("changelog.yml"))['versions'][-1]['name'],
    packages=["tradet"],
    install_requires=open(path.join(this_dir, 'requirements.txt')).read().split('\n'),
    
    # metadata to display on PyPI
    author="Gustavo6046",
    author_email="gugurehermann@gmail.com",
    description="Trade of Times: an experimental, demonstrative single & multiplayer RPG game, based on top of Peertable.",
    license="MIT",
    keywords=" ".join(['p2p', 'peer-to-peer', 'peer', 'network', 'infrastructure', 'game', 'test', 'experimental', 'protocol', 'demo', 'rpg', 'multiplayer']),
    
    long_description=long_description,
    long_description_content_type='text/markdown'
)