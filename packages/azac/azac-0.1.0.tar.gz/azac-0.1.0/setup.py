from distutils.core import setup
import os
from setuptools import find_packages

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    name='azac',
    packages=find_packages('.'),
    version='0.1.0',
    license='',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mikolaj Zabinski',
    author_email='mzabinski94@gmail.com',
    # Either the link to your github or to your website
    url='',
    # Link from which the project can be downloaded
        download_url='',
        # List of keywords
        keywords=[],
        # List of packages to install with this one
        install_requires=[],
        # https://pypi.org/classifiers/
        classifiers=[
                "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
    ]
)
