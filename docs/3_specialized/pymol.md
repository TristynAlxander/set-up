# PyMol

Create Environment

    pyenv virtualenv 3.9.7 protein_env
    pyenv activate protein_env
    pyenv local protein_env

Instructions: [Pymol](https://github.com/schrodinger/pymol-open-source/blob/master/INSTALL) ^^[1](https://pymolwiki.org/index.php/Linux_Install)
    
    apt install git build-essential libglew-dev libpng-dev libfreetype6-dev libxml2-dev libmsgpack-dev libglm-dev libnetcdf-dev
    pyenv activate protein_env
    pip install PyQt5
    if [ ! -d $STORE/opt ]; then mkdir $STORE/opt; fi
    cd $STORE/opt
    git clone https://github.com/schrodinger/pymol-open-source.git
    git clone https://github.com/rcsb/mmtf-cpp.git
    mv mmtf-cpp/include/mmtf* pymol-open-source/include/
    cd pymol-open-source
    prefix=$STORE/opt/pymol
    python setup.py build install --home=$prefix
    
    # Note there is an alias that matches up with all this
    rm -r $STORE/opt/mmtf-cpp/ $STORE/opt/pymol-open-source/
    
    
**Hook for Environment:**

Unfortunately, `pyenv` doesn't have hooks for activate/deactivate, so we can't hook in our environment variables.
If `pyenv` gets hooks for activate/deactivate later we'll be doing something like this:

    mkdir $PYENV_ROOT/pyenv.d/activate
    touch $PYENV_ROOT/pyenv.d/activate/pymol
    echo "after_virtualenv 'if [ \$VIRTUALENV_NAME == "protein_env" ]; then export PATH=\$STORE/opt/pymol/bin:\$PATH; fi'" >> $PYENV_ROOT/pyenv.d/activate/pymol

**Instead:** Just use an alias in .alias

    alias pymol="pyenv activate protein_env; export PATH=$STORE/opt/pymol/bin:$PATH; pymol"

