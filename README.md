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
  - Probably also want to type in notification to search bar and disable them
- Install on Computer
  - Either Partition for Dual Boot or Wipe your computer.
    - Obviously you're gonna lose data if you're wiping your computer, so be careful.  
  - Install your distribution
  - re-resolve hardware issues.
  - Fix your Update/Back-Up/Snapshot settings
- Fix Default View
  - Edit > Preferences > Views > View New Folders Using > List View

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

Start by checking that `$PYENV_ROOT` is set correctly wherever you set-up your environment (e.g. look in `~/.environ`).
Assuming you have your bash environment set up correctly, I roughly follow [these instructions](https://realpython.com/intro-to-pyenv/#installing-pyenv).

       sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
       libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
       libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

       curl https://pyenv.run | bash

Re-Strart your Computer.

       # Compile and Install Python, this may take a while. Use your version.
       pyenv install #3.9.7
       pyenv global 3.9.7

Note: `pyenv activate my_python_env` to activate environment.
Note: Use `pyenv virtualenv <python_version> <environment_name>` to create new environments and `pyenv local environment_name` to set in a location.
Note: You probably want to `pip install pytest` first thing.
Note: Use `python --version` and `pip freeze > requirements.txt` to export, then remake with the version and reinstall with `pip install -r requirements.txt`
Note: Delete by going to `$PYENV_ROOT/versions` and using `rm -rf` (for virtualenv remove both link and link location).

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
    - `git config --global --add safe.directory $STORE/repos/myRepo`
      - This is very picky about exactly how this is written, and I can't figure out what's wrong.
      - Seems like it only works if I copy/paste 

- Creating a Respository
  - Create a Github Repo [link](https://docs.github.com/en/get-started/quickstart/create-a-repo)
  - Create and Empty Repository `git init` make bare `git config --bool core.bare true`

## Set-Up Common Tools


 - Fix Internet via Android Hot-Spot
   - Enable Phone Modding
    - Enable Developer Mode: Settings > System > About Phone > Build Number > Click 9 times? 7 Times?
    - Enable USB Debug Mode: Settings > System > Developer Options > Debugging > Enable USB Debuging
   - Install and Enable Android Debug Bridge
     - `sudo apt-get install android-tools-adb android-tools-fastboot`
     - Unplug and Replug Device.
     - `adb kill-server`
     - `adb start-server`
     - `sudo adb devices`
     - Might Need [this](https://wiki.archlinux.org/title/Android_Debug_Bridge)
     - Note: Use `adb shell` and `exit` to access android terminal
     - Might Read [This](https://linuxconfig.org/how-to-use-adb-android-debug-bridge-to-manage-your-android-mobile-phone), skip last wireless bit.
     - You might need to activate adb root from the developer settings menu. 
   - Turn Off Betrayal 
    - `settings put global tether_dun_required 0`
    - Note: This only works if the service provider is using the dun tag in their APN type.
  - Root Device
    sudo fastboot
   - https://www.theitstuff.com/root-android-phone
   - https://www.rojtberg.net/668/how-to-root-android-using-ubuntu/
   - https://supersuroot.org/download/
   
   adb reboot bootloader
   `sudo fastboot devices`
   `sudo fastboot oem get_unlock_data`
   Use who maker website to see if you can unlock -- I haven't made it past this. Mine won't unlock
   `sudo fastboot oem unlock`
   
   - Tweak Access Point Name Settings?
   
   - Find Where APN Settings are stored on android device: Seems to vary significantly by device.
    - `/data/data/com.android.settings/shared_prefs/com.android.settings_preferences.x­ml`
    - `/system/etc/apns-conf.xml`
    - `/data/data/com.android.providers.telephony/databases/.telephony.db`
    - `/data/user/com.android.providers.telephony/databases/.telephony.db`
    - `/data/user_de/0/com.android.providers.telephony/databases/telephony.db/carriers`
      - user_de is user specific Device Encrypted storage
    
    Default APNs: /system/etc/apns-conf.xml
    OEM APNs: /oem/telephony/apns-conf.xml
    OTA Update APNs: /data/misc/apns/apns-conf.xml
    Product APNs: /product/etc/apns-conf.xml
    `/data/misc/apns/apns-conf.xml`
    
   “Mobile Country Code” (MCC) and “Mobile Network Code” (MNC)
   https://4gbritain.org/settings-put-global-tether_dun_required-0/
   Settings > Network & Internet > Mobile Network > Access point Names > `default,supl,dun`
   
   
   
   
   adb tcpip 7997
   Settings > System > About Phone > IP Address
   abd connect [your_ip_address_here]
   abd connect 100.93.190.201
   
   
   
   

## Install Semi-Common Tools

    sudo apt install inkscape
    sudo apt install texlive-full
    sudo apt install pdf2svg
    sudo apt install ffmpeg
    
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

- `sudo apt install emboss`
  - `abiview -infile thing.ab1 -outseq thing.fasta -graph png`

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
        curl -s -f https://xds.mr.mpg.de/1XDS-INTEL64_Linux_x86_64.tar.gz -o xds.tar.gz
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
- Install PyMol: `sudo apt-get install pymol`        
- Create Protein Environment

      pyenv virtualenv 3.9.7 protein_env
      pyenv activate protein_env
      pyenv local protein_env

  - Install [Pymol](https://github.com/schrodinger/pymol-open-source/blob/master/INSTALL) ^^[1](https://pymolwiki.org/index.php/Linux_Install)
    
        apt install git build-essential libglew-dev libpng-dev libfreetype6-dev libxml2-dev libmsgpack-dev libglm-dev libnetcdf-dev
        pyenv activate protein_env
        pip install PyQt5
        if [ ! -d $STORE/opt ]; then mkdir $STORE/opt; fi
        cd $STORE/opt
        git clone https://github.com/schrodinger/pymol-open-source.git
        git clone https://github.com/rcsb/mmtf-cpp.git
        mv mmtf-cpp/include/mmtf* pymol-open-source/include/
        cd pymol-open-source
        prefix=$STORE/opt/pymol
        python setup.py build install --home=$prefix
        # Note there is an alias that matches up with all this
        rm -r $STORE/opt/mmtf-cpp/ $STORE/opt/pymol-open-source/
      
  - Install [PyRosetta](https://www.pyrosetta.org/downloads)
      
        # https://www.pyrosetta.org/downloads
        tar -jxf PyRosetta-<version>.tar.bz2
        cd setup && python setup.py install 
        import pyrosetta; pyrosetta.init()
        # May want to remove local environment file
  
