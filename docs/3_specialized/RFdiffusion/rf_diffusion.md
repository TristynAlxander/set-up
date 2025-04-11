# RF Diffusion

I've made a python file that generates a bunch of poor efficiency attempts at installation, but try the following first:
I think, generally, conda is more appropriate since it helps manage the C program files in graphics libraries.

# Conda: Not Working 
    # This works
    # Not Probably want to rename SE3nv to RFDiffusion or something
    conda env create -f env/SE3nv.yml
    conda activate SE3nv
    cd env/SE3Transformer
    pip install --no-cache-dir -r requirements.txt
    python setup.py install
    cd ../.. # change into the root directory of the repository
    pip install -e . # install the rfdiffusion module from the root of the repository
    conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia
    pip install --force-reinstall numpy==1.25.0

    # Just removed the following see if it still works
      libnvidia-compute-525 libnvidia-compute-525:i386 libnvidia-decode-525 libnvidia-decode-525:i386 libnvidia-egl-wayland1
      libnvidia-encode-525 libnvidia-encode-525:i386 libnvidia-extra-525 libnvidia-fbc1-525 libnvidia-fbc1-525:i386 libnvidia-gl-525
      libnvidia-gl-525:i386 libwmf0.2-7 libwpe-1.0-1 libwpebackend-fdo-1.0-1 linux-headers-5.15.0-101 linux-headers-5.15.0-101-generic
      linux-headers-5.15.0-105 linux-headers-5.15.0-105-generic linux-headers-5.15.0-107 linux-headers-5.15.0-107-generic
      linux-headers-5.15.0-113 linux-headers-5.15.0-113-generic linux-headers-5.15.0-117 linux-headers-5.15.0-117-generic
      linux-headers-5.15.0-79 linux-headers-5.15.0-79-generic linux-headers-5.15.0-82 linux-headers-5.15.0-82-generic
      linux-headers-5.15.0-83 linux-headers-5.15.0-83-generic linux-headers-5.15.0-86 linux-headers-5.15.0-86-generic
      linux-headers-5.15.0-87 linux-headers-5.15.0-87-generic linux-headers-5.15.0-88 linux-headers-5.15.0-88-generic
      linux-headers-5.15.0-91 linux-headers-5.15.0-91-generic linux-headers-5.15.0-92 linux-headers-5.15.0-92-generic
      linux-headers-5.15.0-94 linux-headers-5.15.0-94-generic linux-headers-5.15.0-97 linux-headers-5.15.0-97-generic
      linux-headers-6.2.0-26-generic linux-headers-6.2.0-31-generic linux-headers-6.2.0-32-generic linux-headers-6.2.0-34-generic
      linux-headers-6.2.0-35-generic linux-headers-6.2.0-36-generic linux-headers-6.2.0-37-generic linux-headers-6.5.0-15-generic
      linux-headers-6.5.0-17-generic linux-headers-6.5.0-18-generic linux-headers-6.5.0-21-generic linux-headers-6.5.0-26-generic
      linux-headers-6.5.0-28-generic linux-headers-6.5.0-35-generic linux-headers-6.5.0-41-generic linux-hwe-6.2-headers-6.2.0-26
      linux-hwe-6.2-headers-6.2.0-31 linux-hwe-6.2-headers-6.2.0-32 linux-hwe-6.2-headers-6.2.0-34 linux-hwe-6.2-headers-6.2.0-35
      linux-hwe-6.2-headers-6.2.0-36 linux-hwe-6.2-headers-6.2.0-37 linux-hwe-6.5-headers-6.5.0-15 linux-hwe-6.5-headers-6.5.0-17
      linux-hwe-6.5-headers-6.5.0-18 linux-hwe-6.5-headers-6.5.0-21 linux-hwe-6.5-headers-6.5.0-26 linux-hwe-6.5-headers-6.5.0-28
      linux-hwe-6.5-headers-6.5.0-35 linux-hwe-6.5-headers-6.5.0-41 linux-image-5.15.0-101-generic linux-image-5.15.0-105-generic
      linux-image-5.15.0-107-generic linux-image-5.15.0-113-generic linux-image-5.15.0-117-generic linux-image-5.15.0-79-generic
      linux-image-5.15.0-82-generic linux-image-5.15.0-83-generic linux-image-5.15.0-86-generic linux-image-5.15.0-87-generic
      linux-image-5.15.0-88-generic linux-image-5.15.0-91-generic linux-image-5.15.0-92-generic linux-image-5.15.0-94-generic
      linux-image-5.15.0-97-generic linux-image-5.19.0-50-generic linux-image-6.2.0-26-generic linux-image-6.2.0-31-generic
      linux-image-6.2.0-32-generic linux-image-6.2.0-34-generic linux-image-6.2.0-35-generic linux-image-6.2.0-36-generic
      linux-image-6.2.0-37-generic linux-image-6.2.0-39-generic linux-image-6.5.0-15-generic linux-image-6.5.0-17-generic
      linux-image-6.5.0-18-generic linux-image-6.5.0-21-generic linux-image-6.5.0-26-generic linux-image-6.5.0-28-generic
      linux-image-6.5.0-35-generic linux-image-6.5.0-41-generic linux-modules-5.15.0-101-generic linux-modules-5.15.0-105-generic
      linux-modules-5.15.0-107-generic linux-modules-5.15.0-113-generic linux-modules-5.15.0-117-generic
      linux-modules-5.15.0-79-generic linux-modules-5.15.0-82-generic linux-modules-5.15.0-83-generic linux-modules-5.15.0-86-generic
      linux-modules-5.15.0-87-generic linux-modules-5.15.0-88-generic linux-modules-5.15.0-91-generic linux-modules-5.15.0-92-generic
      linux-modules-5.15.0-94-generic linux-modules-5.15.0-97-generic linux-modules-5.19.0-50-generic linux-modules-6.2.0-26-generic
      linux-modules-6.2.0-31-generic linux-modules-6.2.0-32-generic linux-modules-6.2.0-34-generic linux-modules-6.2.0-35-generic
      linux-modules-6.2.0-36-generic linux-modules-6.2.0-37-generic linux-modules-6.2.0-39-generic linux-modules-6.5.0-15-generic
      linux-modules-6.5.0-17-generic linux-modules-6.5.0-18-generic linux-modules-6.5.0-21-generic linux-modules-6.5.0-26-generic
      linux-modules-6.5.0-28-generic linux-modules-6.5.0-35-generic linux-modules-6.5.0-41-generic
      linux-modules-extra-5.15.0-101-generic linux-modules-extra-5.15.0-105-generic linux-modules-extra-5.15.0-107-generic
      linux-modules-extra-5.15.0-113-generic linux-modules-extra-5.15.0-117-generic linux-modules-extra-5.15.0-79-generic
      linux-modules-extra-5.15.0-82-generic linux-modules-extra-5.15.0-83-generic linux-modules-extra-5.15.0-86-generic
      linux-modules-extra-5.15.0-87-generic linux-modules-extra-5.15.0-88-generic linux-modules-extra-5.15.0-91-generic
      linux-modules-extra-5.15.0-92-generic linux-modules-extra-5.15.0-94-generic linux-modules-extra-5.15.0-97-generic
      linux-modules-extra-5.19.0-50-generic linux-modules-extra-6.2.0-26-generic linux-modules-extra-6.2.0-31-generic
      linux-modules-extra-6.2.0-32-generic linux-modules-extra-6.2.0-34-generic linux-modules-extra-6.2.0-35-generic
      linux-modules-extra-6.2.0-36-generic linux-modules-extra-6.2.0-37-generic linux-modules-extra-6.2.0-39-generic
      linux-modules-extra-6.5.0-15-generic linux-modules-extra-6.5.0-17-generic linux-modules-extra-6.5.0-18-generic
      linux-modules-extra-6.5.0-21-generic linux-modules-extra-6.5.0-26-generic linux-modules-extra-6.5.0-28-generic
      linux-modules-extra-6.5.0-35-generic linux-modules-extra-6.5.0-41-generic linux-objects-nvidia-535-6.2.0-26-generic
#

  
# Try to Run the Program

## Make Protein
./scripts/run_inference.py 'contigmap.contigs=[100-100]' inference.output_prefix=test_outputs/test inference.num_designs=1


