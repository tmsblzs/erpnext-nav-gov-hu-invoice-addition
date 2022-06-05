from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nav_gov_hu_invoice_addition/__init__.py
from nav_gov_hu_invoice_addition import __version__ as version

setup(
	name="nav_gov_hu_invoice_addition",
	version=version,
	description="This app contains additional settings for hungarian online invoice system.",
	author="tmsblzs",
	author_email="tmsblzs+github@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
