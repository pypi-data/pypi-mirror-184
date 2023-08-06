from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name = "KitronikPicoRobotics",
    version = "1.0.0",
    description = "Kitronik Robotics Board for Raspberry Pi Pico to drive 4 motors (or 2 stepper motors) and 8 servos",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    py_modules = ["PicoRobotics"],
)