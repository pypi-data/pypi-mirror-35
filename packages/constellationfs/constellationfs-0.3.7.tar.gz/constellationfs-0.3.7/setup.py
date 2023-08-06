import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="constellationfs",
    version="0.3.7",
    author="ilrico",
    author_email="admin@constellation-fs.org",
    description="Incentivation system for IPFS pinning via Stellar micropayments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilrico/constellation-fs",
    packages=setuptools.find_packages(),
    keywords = ['IPFS', 'Stellar'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
