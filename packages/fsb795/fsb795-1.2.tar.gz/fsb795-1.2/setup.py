import fsb795
from setuptools import setup, find_packages
setup(name='fsb795',
    version='1.2',
    py_modules=['fsb795'],
    description='Obtaining the attributes of a qualified certificate, defined by the Order of the FSB 795', 
    long_description='Obtaining the attributes of a qualified certificate, \n\tdefined by the Order of the Federal Security Service \n\tof the Russian Federation of December 27, 2011 No. 795', 
    packages=find_packages(),
    install_requires=[
	'pyasn1', 'six'
    ],
    platforms=['any'],
    classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3.5',
	],
    test_suite='test795',
    author='Vladimir Orlov', 
    author_email='vorlov@lissi.ru', 
    license='GNU General Public License')
