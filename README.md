# Bart Flask
Flask server to return real-time bart departure
## Setup
Get BART API Key from http://api.bart.gov/api/register.aspx then enter that in token file.
## Installation
First, clone this repo.

Start new virtualenv, then install bart_api with
```
cd bart_api
git clone https://github.com/projectdelphai/bart_api
python setup.py install
# Make it into module
touch __init__.py
```

Then, run to install requirements for flask
```
pip install -r requirements.txt
```

