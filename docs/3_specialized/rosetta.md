# PyRosetta


## Installation

Install [PyRosetta](https://www.pyrosetta.org/downloads)

**Set-Up Optional Software Location (opt):**

    # File Name
    TEMP=PyRosetta-<version>.tar.bz2
    
    # Opt
    mkdir $OPT/pyrosetta
    mv $TEMP $OPT/pyrosetta
    cd $OPT/pyrosetta
    tar -jxf $TEMP

**Installation:**

    # Install
    cd $OPT/pyrosetta/setup && python setup.py install 

**Test:**

    python
    import pyrosetta; pyrosetta.init()



# RFDiffusion
https://github.com/RosettaCommons/RFdiffusion


antlr4-python3-runtime==4.9.3
asttokens==2.2.1
certifi==2022.12.7
charset-normalizer==3.1.0
click==8.1.3
colorama==0.4.6
configparser==5.3.0
cuda-python==12.1.0
Cython==0.29.34
decorator==5.1.0
dgl-cu111==0.6.1
DLLogger==1.0.0
docker-pycreds==0.4.0
e3nn==0.3.3
executing==1.2.0
gitdb==4.0.10
GitPython==3.1.31
hydra-core==1.3.2
icecream==2.1.3
idna==3.4
mpmath==1.3.0
networkx==3.1
numpy==1.24.3
omegaconf==2.3.0
opt-einsum==3.3.0
opt-einsum-fx==0.1.4
packaging==23.1
pathtools==0.1.2
Pillow==9.5.0
promise==2.3
protobuf==4.22.3
psutil==5.9.5
Pygments==2.15.1
pynvml==11.0.0
pyrosetta==2021.40+release.be58cfdca5c
pyrsistent==0.19.3
python-dateutil==2.8.2
PyYAML==6.0
requests==2.28.2
-e git+https://github.com/RosettaCommons/RFdiffusion.git@3139977cdb3233ab8c910d0b66a3d54c25528e5b#egg=rfdiffusion
scipy==1.10.1
se3-transformer==1.0.0
sentry-sdk==1.20.0
shortuuid==1.0.11
six==1.16.0
smmap==5.0.0
subprocess32==3.5.4
sympy==1.11.1
torch==1.9.1+cu111
torchaudio==0.9.1
torchvision==0.10.1+cu111
typing_extensions==4.5.0
urllib3==1.26.15
wandb==0.12.0
