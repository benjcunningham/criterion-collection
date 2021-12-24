from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()


extras = {
    "quality": ["black", "flake8", "isort", "mypy", "types-requests"],
    "testing": ["pytest"],
}

extras["dev"] = extras["quality"] + extras["testing"]

setup(
    name="criterion-collection",
    version="0.1.0.dev0",
    author="Ben Cunningham",
    author_email="benjamescunningham@gmail.com",
    description="Utilities for scraping the Criterion Collection website",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/benjcunningham/criterion-collection",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "beautifulsoup4>=4.10.0",
        "pandas>=1.3.5",
        "requests",
    ],
    extras_require=extras,
    python_requires=">=3.9.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
