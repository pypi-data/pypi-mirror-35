from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sklPCA',
    version='1.0.0',
    description='Supervised Kernel-Based Longitudinal PCA (skl-PCA)',
    long_description=long_description,
    url='http://mindstrong.com',
    author='Mindstrong Health Data Science',
    author_email='datascience@mindstronghealth.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3'
    ],
    keywords='digital biomarkers, supervised methods, kernel methods, longitudinal methods, dimension reduction, machine learning',
    packages=['sklPCA'],
    install_requires=['numpy','scipy', 'pandas','sklearn'],
    package_data={},
    include_package_data=False,
    scripts = ['examples.py'],
)