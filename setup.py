# python setup.py sdist bdist_wheel
# python -m pip install --upgrade twine
# python -m twine upload dist/*
import setuptools

try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except UnicodeDecodeError:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

with open("aiobrawlstats/const/const.py", encoding="utf-8") as f:
    exec(f.read())

setuptools.setup(
    name="aiobrawlstats",
    version=locals()["__version__"],
    author=locals()["__author__"],
    description="Async BrawlStars API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/vladislavkovalskyi/aiobrawlstats",
    packages=setuptools.find_packages(),
    author_email="v.darknesssb@gmail.com",
    classifiers=[
        "Operating System :: OS Independent",
    ],
    install_requires=["aiohttp", "pydantic"]
)