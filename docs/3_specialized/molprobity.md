
Didn't finish this

Note: Should probably figure out how to put this all into a specific environment
    
    cd /opt/
    mkdir molprobity
    cd /opt/molprobity
    
    
    apt-get install -y software-properties-common
    sudo add-apt-repository ppa:ondrej/php
    sudo apt update
    sudo apt upgrade
    sudo apt install -y php5.6

    sudo apt-get install php5.6-gd php5.6-mysql php5.6-imap php5.6-curl php5.6-intl php5.6-pspell php5.6-recode php5.6-sqlite3 php5.6-tidy php5.6-xmlrpc php5.6-xsl php5.6-zip php5.6-mbstring php5.6-soap php5.6-opcache php5.6-common php5.6-json php5.6-readline php5.6-xml libapache2-mod-php5.6 php5.6-cli 
    
    # This fails
    #sudo apt-get install libicu65

    # Attempting to replace above with this.
    apt purge libicu-dev
    apt update
    apt install libicu-dev

    php --version
    # Should say 5.6
    
    wget -O install_via_bootstrap.sh https://github.com/rlabduke/MolProbity/raw/master/install_via_bootstrap.sh


