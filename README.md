# Set-Up Linux
Instructions and files for my preferred linux set-up.

## Installation Linux

- Download your distribution of choice.
  - If possible, download with unofficial & proprietary firmware/drivers.
  - Pay attention to the architecture (probably `amd64/`)
  - Download as dvd
  - Recommended Distributions: [Devian](http://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/), [Mint Cinnamon](https://linuxmint.com/download.php), Ubuntu?
- Install your Distribution on a USB drive.
  - From Windows, use [rufus](https://rufus.ie/en/) to prepare a USB, use default settings.
- Check the Distribution Works on your Computer
  - Set your BIOS to boot from USB (This may require usb be plugged in.)
  - If possible, use the Live Image
  - On the live image, check Wifi, Graphics (watch a video), etc.
  - Some Distributions have a "Driver Manager" that will auto-detect drivers for you to install.
    - Note: You may need a USB wifi thing if your wifi driver is bad.
  - If a driver manager does not exist or does not solve the problem run `lspci` and search for the thing that failed
    - Search using that name in a search engine.
  - take notes while resolving hardware issues to repeat process on real installation.
  - Learn how to manipulate your Update/Back-Up/Snapshot settings.
    - Note: Computers with near little space may not want back-ups/snapshots.
  - Note: Do not continue if you cannot resolve the hardware issues.
- Install on Computer
  - Either Partition for Dual Boot or Wipe your computer.
    - Obviously you're gonna lose data if you're wiping your computer, so be careful.  
  - Install your distribution
  - re-resolve hardware issues.
  - Fix your Update/Back-Up/Snapshot settings


## Set-Up Bin

Do not attempt to keep bins organized. Bin in not a user area.
Users should keep all their files in a separate location.
Preferably a separate hard-drive.

- Append the following to `~/.bashrc` and `~/.profile`

      if [ -t 0 ] && [ -t 1 ]; then
        if ! [ $ENV_CHECK ]; then source ~/.environ; fi
        if ! [ $ALIAS_CHECK ]; then source ~/.alias; fi
      fi

  - From inside the repo's Directory `cp .environ ~/.environ`
  - From inside the repo's Directory `cp .alias ~/.alias`

- Set up auto mount for your storage hard drive. (If applicable, externals may load on start-up)

      sudo fdisk -l
      sudo blkid
      # Get UUID, not PARTUUID, from above

      # Make Mount point
      sudo mkdir /media/username/drivename

    - Use `atom /etc/fstab`
      - For Internal Hard Drives add `UUID=MY-UUID-HERE /media/username/drivename auto nosuid,nodev,nofail,x-gvfs-show 0 0`
      - For Internal (Samba) Networks 
        - Install `apt install cifs-utils` 
        - Get ip address `nmblookup -S WORKGROUP` 
        - Add to fstab `//192.168.0.??/backup/ /media/username/drivename cifs uid=0,credentials=/.creds 0 0`
    - Test if you did it right `sudo mount -a` - ???
    - You may have to restart here. Unclear it just started working.

- Clean up bash
  - open file `/etc/login.defs`  remove `:/usr/local/games:/usr/games`
  - open file `/etc/environment` remove `:/usr/games:/usr/local/games:/snap/bin`
  - `sudo rm -rf /usr/local/games/`

- Restart Computer for all these to be implemented.


## Install Python via PyEnv.

Start by checking that `$PYENV_ROOT` is set correctly wherever you set your environment (e.g. `~/.environ`).
Assuming you have your bash environment set up correctly, I roughly follow [these instructions](https://realpython.com/intro-to-pyenv/#installing-pyenv).

       sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
       libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
       libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

       curl https://pyenv.run | bash

Re-Strart your Computer.

       # Compile and Install Python, this may take a while. Use your version.
       pyenv install #3.9.7
       pyenv global 3.9.7

Note: Use `pyenv virtualenv <python_version> <environment_name>` to create new environments and `pyenv local environment_name` to set in a location.
Note: You probably want to `pip install pytest` first thing.

## Set-Up Git

- Set-Up Git
  - `git config --global user.email "you@email.com"`
  - `git config --global user.name "UserName"`

- Make and Link Repos Directory

      if [ ! -d $STORE/repos ]; then mkdir $STORE/repos; fi
      ln -s $STORE/repos ~/repos

- Downloading a Repository
  - Use in `$STORE/repos` use `git clone URL` with URL as:
    - `https://Username`:`Password`@`github.com/Username/myRepo.git`
    - `https://Username`:`Personal_Access_Token`@`github.com/Username/myRepo.git`
    - Note: Personal_Access_Token can be found in configs

- Creating a Respository
  - Create a Github Repo [link](https://docs.github.com/en/get-started/quickstart/create-a-repo)

## Install Common Tools

    sudo apt update && sudo apt upgrade -y
    sudo apt install git-all
    sudo apt install hardlink
    sudo apt install atom
    

## Set-Up Common Tools

- Atom Text Editor
  - Disable snippets in `language-python`
  - set default tab size in `language-python` (and global)
  - disable `whitespace`
  - `bracket-matcher` > uncheck Autocomplete Brackets
  - `apm install duplicate-line-or-selection`
  - `apm install highlight-selected`
  - Check if `markdown-preview` is already installed. if not `apm install markdown-preview`
  - append duplicate key to `~/.atom/keymap.cson`
  
        'atom-workspace atom-text-editor:not([mini])':
          'ctrl-d': 'duplicate-line-or-selection:duplicate'
          
  - bigger scrollbar append following to Edit > Stylesheet... > 
  
        .scrollbars-visible-always {
          ::-webkit-scrollbar {
            width: 12px;
            height: 12px;
            &-track {
                border: 0px;
                border-radius: 0px;
                background-color: #444 !important;
                }
            &-thumb {
                background-color: rgba(200,200,250,0.35) !important;
                border: 0px;
                border-radius: 9px;
                }
            }
          }

- Fix Firefox
  - Set default Browser to Google.
  - Note: FTP links can be open in the file manager, then the htmls in those directories can be open in firefox. I don't know why.
  - `about:config` > `widget.non-native-theme.scrollbar.size` > 24
  - `about:config` > `widget.non-native-theme.gtk.scrollbar.allow-buttons` > True

## Install Semi-Common Tools

    sudo apt install inkscape
    sudo apt install texlive-full
    sudo apt install pdf2svg
    
### Semi-Common Preferences
  
  inkscape > Edit > Preferences > Behaviour > Transforms > [deselect] "Scale stroke width" 
  - Not sure which of these controls scroll bars, but look at terminal scroll bar
  Linux Mint > `atom /usr/share/themes/Mint-X/gtk-2.0/gtkrc` > `GtkScrollbar::slider-width =`
  Linux Mint > `atom ~/.config/gtk-3.0/gtk.css` > append:

        .scrollbar {
        -GtkScrollbar-has-backward-stepper: true;
        -GtkScrollbar-has-forward-stepper: true;
        -GtkRange-slider-width: 15;
        -GtkRange-stepper-size: 8;
        }
        .scrollbar.vertical slider,scrollbar.vertical slider {min-width: 15px;}


## Install Uncommon Tools

Note: It may be wise to load all the crystallography environments at once, but I'm not sure yet.

- `if [ ! -d $STORE/opt ]; then mkdir $STORE/opt; fi`
- Install PyMol: `sudo apt-get install pymol`
- Install Phenix from download.

      tar xvf phenix-installer-<version>-<platform>.tar
      cd phenix-installer-<version>-<platform>
      sudo ./install --prefix=$STORE/opt/

- Install CCP4 from download.

      tar -xf <sys>_ccp4-<ver>-setup.tar.gz 
      ./ccp4-7.1-setup
      
  - **Caution:** Install to $STORE/opt/ in GUI installer

- Install [XDS](https://strucbio.biologie.uni-konstanz.de/xdswiki/index.php/Installation)
  - Install [XDS](https://xds.mr.mpg.de/html_doc/downloading.html)

        # XDS
        cd $STORE/opt
        curl -s -f https://xds.mr.mpg.de/XDS-INTEL64_Linux_x86_64.tar.gz -o xds.tar.gz
        tar -xzf xds.tar.gz
        rm xds.tar.gz
        mv XDS* xds

  - Install [XDS Accessories](https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/)

        cd $STORE/opt/xds
        # xdsgui
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/xdsgui -o xdsgui
        chmod a+x xdsgui
        # generate_XDS.INP
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/generate_XDS.INP -o generate_XDS.INP
        chmod a+x generate_XDS.INP
        # spot2pdb
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/spot2pdb -o spot2pdb
        chmod a+x spot2pdb
        # xscale_isocluster
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/xscale_isocluster -o xscale_isocluster
        chmod a+x xscale_isocluster
        # xdscc12
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/xdscc12 -o xdscc12
        chmod a+x xdscc12
        # xdsstat
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/xdsstat -o xdsstat
        chmod a+x xdsstat
        # XDS-viewer
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/XDS-viewer -o XDS-viewer
        chmod a+x XDS-viewer
        ln -s XDS-viewer xdsviewer
        ln -s XDS-viewer xds-viewer
        # checkcentering
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/checkcentering -o checkcentering
        chmod a+x checkcentering
        
- Create Protein Environment
  - Install [PyRosetta](https://www.pyrosetta.org/downloads)

      pyenv virtualenv 3.9.7 protein_env
      pyenv local protein_env
      # https://www.pyrosetta.org/downloads
      tar -jxf PyRosetta-<version>.tar.bz2
      cd setup && python setup.py install 
      import pyrosetta; pyrosetta.init()
      # May want to remove local environment file
      
