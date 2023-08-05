from setuptools import setup, find_packages

long_description = """
GUI wrapper for pdfconduit.
"""

setup(
    name='pdfconduit-gui',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyPDF3>=0.0.6',
        'pdfrw',
        'PyMuPDF',
        'Pillow',
        'PySimpleGUI>=2.9.0',
        'reportlab',
        'looptools',
        'pdfconduit',
    ],
    include_package_data=True,
    url='https://github.com/mrstephenneal/pdfconduit',
    license='',
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    description='PDF toolkit for preparing documents for distribution.',
    long_description=long_description,
)
