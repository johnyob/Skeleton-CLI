import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

requires = [
    "docopt"
]

packages = [
    "client",
    "client.commands",
    "client.helpers"
]

setuptools.setup(
    name="skeleton-cli",
    version="0.0.1",
    author="Alistair O'Brien",
    author_email="alistair@duneroot.co.uk",
    description="A simple modular command line interface skeleton program package.",
    long_description=long_description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    url="https://github.com/johnyob/Skeleton-CLI",
    packages=packages,
    install_requires=requires,
    entry_points={
        "console_scripts": [
            "client=client.__main__:main"
        ]
    }
)
