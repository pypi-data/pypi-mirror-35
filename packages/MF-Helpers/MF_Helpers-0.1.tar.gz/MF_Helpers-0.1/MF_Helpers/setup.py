from setuptools import setup, find_packages

setup(name='MF_Helpers',
	version='0.1',
	description='Modeling Factory Utilities',
	url='https://vc-bds002.vimpelcom.global/model-factory/MF_Helpers',
	author='Natalia Galanova',
	author_email='NGalanova@nsk.beeline.ru',
	packages=find_packages(),
	install_requires=[ 'numpy', 'pandas', 'sklearn' ])