import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prawframe",
    version="0.0.1",
    author="py-am-i",
    author_email="duckpuncherirl@gmail.com",
    description="prawframe is a small framework for running plugin-based reddit bots. prawframe supports scheduling plugins and includes a remote python console for modifying your bot's behavior while it runs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wykleph/prawframe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
