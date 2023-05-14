## Installation Linux

- Download your distribution of choice.
  - If possible, download with unofficial & proprietary firmware/drivers.
  - Pay attention to the architecture (probably `amd64/`)
  - Download as dvd
  - Recommended Distributions:
    - [Mint Cinnamon](https://linuxmint.com/download.php)
    - [Devian](http://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/)
    - Ubuntu
- Install your Distribution on a USB drive.
  - From Windows, use [rufus](https://rufus.ie/en/) to prepare a USB, use default settings.
  - From Linux you can just right click the iso file to prepare a USB
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


You have to disable windows fast boot 
On ASUS machines ACPI is often "VMD Controller" 
Also Linux has a separate kernel that may be necessary for drivers on extremely new machines. 

See `1_common/0_cmds` to set-up your paths and environments.