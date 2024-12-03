from setuptools import setup, find_packages

setup(
    name='biclustlib',
    version='0.1',
    description='Library of biclustering algorithms, evaluation measures and dataset',
    url='https://github.com/padilha/biclustlib',
    author='...',
    author_email='...',
    license='GPLv3',
    packages=find_packages(),
    include_package_data=True,  # Include package data as specified in MANIFEST.in
    package_data={
        'biclustlib.datasets': [
            'data/*/*',  # Include all files in datasets/data directory and subdirectories
        ],
    },
    zip_safe=False,
)