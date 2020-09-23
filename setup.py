import os
from setuptools import setup, find_packages

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long = f.read()
setup(
    name='pyqt5-material',
    version='1.14.3',
    packages=['pyqt5_material', 'pyqt5_material.resources'],
    author='Yeison Cardona, Aman Anifer',
    author_email='yencardonaal@unal.edu.co, amananiferfiaff@gmail.com',
    maintainer='Aman Anifer',
    maintainer_email='amananiferfiaff@gmail.com',
	url='https://github.com/FuturisticGoo/pyqt5-material',
    download_url='https://github.com/FuturisticGoo/pyqt5-material',
	keywords=['PyQt5','pyqt','material','stylesheet'],
    install_requires=['pyqt5',
                      ],

    include_package_data=True,
    license='BSD License',
    description="PyQt5 Stylesheet.",
    long_description = long,
	long_description_content_type='text/markdown',

    classifiers=[

    ],

)
