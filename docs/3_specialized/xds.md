Install [XDS](https://strucbio.biologie.uni-konstanz.de/xdswiki/index.php/Installation)

  - Install [XDS](https://xds.mr.mpg.de/html_doc/downloading.html)

        # XDS
        cd $STORE/opt
        curl -s -f https://xds.mr.mpg.de/1XDS-INTEL64_Linux_x86_64.tar.gz -o xds.tar.gz
        tar -xzf xds.tar.gz
        rm xds.tar.gz
        mv XDS* xds

  - Install [XDS Accessories](https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/)

        cd $STORE/opt/xds
        # xdsgui
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/xdsgui -o xdsgui
        chmod a+x xdsgui
        # generate_XDS.INP
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/generate_XDS.INP -o generate_XDS.INP
        chmod a+x generate_XDS.INP
        # spot2pdb
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/spot2pdb -o spot2pdb
        chmod a+x spot2pdb
        # xscale_isocluster
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/xscale_isocluster -o xscale_isocluster
        chmod a+x xscale_isocluster
        # xdscc12
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/xdscc12 -o xdscc12
        chmod a+x xdscc12
        # xdsstat
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/xdsstat -o xdsstat
        chmod a+x xdsstat
        # XDS-viewer
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/XDS-viewer -o XDS-viewer
        chmod a+x XDS-viewer
        ln -s XDS-viewer xdsviewer
        ln -s XDS-viewer xds-viewer
        # checkcentering
        curl -s -f https://strucbio.biologie.uni-konstanz.de/pub/linux_bin/checkcentering -o checkcentering
        chmod a+x checkcentering
