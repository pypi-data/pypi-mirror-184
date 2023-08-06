from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gotji",
    version="0.0.2",
    description="gotji module on top !!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="GxdjCoding",
    author_email="meoawcute@gmail.com",
    license="MIT",
    packages=["gotji"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests"
    ],
)
