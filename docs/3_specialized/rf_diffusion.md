# RF Diffusion


pyenv virtualenv 3.9.7 rf_diff1
pyenv activate rf_diff1
pyenv local rf_diff

pip install hydra-core
pip install pyrsistent
pip install icecream

# SE3 Transformers
pip install e3nn==0.3.3
pip install wandb==0.12.0
pip install pynvml==11.0.0
pip install git+https://github.com/NVIDIA/dllogger#egg=dllogger
pip install decorator==5.1.0

python env/SE3Transformer/setup.py install

# Tensor Stuff? 
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install dgl==1.0.2+cu116 -f https://data.dgl.ai/wheels/cu116/repo.html

pip install -e .





pip uninstall torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html


#pip -q install jedi omegaconf hydra-core icecream


