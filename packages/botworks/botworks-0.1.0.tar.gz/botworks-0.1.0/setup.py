import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="botworks",
    version="0.1.0",
    author="William Hanson",
    author_email="42045551+doubleyuhtee@users.noreply.github.com",
    description="Slack bot framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doubleyuhtee/botworks",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ),
)