# setup.py

# Фомирует необходимые данные для установки пакета flamoon

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from setuptools import setup, find_packages

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flamoon', 
    version='0.0.1', 
    description='Надстройка над Flask, для быстрой и удобной web-разработки.', 
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Operating System :: POSIX :: Linux'],  
    url='https://github.com/volitilov/flamoon', 
    author='volitilov', 
    author_email='volitilov@gmail.com', 
    license='MIT', 
    packages=find_packages(), 
    install_requires=['Flask==1.0.2', ], 
    include_package_data=True,
    zip_safe=False
)