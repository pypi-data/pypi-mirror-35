from setuptools import setup
import sys

requires = ['broadlink']
if sys.version_info.major == 2:
    requires.append('configparser')
setup(
    name='rmctl',
    version='0.1.1',
    packages={'pkg'},
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'rmctl = pkg.rmctl:main',
        ],
    },
    url='',
    license='BSD',
    author='mao2009',
    description='Simple cli client for broadlink',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
