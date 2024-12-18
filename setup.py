from setuptools import setup, find_packages

setup(
    name="my-library",  # Уникальное имя на PyPI
    version="0.1.0",  # Версия
    author="Your Name",
    author_email="your_email@example.com",
    description="A custom library for parsing, compiling, and managing structured data.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-library",  # Замените на ваш репозиторий
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
