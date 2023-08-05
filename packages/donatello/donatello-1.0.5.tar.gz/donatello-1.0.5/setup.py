
from setuptools import setup

NAME = "donatello"
DESCRIPTION = "🐍 Python API wrapper for Ukrainian donate service Donatello"
URL = "https://github.com/selfkilla666/donatello"
EMAIL = "selfkilla666@yahoo.com & olddft@gmail.com"
AUTHOR = "selfkilla666 & Beengoo"
PYTHON_REQUIRES = ">=3.7.0"
VERSION = "1.0.5"

REQUIRED = ["aiohttp", "requests", "pydantic"]

try:
    with open("README.md", encoding="utf-8") as file:
        LONG_DESCRIPTION = "\n" + file.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=PYTHON_REQUIRES,
    url=URL,
    download_url="https://github.com/selfkilla666/donatello/blob/main/dist/donatello-1.0.5.tar.gz",
    packages=["donatello"],
    install_requires=REQUIRED,
    license="MIT License (MIT)",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
		"Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Utilities",
		"Typing :: Typed",
    ]
)