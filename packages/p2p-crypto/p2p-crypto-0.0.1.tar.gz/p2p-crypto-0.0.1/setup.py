from setuptools import setup, find_packages
import re
from io import open

def read(filename):
    with open(filename, encoding="utf-8") as file:
        return file.read()

with open('p2p_crypto/version.py', 'r', encoding='utf-8') as f:  # Credits: LonamiWebs
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$",
                        f.read(), flags=re.MULTILINE).group(1)

setup(
    name="p2p-crypto",
    version=version,
    author="exsplash.it",
    description="Python3 library for interacting with P2P trading on different cryptoexchanges",
    long_description=read("README_pypi.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/exsplashit/p2p",
    license="MIT",
    keywords="p2p crypto api",
    project_urls={
        'Documentation': 'https://github.com/exsplashit/p2p',
        'Source': 'https://github.com/exsplashit/p2p/',
        'Tracker': 'https://github.com/exsplashit/p2p/issues',
    },
    install_requires=[
        'requests',
        'pandas'
    ],
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)