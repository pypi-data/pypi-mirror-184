# A sample Python project

A sample project to copy the correct structure of a python project.

## Pyproject.toml
Project properties to update:
* _name_ : name of the project
* _description_ : description of the project
* _authors_ : authors of the project
* _keywords_ : keywords to help search of the project
* _classifiers_ : one or more [classifiers](https://pypi.org/classifiers/) of the project
* _dependencies_ : equivalent to requirements.txt
* _urls_ : homepage, documentation and repository
* _scripts_ : startup script when executing like **python -m < project >**
* _tool.bumpver.file_pattern_ : name of the folder of the project

## Update to PyPi
Steps to update to pip:
* _tox -r_ : check integrity of the project and execute tests
* _bumpver update --patch_ : update version of the project. Also --minor and --major is supported
* _python -m build_ : build the project
* _twine check dist/*_ : check build files
* _twine upload dist/*_ : upload to PyPi (may upload before to testpypi with _twine upload -r testpypi dist/*_)
* _pip install < project >_ : to install the package and check it (may check before from testpypi with _pip install -i https://test.pypi.org/simple < project >_)

# Structure
Data folder is used for external files (like configuration files or scripts)

Basic packages to install: _pip install .[dev]_