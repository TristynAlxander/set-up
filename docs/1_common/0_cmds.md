# Default Environment Set-Up

    # Link Repo Aliases and Environment Variables to Standard Location
    #rm ~/.environment, ~/.alias
    
    # Note: This must use full path not ~
    export UPLOADS="/home/tristin/Uploads"
    
    chmod 777 $UPLOADS/set-up/.environment
    chmod 777 $UPLOADS/set-up/.alias
    sudo ln -sf $UPLOADS/set-up/.environment ~/.environment
    sudo ln -sf $UPLOADS/set-up/.alias ~/.alias
    
    # Add Check for Aliases and Environment Variables to BashRC
    echo "if [ -t 0 ] && [ -t 1 ]; then"                          >> ~/.bashrc
    echo "  if ! [ \$ENV_CHECK ]; then source ~/.environment; fi" >> ~/.bashrc
    echo "  if ! [ \$ALIAS_CHECK ]; then source ~/.alias; fi"     >> ~/.bashrc
    echo "fi"                                                     >> ~/.bashrc
    
    # Add Check for Aliases and Environment Variables to Profile
    echo "if [ -t 0 ] && [ -t 1 ]; then"                          >> ~/.profile
    echo "  if ! [ \$ENV_CHECK ]; then source ~/.environment; fi" >> ~/.profile
    echo "  if ! [ \$ALIAS_CHECK ]; then source ~/.alias; fi"     >> ~/.profile
    echo "fi"                                                     >> ~/.profile

Restart Computer.

# Install Common Tools via Command Line

    sudo apt update && sudo apt upgrade -y
    sudo apt install git-all
    sudo apt install hardlink

# Preferences


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


