# ProteinMPNN


env1/bin/python -m pip freeze > requirements.txt
env2/bin/python -m pip install -r requirements.txt 
fails

I've made a python file that generates a bunch of poor efficiency attempts at installation, but try the following first:

    export PROTEINMPNN=$DOWNLOADS/large_language_models/ProteinMPNN
    
    pyenv virtualenv 3.9.7 ProMPNN
    pyenv activate ProMPNN
    
    
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
    
    torch==2.0.1
    nvidia-cublas-cu11==11.10.3.66
    nvidia-cuda-cupti-cu11==11.7.101
    nvidia-cuda-nvrtc-cu11==11.7.99
    nvidia-cuda-runtime-cu11==11.7.99
    nvidia-cudnn-cu11==8.5.0.96
    nvidia-cufft-cu11==10.9.0.58
    nvidia-curand-cu11==10.2.10.91
    nvidia-cusolver-cu11==11.4.0.1
    nvidia-cusparse-cu11==11.7.4.91
    nvidia-nccl-cu11==2.14.3
    nvidia-nvtx-cu11==11.7.91
    
    