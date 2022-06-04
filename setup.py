from setuptools import setup

setup(

	name="PhysicsPy",
	version="0.1",
	description="Package of scientific computing to solve problems in Computational Physics",
	author="Luis",
	author_email="lsgm16308@gmail.com"
	url="https://luis2501.github.io/portfolio/portfolio-2/"
	packages=["physicspy", "physicspy/physics", "physicspy/integration"]
	install_requires=["numpy", "matplotlib", "plotly"]
	
)
