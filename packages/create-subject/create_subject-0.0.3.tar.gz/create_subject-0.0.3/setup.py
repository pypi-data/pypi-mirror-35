import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# print(setuptools.find_packages())

setuptools.setup(
    name="create_subject",
    version="0.0.3",
    author="Adam Johnston",
    author_email="adamjohnston151@yahoo.com",
    description="Package to expose subject with next, filter, and subscribe methods - based on yurikoex's npm subject-with-filter package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aj03794/create-subject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)