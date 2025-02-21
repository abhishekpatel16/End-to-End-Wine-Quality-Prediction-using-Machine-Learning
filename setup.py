import setuptools  # Importing setuptools, a library for packaging Python projects

# Opening the README.md file to read its contents for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()  # Reading the contents of README.md

__version__ = "0.0.0"  # Defining the initial version of the package

# Defining project metadata
REPO_NAME = "End-to-End-Wine-Quality-Prediction-using-Machine-Learning"  # Name of the GitHub repository
AUTHOR_USER_NAME = "abhishekpatel16"  # GitHub username of the author
SRC_REPO = "mlProject"  # Name of the source repository/package
AUTHOR_EMAIL = "abhishekpatel0771@gmail.com"  # Author's email address

# Calling setuptools.setup() to configure the package details
setuptools.setup(
    name=SRC_REPO,  # Name of the package
    version=__version__,  # Package version
    author=AUTHOR_USER_NAME,  # Author's name
    author_email=AUTHOR_EMAIL,  # Author's email
    description="A small python package for ml app",  # Short description of the package
    long_description=long_description,  # Detailed description from README.md
    long_description_content="text/markdown",  # Content type of long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # GitHub repository URL
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # URL for reporting issues
    },
    package_dir={"": "src"},  # Directory where the package is located
    packages=setuptools.find_packages(where="src")  # Automatically find packages inside 'src'
)
