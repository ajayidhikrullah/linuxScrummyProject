import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

#allow setup.py to b run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ajayidhikrullahscrumy',
    version='0.01',
    packages=find_packages(),
    # packages=['ajayidhikrullahscrumy'],
    include_package_data=True,
    license='BSD License', #eg: license
    description='A simple django myscurmy app under the influence of Linuxjobber',
    long_description=README,
    url='https://www.example.com',
    author='AJAYI DHIKRULLAH ADEKUNLE',
    author_email='ajayidhikrullah@gmail.com'
    # classifiers=[
    #     'Environment :: web Environment',
    #     'Framework :: Django',
    #     'Framework :: Django :: X.Y', #X.Y TO b replaced later by me
    #     'Intended Audience :: developers in inuxjobber',
    #     'License :: OSI approved :: BSD License',
    #     'Operating Sytem :: OS Independent',
    #     'Programming language :: Python',
    #     'programming language :: Python :: 3.6+',
    #     'Topic :: Internet :: WWW/HTTP',
    # ],
)