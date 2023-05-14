# Zotero

    ZOTERO=Zotero-6.0.26_linux-x86_64
    mv ~/Downloads/$ZOTERO.tar.bz2 /opt/
    cd /opt/
    tar -xjf $ZOTERO.tar.bz2
    mv Zotero_linux-x86_64 zotero
    ln -s $OPT/zotero/zotero.desktop ~/.local/share/applications/zotero.desktop

Edit > Preferences > Advanced > Files and Folders > Data Directory Location > Custom > Show hidden folders > ~/.zotero/data

