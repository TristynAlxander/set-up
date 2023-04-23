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

Users should keep all their files in a separate location. Preferably a separate hard-drive.
  
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

- Restart Computer.

##

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

## Install Uncommon Tools

Note: It may be wise to load all the crystallography environments at once, but I'm not sure yet.

- `if [ ! -d $STORE/opt ]; then mkdir $STORE/opt; fi`


- Install Tor
  - Actually Tor cannot be installed on a secondary hard drive.
  - `if [ ! -d $STORE/opt ]; then mkdir $STORE/opt; fi`
  - `cd $STORE/opt`
  - move download to opt
  - `tar -xf [TB archive]`
  - 

- `sudo apt install emboss`
  - `abiview -infile thing.ab1 -outseq thing.fasta -graph png`
