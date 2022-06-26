import setuptools

import watkins

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="watkins",
    version=watkins.__version__,
    author="Chris Hannam",
    author_email="ch@chrishannam.co.uk",
    description="Log medical data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrishannam/watkins",
    packages=setuptools.find_packages(exclude="tests"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "influxdb-client",
        "kafka-python",
        "pyserial",
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "watkins-pulse=watkins.pulse:run",
        ]
    },
)
