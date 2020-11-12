from setuptools import setup

setup(
    name="megalinter",
    version="0.1",
    description="Mega-Linter",
    url="http://github.com/nvuillam/mega-linter",
    author="Lukas Gravley and Nicolas Vuillamy",
    author_email="nicolas.vuillamy@gmail.com",
    license="MIT",
    packages=["megalinter", "megalinter.linters", "megalinter.reporters"],
    install_requires=[
        "gitpython",
        "jsonschema",
        "mkdocs",
        "mkdocs-material",
        "pygithub",
        "pytablewriter",
        "pytest-cov",
        "pyyaml",
        "requests",
        "terminaltables",
        "yq",
    ],
    zip_safe=False,
)
