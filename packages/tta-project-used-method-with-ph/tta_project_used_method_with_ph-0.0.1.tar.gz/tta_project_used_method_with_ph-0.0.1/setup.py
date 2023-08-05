import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8")as fh:
    long_description = fh.read()

setuptools.setup(
    name="tta_project_used_method_with_ph",
    version="0.0.1",
    author="TTA_DE_PH",
    author_email="kanjanggon@crowdworks.kr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ParkHwan/create_module",
    project_urls={
        "Bug Tracker": "https://github.com/ParkHwan/create_module/issues"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},

    packages=find_packages(where="src"),
    python_requires=">=3.9"
)
