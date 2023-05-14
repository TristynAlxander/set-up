## Hot-Spot -> Internet : Currently Not Working

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
