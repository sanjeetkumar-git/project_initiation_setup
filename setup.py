import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "project_initiation_Setup"
AUTHOR_USER_NAME = "sanjeetkumar"
PROJECT_NAME = "Initiation_Setup"
AUTHOR_EMAIL = "kumarsanjeetyes@gmail.com"
DESC =  " A small python project initiation setup"

setuptools.setup(
    name=PROJECT_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESC,
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}-git/{REPO_NAME}",
    project_urls={
       "GitHub link" : f"https://github.com/{AUTHOR_USER_NAME}-git/{REPO_NAME}"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)