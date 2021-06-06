Conda
Check if Anaconda is added to the windows PATH
```bash
conda --version
```

as with python:
```bash
python --version
```


Python for Financial Analysis and Algorithmic Trading
[Home](http:\\localhost:8888\?token=bb00306226d966bc981a6f9f4f33a41dafb0a664e924a401)

Creating an environment from an `environment.yml` file
Use the terminal or an Anaconda Prompt for the following steps:

1. Create the environment from the environment.yml file:
   ```bash
   conda env create -f environment.yml
   ```
   The first line of the `yml` file sets the new environment's name

2. Activate the new environment: `conda activate myenv`
3. Verify that the new environment was installed correctly:
   ```bash
   conda env list   
   ```
   You can also use `conda info --envs`.

Activate virtual env
```
conda activate pyfinance
```
Deactivate an active environment
```
conda deactivate
```

Start Jupyter Notebook:
```
jupyter notebook
```

Stop Jupyter Notebook
```
[CTRL] + [C]
```
---
pip3 install virtualenv

python3 -m virtualenv .\local_env
Using base prefix '\Library\Frameworks\Python.framework\Verions\3.8'
New python executable in .\local_env\bin\python3
Also creating executable in .\local_env\bin\python
Installing setuptools, pip...done.

cd local_env\bin\

. activate

(local_env)\ pip list