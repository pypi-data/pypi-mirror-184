from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name = "KitronikPicoMotorDriver",
    version = "1.0.0",
    description = "Kitronik Motor Driver Board for Raspberry Pi Pico to drive two motors simultaneously and 4 external connections to GPIO pins",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    py_modules = ["PicoMotorDriver"],
)