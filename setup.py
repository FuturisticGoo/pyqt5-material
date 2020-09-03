import os
from setuptools import setup, find_packages

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pyqt5-material',
    version='1.14',
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
    #    long_description = README,

    classifiers=[

    ],

)
