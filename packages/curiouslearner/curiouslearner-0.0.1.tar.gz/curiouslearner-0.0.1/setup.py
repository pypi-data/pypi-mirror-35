import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="curiouslearner",
    version="0.0.1",
    author="Sanyam Khurana",
    author_email="sanyam@sanyamkhurana.com",
    description="Meet Sanyam Khurana (CuriousLearner)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/curiouslearner/curiouslearner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
