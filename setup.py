from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="nyaascraper",
    version="1.0.1",
    description="A Python-based asynchronous library for scraping and searching torrents on nyaa.si and sukebei.nyaa.si.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Zrekryu",
    author_email="zrekryu@gmail.com",
    url="https://github.com/zrekryu/nyaascraper",
    keywords=["nyaa", "sukebei", "torrent", "asynchronous", "web scraping", "beautifulsoup4", "bs4", "httpx"],
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "httpx"
        ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries",
        ]
    )