<a href="https://cognite.com/">
    <img src="https://github.com/cognitedata/cognite-sdk-python/blob/master/cognite_logo.png" alt="Cognite logo" title="Cognite" align="right" height="80" />
</a>

ML Dev
===============

Data Science tools and algorithms developed at Cognite.

## Setup
#### Get code from github
```bash
$ git clone git@github.com:cognitedata/ml-toolkit.git
```
#### Set Environment variables
Create a .env file in the root directory with the following variables
```bash
PYPI_USERNAME=cognitedeploy
PYPI_PASSWORD=<password-from-lastpass>
COGNITE_MLTEST_API_KEY=<your-mltest-api-key>
```
#### Activate virtual environment and install dependencies from Pipfile.lock
```bash
$ pipenv shell
$ pipenv sync --dev
```