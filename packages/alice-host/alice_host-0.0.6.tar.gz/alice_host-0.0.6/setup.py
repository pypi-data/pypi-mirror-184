from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="alice_host",
    version="0.0.6",
    description="Alice Host its come with ui page!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alice-api/alice-host",
    author="pipatpong",
    author_email="kanyatit2500@email.com",
    license="MIT",
    packages=["alice_host"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "templates"
    ],
)
