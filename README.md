# Playwright - Introduction to install

## Installing Python (Along with Python, 'pip' is also installed which helps to install other supporting packages while working with Python/Playwright)
Windows : https://www.python.org/downloads/windows/

MAC : https://www.python.org/downloads/macos/

## Installing Pytest:
pip install pytest

## Installing Playwright Pytest plugin:
pip install pytest-playwright

## Installing required browsers (Chromium,Firefox,...):
playwright install

# Playwright - How to run tests

## To run the dependencies mentioned in requirements.txt
pip install -r requirements.txt

## Run tests with html reports:
pytest testcases.py --html=reports.html