import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="protocolws",
    version="0.0.1",
    author="Michael Pan",
    author_email="panmpan@gmail.com",
    description="Simple protocol websocket server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/panmpan17/ProtocolWebsocket",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)