from setuptools import setup

setup(

	name="physicspy",
	version="0.1.0",
	description="Package of scientific computing to solve problems in computational physics",
	author="Luis E. Sánchez Glz.",
	author_email="lsgm16308@gmail.com"
	url="https://luis2501.github.io/portfolio/portfolio-2/"
	packages=["physicspy", "physicspy/physics", "physicspy/integration", "physicspy/others"]
	install_requires=["numpy", "matplotlib", "plotly"]
	
)
