from os import path
from distutils.core import setup
from setuptools import find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyquotex',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    version='1.0.0',
    license='MIT',
    description='Quotex Api Client written in python.',
    author='Cleiton Leonel Creton',
    author_email='cleiton.leonel@gmail.com',
    url='https://github.com/cleitonleonel/pyquotex.git',
    # download_url='https://github.com/cleitonleonel/pyquotex/archive/v_1.0.0.tar.gz',
    keywords=['SOME', 'MEANINGFULL', 'KEYWORDS'],
    install_requires=[
        'setuptools==70.2.0', # Need to install setuptools
        "certifi==2023.7.22", # Need to install certifi
        # "greenlet",
        # "pyOpenSSL",
        # "pytz",
        # "requests-toolbelt",
        'requests==2.31.0', # Need to install requests
        'beautifulsoup4==4.12.2', # Need to install beautifulsoup4
        'websocket-client==1.8.0', # Need to install websocket-client
        'playwright==1.44.0', # Need to install playwright==1.44.0
        'playwright-stealth==1.0.6', # Need to install playwright-stealth
        'pyfiglet==1.0.2', # Need to install pyfiglet
        # 'numpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
