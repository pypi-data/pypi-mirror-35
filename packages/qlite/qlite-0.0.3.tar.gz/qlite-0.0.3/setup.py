from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="qlite",
    version="0.0.3",
    author="BorisPlus",
    author_email="boris-plus@mail.ru",
    description="QLite is a lite project of SQLite ORM at Python3 for SQLite, as lite ORM for lite SQL.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BorisPlus/otus_webpython_005",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
