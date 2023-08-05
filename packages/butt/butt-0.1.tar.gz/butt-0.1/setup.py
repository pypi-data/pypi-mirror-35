from setuptools import setup

setup(
    name="butt",
    version="0.1",
    description="A command line client for scuttlebutt.",
    url="https://github.com/supakeen/butt",
    author="supakeen",
    author_email="cmdr@supakeen.com",
    packages=["butt"],
    install_requires=[
        "scuttlebutt"
    ],
    tests_require=[
        "nose",
        "aiounittest"
    ],
    test_suite="nose.collector"
)
