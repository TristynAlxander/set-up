# Python Environment Manager

Just Use Conda - there is a way to use pyenv and conda [together](https://stackoverflow.com/a/58045893).
But! The important difference between pyenv and conda is that conda works with multiple languages.
This is important for dependencies, so it's best to just use conda.

# PyEnv-VirtualEnv Environment Manager
  
  Install PyEnv:
    Seriously, don't. Use conda, I know it's corporate, but it's under freeware and it's functionally better.
    I roughly follow [these instructions](https://realpython.com/intro-to-pyenv/#installing-pyenv).
    
    1: Start by checking that `$PYENV_ROOT` is set correctly wherever you set-up your environment (e.g. look in `~/.environment`).
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
    2: Install Prerequisites 
      ```
      sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev openssl libssl-dev
      # Note: The Above was modified due to an error.
      # python-openssl -> openssl libssl-dev 

      curl https://pyenv.run | bash
      ```
      Re-Strart Computer.
    3: Set Defaults
      ```
      pyenv install #3.9.7
      pyenv global 3.9.7
      ```
  Uninstall PyEnv:
    ```
    rm -rf $PYENV_ROOT
    ```
    Also remove the above from environment file
  Manage PyEnv Environment:
    **Install Python:**         `pyenv install -v 3.7.2`
    **Creating Environment:**   `pyenv virtualenv <python_version> <environment_name>` and `pyenv local environment_name` to set in a location. e.g. `pyenv virtualenv 3.9.7 temp`
    **Common Installs:**
      ```
      pip install pytest
      pip install numpy
      pip install pandas
      pip install matplotlib
      ```
    **List Installed:**         `pyenv versions`
    **Delete Environment:**     `cd $PYENV_ROOT/versions` and using `rm -rf` (for virtualenv remove both link and link location).
    **Activate Environment:**   `pyenv activate my_python_env`
    **Export Environment:**     `python --version` and `pip freeze > requirements.txt`
    **Import Environment:**     `pyenv install XXXXXX` `pip install -r requirements.txt`

# Conda Environment Manager
  
  Install Conda:
    I roughly follow [install instructions](https://docs.anaconda.com/free/anaconda/install/linux/).
    Download [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 
    ```
    bash ./miniconda.sh -b -p $OPT/.miniconda
    ```
    Set Defaults:
      ```
      source $OPT/.miniconda/bin/activate
      conda init
      conda config --set auto_activate_base false
      ```
  Uninstall Conda
    ```
    rm -rf $OPT/.miniconda
    ```
  
  Fix Conda:
    conda update conda
    conda config --remove channels conda-forge
    conda config --add channels conda-forge
  
  Manage Conda Environment
    **Creating Environment:**   `conda env create -f env.yml` or `conda create --name new-env python=3.13.1`
    **Common Installs:**
      ```
      conda install pip
      ```
    **List Installed:**         `conda env list`
    **Delete Environment:**     `conda remove --name env --all`
    **Activate Environment:**   `conda activate new-env`
    **Rename Environment:**     `conda rename -n old_name new_name`