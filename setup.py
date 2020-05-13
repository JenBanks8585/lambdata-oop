# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="Order", # the name that you will install via pip
    version="1.1.6",
    author="Jen Banks",
    author_email="jenniferbanks8585@gmail.com(opens in new tab)",
    description="Steak & Shake order helper",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/JenBanks8585/lambdata-oop",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)