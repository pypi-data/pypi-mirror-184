from setuptools import setup, find_packages

setup(
    name="unid",
    version="0.0.0rc6",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    keywords=["manager", "id", "python", "identifier"],
    install_requires=[]
)