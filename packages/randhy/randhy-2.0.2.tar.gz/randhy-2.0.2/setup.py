from setuptools import setup

version = open('VERSION').read()
long_description = open('README.md').read()

__author__ = 'Sasho Savkov'
__credits__ = ["William Morgan"]
__license__ = "MIT"
__version__ = version
__email__ = "me@sasho.io"
__status__ = "Production"


setup(
    name='randhy',
    version=version,
    description='Approximate randomisation library',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    author='Sasho Savkov',
    author_email='me@sasho.io',
    url='https://www.github.com/asavkov/randhy/',
    package_dir={'': 'src'},
    packages=['randhy']
)
