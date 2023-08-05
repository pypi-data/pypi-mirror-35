from setuptools import setup

setup(
    name="scuttlebutt",
    version="0.1",
    description="Implementation of the the Secure Scuttlebutt protocol.",
    url="https://github.com/supakeen/scuttlebutt",
    author="supakeen",
    author_email="cmdr@supakeen.com",
    packages=["scuttlebutt"],
    install_requires=[
        "cryptography"
    ],
    tests_require=[
        "nose",
        "aiounittest"
    ],
    test_suite="nose.collector"
)
