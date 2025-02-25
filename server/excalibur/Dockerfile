FROM ubuntu:24.04
# docker run -it ubuntu:24.04
# root@<docker-image>:# apt udpate && apt upgrade -y && apt install wget -y


## ## =========================== DOESN'T WORK (NO SNAP IN DOCKER) ============================ ## ##
#### TO-DO: Try to fix the timezone # DEBIAN_FRONTEND=noninteractive apt-get -y install snapd
#### dpkg-reconfigure debconf --frontend=noninteractive
## root@<docker-image>:# apt install snapd -y ## Asks for timezone

#### Install the ghost-script that we need
## root@<docker-image>:# cd /tmp
## root@<docker-image>:# wget https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10040/gs_10.04.0_amd64_snap.tgz
## root@<docker-image>:# gunzip gs_10.04.0_amd64_snap.tgz
## root@<docker-image>:# tar xvf gs_10.04.0_amd64_snap.tar
## root@<docker-image>:# snap install --devmode gs_10.04.0_amd64_snap/gs_10.04.0_amd64.snap
## ## ========================================================================================= ## ##

## Download the source files for ghostscript
# root@<docker-image>:# wget https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10040/ghostpdl-10.04.0.tar.gz
# root@<docker-image>:# gunzip ghostpdl-10.04.0.tar.gz
# root@<docker-image>:# tar xvf ghostpdl-10.04.0.tar

## Add the make files / build-essentials
$ apt install build-essential -y
## tk is required for install ghostscript
$ apt install python3-tk

## Link : https://ghostscript.readthedocs.io/en/gs10.04.0/Install.html#install-html
##      : https://ghostscript.com/releases/gpdldnld.html
##      : https://ghostscript.readthedocs.io/en/gs10.04.0/Make.html
$ cd ghostpdl-10.04.0
$ ./configure
$ make
$ make install

# root@<docker-image>:# 


# root@<docker-image>:# apt install python3

