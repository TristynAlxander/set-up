# PyMol

Create Environment (pyenv, python 3.6+)
  pyenv install 3.9.7
  pyenv virtualenv 3.9.7 pymol
  pyenv activate pymol
  pyenv local pymol

Create Environment (conda)
  conda create --name protein_pymol python=3.13.1
  conda activate protein_pymol

## Installation

Instructions: [Pymol](https://github.com/schrodinger/pymol-open-source/blob/master/INSTALL) ^^[1](https://pymolwiki.org/index.php/Linux_Install)

**Set-Up Optional Software Location (opt):**

    if [ ! -d $OPT ]; then mkdir $OPT; fi; cd $OPT
    git clone https://github.com/schrodinger/pymol-open-source.git
    git clone https://github.com/rcsb/mmtf-cpp.git
    mv mmtf-cpp/include/mmtf* pymol-open-source/include/
    mv pymol-open-source pymol; rm -rf mmtf-cpp/

Technically one doesn't have to leave the source files on the computer. 
If one installs pymol to a home location (see below) outside of the download location, then the source files can be removed after installation. 
I do not recommend this. It'd require downloading pymol each time it's installed in a different environment.

**Installation:**

Activate your Environment.

    # Prerequisites
    apt install git build-essential libglew-dev libpng-dev libfreetype6-dev libxml2-dev libmsgpack-dev libglm-dev libnetcdf-dev
    pip install PyQt5
    pip install numpy
    pip install setuptools
    pip install cmake
    
    # Install Program
    cd $OPT/pymol
    python setup.py build install --home=$OPT/temp
    
    # Move to Library
    mv $OPT/temp/lib/python/* $(( python -c 'import site; print(site.getsitepackages()[0])' ) >&1 )
    
    # Add to Bin
    if [ ! -d ~/bin ]; then mkdir ~/bin; fi;
    echo '#!/bin/sh' > ~/bin/pymol
    echo exec \"/opt/.miniconda/envs/protein_pymol/bin/python\" \"$(( python -c "import site; print(site.getsitepackages()[0])" ) >&1)/pymol/__init__.py\" \"\$@\" >> ~/bin/pymol
    chmod 777 ~/bin/pymol
    
    # Clean-Up
    rm -r $OPT/temp
    rm -r $OPT/pymol/build

**Plugins:**
conda install conda-forge::cctbx-base

Best to use GUI for this

https://github.com/Pymol-Scripts/Pymol-script-repo/blob/master/plugins/SuperSymPlugin.py


**Old Solutions:**

    # Move or Link Library to Python Library
    
    # Solution 1: Link via Python Path Variable
    #export PYTHONPATH="/media/tristin/DATA/opt/temp/lib/python:$PYTHONPATH"
    
    # Solution 2: Link via Python Path file
    # echo "$OPT/temp/lib/python" >> $PYENV_ROOT/versions/pymol/lib/python3.9/site-packages/pymol.pth
    
    # Solution 3: AutoLink via Python Path file
    # echo "$OPT/temp/lib/python" >> $(( python -c 'import site; print(site.getsitepackages()[0])' ) >&1 )/pymol.pth
    