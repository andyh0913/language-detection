from setuptools import setup, find_packages

# https://python-packaging.readthedocs.io/en/latest/minimal.html

setup(
    name='language-detection',
    version='0.0.1',
    description='Detect if a language exists in the texts',
    url='https://github.com/andyh0913/language-detection',
    author='andyh0913',
    license='Apache-2.0',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    package_data={
        'langdetect': ['data/pattern/*/*.txt'],
    },
)