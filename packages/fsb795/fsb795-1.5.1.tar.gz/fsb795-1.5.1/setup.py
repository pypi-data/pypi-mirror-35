import fsb795
import os
from setuptools import setup, find_packages
s = '/'
print(os.path.abspath(__file__))
ff = os.path.abspath(__file__)
ff1 = os.path.dirname(ff)
ld1 = os.path.join(ff1, 'README.txt')
#print(os.path.abspath(os.curdir))
ld=open(ld1).read()
setup(name='fsb795',
    version='1.5.1',
    py_modules=['fsb795'],
    description='Obtaining the attributes of a qualified certificate, defined by the Order of the FSB 795', 
#    long_description='Obtaining the attributes of a qualified certificate, \n\tdefined by the Order of the #Federal Security Service \n\tof the Russian Federation of December 27, 2011 No. 795', 
    packages=find_packages(),
#    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    long_description=ld,
    install_requires=[
	'pyasn1>=0.4.4', 'pyasn1-modules>=0.2.2', 'six'
    ],
    platforms=['any'],
    classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
	'Programming Language :: Python',
        'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.5',
        'Natural Language :: Russian',
	],
    test_suite='test795',
    author='Vladimir Orlov', 
    author_email='vorlov@lissi.ru',
    url='https://pypi.org/project/fsb795/',
    license='MIT License')
