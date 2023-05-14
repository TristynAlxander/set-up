# PyEnv-VirtualEnv Environment Manager

While `pyenv` is effective for managing pure python environments it does not work with `conda`. 
While I am not partial to anaconda, it is a common dependency that I cannot always work around. 
As such, I must (unfortunately) recommend using `conda` instead. 

# Install Python via PyEnv.

Start by checking that `$PYENV_ROOT` is set correctly wherever you set-up your environment (e.g. look in `~/.environment`).

```
# Python Environment Variables
export PYENV_ROOT="$OPT/.pyenv_root"
export PATH="$PYENV_ROOT/bin:$PATH"
export PATH="$PYENV_ROOT/shims:$PATH"

# Add Auto Completion to Python Environment
if [ -d $PYENV_ROOT ]; then
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
fi
```

Assuming you have your bash environment set up correctly, I roughly follow [these instructions](https://realpython.com/intro-to-pyenv/#installing-pyenv).

       sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
       libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
       libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev openssl libssl-dev 
       
       # Note: The Above was modified due to an error.
       # python-openssl -> openssl libssl-dev 

       curl https://pyenv.run | bash

Re-Strart your Computer.

       # Compile and Install Python, this may take a while. Use your version.
       pyenv install #3.9.7
       pyenv global 3.9.7

# Uninstall PyEnv

rm -rf $PYENV_ROOT


# Creating a PyEnv Environment.



**Creating Environment:** `pyenv virtualenv <python_version> <environment_name>` and `pyenv local environment_name` to set in a location. e.g. `pyenv virtualenv 3.9.7 temp`

**Common Installs:**

    pip install pytest
    pip install numpy
    pip install pandas
    pip install matplotlib

**List Installed:**         `pyenv versions`
**Delete Environment:**     `cd $PYENV_ROOT/versions` and using `rm -rf` (for virtualenv remove both link and link location).
**Activate Environment:**   `pyenv activate my_python_env`
**Export Environment:**     `python --version` and `pip freeze > requirements.txt`
**Import Environment:**     `pyenv install XXXXXX` `pip install -r requirements.txt`


pytest
coverage