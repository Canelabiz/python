# Python, virtual environments, VS Code, and Git

## Table of contents

* [python](#python)
* [pip](#pip)
* [venv](#venv)
* [pip and virtualenv](<#pip and virtualenv>)
* [Visual Studio Code](<#Visual Studio Code>)
* [Git](#Git)
* [Docker](#Docker)
* [Footnotes & Linkies](<#Footnotes & Linkies>)

---

## [python](https://www.python.org/)

Python location  
`where python`

python version  
`python --version` or `python -V`

python run module (pip):  
`python -m pip`

---

## [pip](https://pip.pypa.io/)

### pip version

`pip --version` or `pip -V`

### pip location

`where pip`

### Upgrade pip

`python -m pip install -U pip` (short for)
`python -m pip install --upgrade pip`

### [pip list](https://pip.pypa.io/en/stable/cli/pip_list/)

`pip list`

### [pip install](https://pip.pypa.io/en/stable/cli/pip_install/)

best practice: `python -m pip install requests`
`pip install requests`

### pip upgrade

`pip install Django -U` (short for) `pip install Django --upgrade`

alternatively `python -m --upgrade Django`

### [pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)

Create a requirements.txt file containing the names of your dependencies. You can use the pip command freeze for this task:
`pip freeze > requirements.txt`

With pip, you can list all installed packages and their versions with `pip freeze`
In most linux systems, you can pipe this to grep (or findstr on Windows) to find the row for the particular package you're interested in:

Linux:

```bash
$ pip freeze | grep lxml
lxml==2.3
```

Windows:

```cmd
c:\> pip freeze | findstr lxml
lxml==2.3
```

### [pip uninstall](https://pip.pypa.io/en/stable/cli/pip_uninstall/)

`pip uninstall Django`

batch uninstall:
`pip uninstall -r uninstall.txt` or `python -m pip uninstall -r uninstall.txt -y`

---

## [venv](https://docs.python.org/3/library/venv.html)

Create a virtual environment called `[appenv]` in the current folder  
`python -m venv appenv`

This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named venv.

Activate the virtual environment  
(Win)  
`venv\Scripts\activate`

(Linux)  
`source venv\bin\activate`

Install packages with pip  
`pip install requests`

Deactivate virtual environment  
`deactivate`

To delete a virtual environment, just delete its folder.  
(In this case, it would be `rm -rf venv`.)

In order to keep your environment consistent, it’s a good idea to “freeze” the current state of the environment packages.  
`pip freeze > requirements.txt`

To re-create the enviroment with the same packages and versions elsewhere  
`pip install -r requirements.txt`

Lastly, remember to exclude the virtual environment folder from source control by adding it to the ignore list (see Version Control Ignores).  
.ignore file:  
`\appenv`

---

## pip and virtualenv

pip3 always operates on the Python3 environment only, as pip2 does with Python2. pip operates on whichever environment is appropriate to the context. For example if you are in a Python3 venv, pip will operate on the Python3 environment.

Pip works as a module with -m, and so does venv for Python 3, so if you have Python 3.5 installed and stand in a project directory, you could e.g. do (assuming linux or MacOS):

`python3.5 -m venv venv35`

`source venv35/bin/activate`

`(venv35) [Prompt] pip install <whatever>`

That will install `<whatever>` in the Python3.5 virtual environment venv35 in your current directory.  
Another example:

```cmd
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

---

## [Visual Studio Code](https://code.visualstudio.com/)

placeholder

---

## [Git](https://git-scm.com/)

### Local Repository

### Remote Repository

---

## [Docker](https://www.docker.com)

placeholder

---

## Footnotes & Linkies

* [Python.org](https://www.python.org/)
* [PyPA - The Python Packaging Authority](https://www.pypa.io/)
* [pip latest version](https://pip.pypa.io/en/latest/installing.html)
* [PyPI - the Python Package Index](https://pypi.python.org/pypi)
* [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)
* [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)
* [What is difference between pip and pip3? - Quora](https://www.quora.com/What-is-difference-between-pip-and-pip3)
* [Better organization of your projects with python imports](https://pythonhowtoprogram.com/better-organization-of-your-projects-with-python-imports/)
* [Creating the Perfect Python Dockerfile](https://luis-sena.medium.com/creating-the-perfect-python-dockerfile-51bdec41f1c8)
* [GitHub - Production tools for Data Science](https://github.com/thuijskens/production-tools)
* [Design Patterns in Python- The Catalog of Python Examples](https://refactoring.guru/design-patterns/python)
* [Python SpeedSheet](https://speedsheet.io/s/python)
* [Objects, Memory, and Mutation in Python](https://medium.com/@birnbera/objects-memory-and-mutation-in-python-810bf090b63c)
