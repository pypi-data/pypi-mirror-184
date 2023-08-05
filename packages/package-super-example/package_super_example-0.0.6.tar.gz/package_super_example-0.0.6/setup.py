from configparser import ConfigParser
from setuptools import setup, find_packages

config = ConfigParser(delimiters=['='])
config.read('settings.ini')
cfg = config['DEFAULT']

# install_requires will be filled automatically in pipfile_parse.py:
setup(
    name = cfg['lib_name'],
    version=cfg['version'],
    packages=find_packages(),
    install_requires = ['pandas', 'plotly', 'seaborn'], # <-- DO NOT EDIT, THIS LINE IS AUTOGENERATED
    long_description=cfg['long_description'],
    description=cfg['description']
)
    