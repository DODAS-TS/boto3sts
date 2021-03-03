import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="boto3-sts",
    version="0.0.1",
    author="dciangot",
    author_email="diego.ciangottini@gmail.com",
    description="It's boto3 STS refresh function.",
    long_description=long_description,
    url="https://github.com/dodas-ts/boto3-sts",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    'boto3',
    'requests',
    'xmltodict',
    'liboidcagent'
   ]
)
