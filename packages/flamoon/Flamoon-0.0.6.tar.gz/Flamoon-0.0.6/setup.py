# setup.py

# Фомирует необходимые данные для установки пакета flamoon

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from setuptools import setup, find_packages

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

PACKAGE = 'flamoon'
VERSION = __import__(PACKAGE).__version__
NAME = 'Flamoon'
DESCRIPTION = 'Надстройка над Flask, для быстрой и удобной web-разработки.'
AUTHOR = 'volitilov'
AUTHOR_EMAIL = 'volitilov@gmail.com'
URL = 'https://github.com/volitilov/flamoon'


with open("pypi_doc.md", "r") as fh:
    README = fh.read()
    

setup(
    name=NAME, 
    version=VERSION, 
    description=DESCRIPTION, 
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Operating System :: POSIX :: Linux'],  
    url=URL,
    author=AUTHOR, 
    author_email=AUTHOR_EMAIL, 
    license='MIT', 
    packages=find_packages(), 
    install_requires=[
        'Flask==1.0.2', 
        'Flask-Login==0.4.1',
        'Flask-Mail==0.9.1',
        'python-dotenv==0.8.2',
        'Flask-SQLAlchemy==2.3.2',
        'Flask-Migrate==2.1.1',
        'psycopg2==2.7.4',
        'psycopg2-binary==2.7.4'
    ], 
    include_package_data=True,
    zip_safe=False,
    test_suite='tests/test_basic',
    entry_points={
        'console_scripts': [
            'flamoon = flamoon.cli:main',
        ],
    },
)