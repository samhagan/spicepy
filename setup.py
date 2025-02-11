#!/usr/bin/env python3
"""spicepy is the Spice.xyz client library.

"""


from setuptools import setup, find_packages


def setup_package():
    setup(
        name="spicepy",
        version="0.2.0",
        maintainer="Spice AI, Inc.",
        maintainer_email="webmaster@spice.ai",
        author="Spice AI, Inc.",
        author_email="webmaster@spice.ai",
        url="https://github.com/spiceai/spicepy",
        description="Spice.xyz client library - data and AI infrastructure for web3.",
        license="Apache 2.0",
        packages=["spicepy"],
        install_requires=["pyarrow", "pandas", "web3>=5.27.0"],
        python_requires=">=3.8",
    )


if __name__ == "__main__":
    setup_package()
