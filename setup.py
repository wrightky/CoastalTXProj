from setuptools import setup, find_packages

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name = 'coastx',
    version = '1.0.0',
    license = 'MIT',
    description = 'Linear Reference Frame for the Coast of Texas',
    long_description=LONG_DESCRIPTION,
    long_description_content_type = 'text/markdown',
    author = 'Kyle Wright',
    author_email = 'Kyle.Wright@twdb.texas.gov',
    url = 'https://github.com/wrightky/CoastalTXProj',
    packages = find_packages(),
    package_data = {'coastx':['transform_grid.nc']},
    include_package_data = True,
    keywords='Texas coastal geotransform reference frame',
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    install_requires = ['numpy','matplotlib','xarray'],
)
