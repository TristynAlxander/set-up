# Install Python via PyEnv.

Start by checking that `$PYENV_ROOT` is set correctly wherever you set-up your environment (e.g. look in `~/.environ`).
Assuming you have your bash environment set up correctly, I roughly follow [these instructions](https://realpython.com/intro-to-pyenv/#installing-pyenv).

       sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
       libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
       libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

       curl https://pyenv.run | bash

Re-Strart your Computer.

       # Compile and Install Python, this may take a while. Use your version.
       pyenv install #3.9.7
       pyenv global 3.9.7

# Creating An Environment

**Creating Environment:** `pyenv virtualenv <python_version> <environment_name>` and `pyenv local environment_name` to set in a location.
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

## Standard Environments

git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
pyenv install 3.10.6
pyenv virtualenv 3.10.6 stable_diffusion
pyenv local stable_diffusion
...

maybe 
bash <(wget -qO- https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh)
https://github.com/AUTOMATIC1111/stable-diffusion-webui
https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies
https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPUs



# Python Testing

pytest
coverage

Arrange, Act, Assert. Phases of a test


