



import setuptools

with open("README.md", "r") as fh: 
	long_description = fh.read()

setuptools.setup(
	name="zeiterfassung",
	version="0.0.1",
	author="fichtnerfl64707",
	author_email="florian.fichtner96@googlemail.com",
	description="A simple package to concure your working tims",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/fichtnerfl64707/zeiterfassung",
	packages=setuptools.find_packages(),
	include_package_data=True,
	scripts=['bin/zeiterfassung'],

#	entry_points={
 #       'console_scripts': [
  #      	'zeiterfassung = zeiterfassung:main'
#			]
#	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	#python_requires='>=3.5.2',
)
