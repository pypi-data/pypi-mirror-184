import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()
	
setuptools.setup(
	name = 'HashedDB',
	version = '0.0.1',
	author = 'Pigeon Nation',
	description = 'Secure Password Databases!',
	long_description = long_description,
	long_description_content_type="text/markdown",
	packages = setuptools.find_packages(),
	license = 'MIT',
	classifiers=[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Topic :: Security :: Cryptography"
	]
)