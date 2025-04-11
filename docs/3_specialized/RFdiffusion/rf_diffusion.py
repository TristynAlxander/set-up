# Header
if(True):
  import sys, os, copy, shutil, subprocess

# This is quite possibly the least effective method of installing RF-Diffusion.

######################################################################
# WARNING: I Never ended up using this, but it would download a lot. #
######################################################################

rf_diffusion_location ="$DOWNLOADS/RFdiffusion"

# PyTorch Installations
if(True):
  # Tensor Stuff? 
  # https://pytorch.org/get-started/previous-versions/
  pytorch_installation_commands = """
    pip install torch==2.0.0+cu117 torchvision==0.15.1+cu116 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu117
    pip install torch==2.0.0+cu118 torchvision==0.15.1+cu117 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
    pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116
    pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
    pip install torch==1.13.0+cu116 torchvision==0.14.0+cu116 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cu116
    pip install torch==1.13.0+cu117 torchvision==0.14.0+cu117 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cu117
    pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
    pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
    pip install torch==1.12.1+cu102 torchvision==0.13.1+cu102 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu102
    pip install torch==1.12.0+cu116 torchvision==0.13.0+cu116 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu116
    pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113
    pip install torch==1.12.0+cu102 torchvision==0.13.0+cu102 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu102
    pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
    pip install torch==1.11.0+cu102 torchvision==0.12.0+cu102 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu102
    pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu111/torch_stable.html
    pip install torch==1.10.1+cu102 torchvision==0.11.2+cu102 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu102/torch_stable.html
    pip install torch==1.10.0+cu111 torchvision==0.11.0+cu111 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.10.0+cu102 torchvision==0.11.0+cu102 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.9.1+cu102 torchvision==0.10.1+cu102 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
    pip3 install torch==1.8.2 torchvision==0.9.2 torchaudio==0.8.2 --extra-index-url https://download.pytorch.org/whl/lts/1.8/cu102
    pip3 install torch==1.8.2 torchvision==0.9.2 torchaudio==0.8.2 --extra-index-url https://download.pytorch.org/whl/lts/1.8/cu111
    pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.8.1+cu101 torchvision==0.9.1+cu101 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=10.2 -c pytorch
    conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge
    pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0
    pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2
    pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.7.1+cu92 torchvision==0.8.2+cu92 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.7.0+cu110 torchvision==0.8.0+cu110 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0
    pip install torch==1.7.0+cu101 torchvision==0.8.0+cu101 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.7.0+cu92 torchvision==0.8.0+cu92 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.6.0 torchvision==0.7.0
    pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.6.0+cu92 torchvision==0.7.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.5.1 torchvision==0.6.1
    pip install torch==1.5.1+cu101 torchvision==0.6.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.5.1+cu92 torchvision==0.6.1+cu92 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.5.0 torchvision==0.6.0
    pip install torch==1.5.0+cu101 torchvision==0.6.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.5.0+cu92 torchvision==0.6.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.4.0 torchvision==0.5.0
    pip install torch==1.4.0+cu92 torchvision==0.5.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
    pip install torch==1.2.0 torchvision==0.4.0
    pip install torch==1.2.0+cu92 torchvision==0.4.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
    """
  pytorch_installation_commands = pytorch_installation_commands.split("\n")
  pytorch_installation_commands = [_.strip() for _ in pytorch_installation_commands if _.strip()!='']

# Deep Graphics Library Installations
if(True):
  deep_graphics_library_commands = [
    "pip install  dgl -f https://data.dgl.ai/wheels/cu102/repo.html; pip install  dglgo -f https://data.dgl.ai/wheels-test/repo.html",
    "pip install  dgl -f https://data.dgl.ai/wheels/cu113/repo.html; pip install  dglgo -f https://data.dgl.ai/wheels-test/repo.html",
    "pip install  dgl -f https://data.dgl.ai/wheels/cu116/repo.html; pip install  dglgo -f https://data.dgl.ai/wheels-test/repo.html",
    "pip install  dgl -f https://data.dgl.ai/wheels/cu117/repo.html; pip install  dglgo -f https://data.dgl.ai/wheels-test/repo.html",
    "pip install  dgl -f https://data.dgl.ai/wheels/cu118/repo.html; pip install  dglgo -f https://data.dgl.ai/wheels-test/repo.html",
     ]

i=1
for pytorch_installation_command in pytorch_installation_commands:
  for deep_graphics_library_command in deep_graphics_library_commands:
    # Make File
    command_file = open(f"installer_{i}.sh", "w+")
    
    # Export Location
    print( f"export RFDIFFUSION={rf_diffusion_location}" , file=command_file )
    
    # Make Virtual Environment
    print( f"pyenv virtualenv 3.9.7 rf_diff{i}; pyenv activate rf_diff{i}" , file=command_file )
    
    #  Install Conda Pip
    print( "pip install hydra-core pyrsistent icecream" , file=command_file )
    
    # Variant Commands
    print( pytorch_installation_command  , file=command_file )
    print( deep_graphics_library_command , file=command_file )
    
    # Pip Installations
    print( "pip install e3nn==0.3.3"    , file=command_file )
    print( "pip install wandb==0.12.0"  , file=command_file )
    print( "pip install pynvml==11.0.0" , file=command_file )
    print( "pip install git+https://github.com/NVIDIA/dllogger#egg=dllogger" , file=command_file )
    print( "pip install decorator==5.1.0" , file=command_file )
    
    # Setup
    print( "cd $RFDIFFUSION/env/SE3Transformer/" , file=command_file )
    print( "python setup.py install" , file=command_file )
    print( "cd $RFDIFFUSION" , file=command_file )
    print( "pip install -e ." , file=command_file )
    
    # Try to Run the Program
    print( "./scripts/run_inference.py 'contigmap.contigs=[100-100]' inference.output_prefix=test_outputs/test inference.num_designs=1" , file=command_file )
    
    command_file.close()
    
    i=i+1
    



