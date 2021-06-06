# Python

* [Python.org](https://www.python.org/)

`$ python --version`

---

## pip

* [PyPA - The Python Packaging Authority](https://www.pypa.io/)
* [pip latest version](https://pip.pypa.io/en/latest/installing.html)
* [PyPI - the Python Package Index](https://pypi.python.org/pypi)

#### pip version

`$ pip --version` or `$ pip -V`

####  pip location

`$ where pip`

#### Upgrade pip

`$ python -m pip install -U pip` (short for)
`$ python -m pip install --upgrade pip`

#### List Packages

`$ pip list`

#### Upgrade package

`$ pip install Django -U` (short for)
`$ pip install Django --upgrade`

---

## virtualenv

install
`$ pip install virtualenv`
verify
`$ virtualenv --version`
usage

```bash
cd project_folder
virtalenv venv
```

This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named venv.

Activate the virtual environment
`C:\Users\SomeUser\project_folder> venv\Scripts activate`

or
`cd local_env\bin\`
followed by
`activate`

Install packages with pip:
`$ pip install requests`

Deactivate virtual environment
`$ deactivate`

To delete a virtual environment, just delete its folder. (In this case, it would be rm -rf venv.)

In order to keep your environment consistent, it’s a good idea to “freeze” the current state of the environment packages. To do this, run:
`$ pip freeze > requirements.txt`

To re-create the enviroment with the same packages and versions elsewhere:
`$ pip install -r requirements.txt`

Lastly, remember to exclude the virtual environment folder from source control by adding it to the ignore list (see Version Control Ignores).

---

## pip and virtualenv

pip3 always operates on the Python3 environment only, as pip2 does with Python2. pip operates on whichever environment is appropriate to the context. For example if you are in a Python3 venv, pip will operate on the Python3 environment.

Pip works as a module with -m, and so does venv for Python 3, so if you have Python 3.5 installed and stand in a project directory, you could e.g. do (assuming linux or MacOS):

`$ python3.5 -m venv venv35`

`$ source venv35/bin/activate`

`(venv35) $ pip install <whatever>`

That will install `<whatever>` in the Python3.5 virtual environment venv35 in your current directory.

another example:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

---
Links

* [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)
* [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)
* [What is difference between pip and pip3? - Quora](https://www.quora.com/What-is-difference-between-pip-and-pip3)
