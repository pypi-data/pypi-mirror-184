import os
from setuptools import setup

if os.environ.get("DEMO_FLAG", "0") != "1":
    raise OSError("Get pwned")

setup(
    name="arturo-logging",
    version="9999.0.0",
    description="Security Risk Demo",
)