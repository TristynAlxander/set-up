# Fix Firefox Settings.
  - Set default Browser to Google.
  - Note: FTP links can be open in the file manager, then the htmls in those directories can be open in firefox. I don't know why.
  - `about:config` > `widget.non-native-theme.scrollbar.size` > 24
  - `about:config` > `widget.non-native-theme.scrollbar.size.override` > 24
  - `about:config` > `widget.non-native-theme.gtk.scrollbar.allow-buttons` > True
# Install Selenium
  
  Install Gecko Driver:
    [Download](https://github.com/mozilla/geckodriver/releases/latest)
    Extract: tar -xzf geckodriver-???.tar.gz
    chmod +777 geckodriver 
    mv geckodriver ~/.bin/
  Make Selenium Environments
    check required python: https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html
    
    conda create --name words_selenium python=3.11.1
    conda activate words_selenium
    conda install conda-forge::selenium
    
  
  
