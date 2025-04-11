


# Fonts

Download and extract fonts e.g. Helvetica Neue, Times new Roman
Install fonts at /usr/share/fonts  or   /home/username/.local/fonts

sudo cp -r ~/downloads/helvetica-neue-5 /usr/share/fonts/

Note: Seems Tff format is weird and better to have otf format

for Times New Roman 
Software manager and search for "ttf-mscorefonts-installer" Install

# Spelling

Words For Spelling:
dimerization, interchain, heterodimers, misfolding, hydrophobicity, deamidation, carbamylation, resuspended

# Macros

Setting Up Macros
  
  Install Macro Stuff
    sudo apt-get update -y
    sudo apt-get install -y libreoffice-script-provider-python
  
  Go to one of these locations to add a macro file or see examples:
    /usr/lib/libreoffice/share/Scripts/python/
    ~/.config/libreoffice/4/user/Scripts/python/
    ~/.config/libreoffice/4/user/Scripts/python/pythonpath
  
  Tools -> Customize > Toolbars tab > Category > Macros

Specific Macros
  Input-Output Tools (I can't get this to work)
    atom /usr/lib/libreoffice/share/Scripts/python/screen_io.py
    Copy Text from https://help.libreoffice.org/latest/en-GB/text/sbasic/python/python_screen.html
    Open LibreOffice
    Tools -> Macros -> Organize Macros -> Basic ... -> Macro From -> My Macros -> Standard -> New -> uiScripts
    Copy Text from https://help.libreoffice.org/latest/en-GB/text/sbasic/python/python_screen.html
    Restart LibreOffice

