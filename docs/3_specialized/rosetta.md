# PyRosetta

## Installation
  
  Install [PyRosetta](https://www.pyrosetta.org/downloads)
    See RosettaCommons Conda Channel
  **Set-Up Optional Software Location (opt):**

      # File Name
      TEMP=PyRosetta-<version>.tar.bz2
      
      # Opt
      mkdir $OPT/pyrosetta
      mv $TEMP $OPT/pyrosetta
      cd $OPT/pyrosetta
      tar -jxf $TEMP

  **Installation:**
      conda create --name protein_pyrosetta python=3.9.13
      conda activate protein_pyrosetta
      pip install pyrosetta-installer 
      python -c 'import pyrosetta_installer; pyrosetta_installer.install_pyrosetta()'


      # Install
      cd $OPT/pyrosetta/setup && python setup.py install 

  **Test:**
      python
      import pyrosetta; pyrosetta.init()

