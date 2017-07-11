# Bart Flask
Flask server to return real-time bart departure
## Setup
Get BART API Key from http://api.bart.gov/api/register.aspx then enter that in token file.
## Installation
First, clone this repo.

```
sudo apt-get install python-lxml
```
Start new virtualenv, then install bart_api and nextbus with
```
git clone https://github.com/projectdelphai/bart_api
cd bart_api
python setup.py install
# Make it into module
touch __init__.py
```

```
# Need this guy's fork version
git clone git@github.com:thewellington00/python-nextbus.git
cd python_nextbus
python setup.py install
# Make it into module
touch __init__.py
```

Then, run to install requirements for flask
```
pip install -r requirements.txt
```

