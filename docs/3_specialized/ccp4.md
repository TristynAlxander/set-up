#CCP4

Download

    tar -xf <sys>_ccp4-<ver>-setup.tar.gz
    mv ccp4_<ver> $OPT
    cd $OPT/ccp4_<ver>
    
    # This Part is inconsistent
    ./BINARY.setup
    # Or 
    ./ccp4-7.1-setup
    

**Caution:** Install to $OPT/ in GUI installer
**Caution:** Need to Activate environment.
    
    # Adjust in Alias File
    alias ccp4_env='export PATH=$OPT/ccp4-<ver>/bin:$PATH; source ccp4.setup-sh'

