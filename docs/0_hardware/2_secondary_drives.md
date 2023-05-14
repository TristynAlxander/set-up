## Secondary Drives

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
- Restart Computer.
