from setuptools import setup

setup(
    name="prattle",
    version="0.1",
    description="A scuttlebutt bridge written in Tornado.",
    url="https://github.com/supakeen/prattle",
    author="supakeen",
    author_email="cmdr@supakeen.com",
    packages=["prattle"],
    install_requires=[
        "scuttlebutt",
        "tornado"
    ],
    tests_require=[
        "nose",
        "aiounittest"
    ],
    test_suite="nose.collector"
)
