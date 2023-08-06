import setuptools

setuptools.setup(
	name="torchpruner",
	version="0.0.4",
	description='Python library to perform pruning of pytorch neural networks',
	long_description='This library takes any pytorch neural network and prunes its weights while maintaining accuracy',
	author="Ashhadul Islam, Samir Brahim Belhaouari",
	packages=["torchpruner"]

	)