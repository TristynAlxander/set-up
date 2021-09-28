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
      sudo mkdir /media/tristin/DATA

    - Use `atom /etc/fstab` to add `UUID=F8E2C122E2C0E64A /media/tristin/DATA    auto nosuid,nodev,nofail,x-gvfs-show 0 0`
    -Test if you did it right `sudo mount -a`
    - You may have to restart here. Unclear it just started working.

- Clean up bash
  - `/etc/login.defs` remove `:/usr/local/games:/usr/games`
  - `/etc/environment` remove `:/usr/games:/usr/local/games:/snap/bin`
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

       # Compile and Install Python, this will take a while. Use your version.
       pyenv install #3.9.7

Note: Use `pyenv virtualenv <python_version> <environment_name>` to create new environments.

## Set-Up Git

- Set-Up Git
  - `git config --global user.email "you@email.com"`
  - `git config --global user.name "UserName"`

- Make repos directory `mkdir $STORE/repos`
- Symlink `ln -s $STORE/repos ~/repos`
- Go to repos directory `cd $STORE/repos`
- Downloading a Repository
  - Use `git clone URL` with URL as:
    - `https://Username`:`Password`@`github.com/myRepoDir/myRepo.git`
    - `https://Username`:`Personal_Access_Token`@`github.com/myRepoDir/myRepo.git`

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
  - disable `bracket-matcher`
  - `apm install duplicate-line-or-selection`
  - Check if `markdown-preview` is already installed. if not `apm install markdown-preview`
  - append duplicate key to `~/.atom/keymap.cson`

        'atom-workspace atom-text-editor:not([mini])':
          'ctrl-d': 'duplicate-line-or-selection:duplicate'

- Fix Firefox
  - Set default Browser to Google.
  - Note: FTP links can be open in the file manager, then the htmls in those directories can be open in firefox. I don't know why.


## Install Semi-Common Tools

    sudo apt install inkscape
    sudo apt install texlive-full
    sudo apt install pdf2svg
