from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name = "KitronikPicoAutonomousRoboticsPlatform",
    version = "1.0.0",
    description = "Kitronik Autonomous Robotics Platform (Buggy) for Pico",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    py_modules = ["PicoAutonomousRobotics"],
)