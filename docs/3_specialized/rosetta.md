# PyRosetta

Install [PyRosetta](https://www.pyrosetta.org/downloads)

    cd $STORE/opt/pyrosetta
    mkdir $STORE/opt/pyrosetta
    
    # Activate Python Environment
    pyenv virtualenv 3.9.7 rosetta
    pyenv activate rosetta
    
    # UnTar
    tar -jxf PyRosetta-<version>.tar.bz2
    
    # Install
    cd setup && python setup.py install 
    
    # Test
    python
    import pyrosetta; pyrosetta.init()

#