conda create --name protein_boltz1 python=3.9.7
conda activate protein_boltz1
conda install cmake
export CMAKE_PREFIX_PATH=/opt/.miniconda/envs/protein_boltz1/
conda install scipy==1.13.1
pip install boltz -U

#conda deactivate; conda remove --name protein_boltz1 --all

git clone https://github.com/jwohlwend/boltz.git
cd boltz; pip install -e .