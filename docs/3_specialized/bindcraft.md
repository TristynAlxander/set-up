git clone https://github.com/martinpacesa/BindCraft
cd BindCraft
bash install_bindcraft.sh --cuda '12.4' --pkg_manager 'conda'

conda rename -n BindCraft  protein_bindcraft 
conda activate protein_bindcraft
pip install --upgrade "jax[cuda12_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

#conda deactivate; conda remove --name BindCraft --all
#conda deactivate; conda remove --name protein_bindcraft --all