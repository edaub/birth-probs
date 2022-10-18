from setuptools import setup, find_packages

# Source dependencies from requirements.txt file.
try:
    with open("requirements.txt", "r") as f:
        lines = f.readlines()
        install_packages = [line.strip() for line in lines]
except FileNotFoundError:
    install_packages = []

setup(
    name="birth-probs",
    version="0.1",
    install_requires=install_packages,
    include_package_data=True,
    python_requires=">=3.6",
    author='Eric Daub',
    author_email="edaub@turing.ac.uk",
    url="https://github.com/edaub/birth-probs",
    # this should be a whitespace separated string of keywords, not a list
    keywords="pregnancy statistics",
    description="Tool for estimating weekly birth probabilities",
    long_description=open("./README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts" : ['birth-probs=birth_probs.birth_probs:main']},
)
