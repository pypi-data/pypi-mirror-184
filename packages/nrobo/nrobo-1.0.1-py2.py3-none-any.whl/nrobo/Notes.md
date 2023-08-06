# Allure Reporting Framework
* Allure Reports 
https://docs.qameta.io/allure-report/
* Allure Command Line Tools
https://docs.qameta.io/allure/#_commandline
$ brew tap qameta/allure
$ brew install allure

# Generate and save allure report as html

`allure generate tests_advanced_reports --clean`

# Packaging and Publishing to PyPi
- `python3 -m pip install --upgrade build`
  - `python3 -m build`
- `python3 -m pip install --upgrade twine`
  - `python3 -m twine upload --repository testpypi dist/*`


# Key Files
- `pyproject.toml`
- `nrobo/__init__.py`
- `nrobo/__main__.py`
- `speedboat.py`
- `requirements.py`
- `Notes.md`
- `README.md`
- `conftest.py`