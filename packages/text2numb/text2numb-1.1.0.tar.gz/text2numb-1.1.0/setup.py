import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = 'text2numb',
	version = '1.1.0',
	author = 'Pigeon Nation',
	author_email = 'pigeonnation2@gmail.com',
	description = 'Converts text into a numbers and back again. ',
	long_description = long_description,
	long_description_content_type="text/markdown",
	packages = setuptools.find_packages(),
	license = 'MIT',
	classifiers=[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Topic :: Other/Nonlisted Topic"
	]
)