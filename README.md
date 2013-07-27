Fully automatic build
========
Just open terminal and execute this commands:
```
wget https://github.com/xvitaly/steamrpm/raw/master/genrpm.sh && chmod +x genrpm.sh && ./genrpm.sh
```
Then go to Step 7.

Step 1
========
Download original package for Ubuntu:

```
cd ~
wget http://media.steampowered.com/client/installer/steam.deb
```

Step 2
=======
Unpack Ubuntu package by using **ar** tool:

```
cd ~
ar vx steam.deb
```

You will get three files: **debian-binary**, **control.tar.gz** and **data.tar.gz**. 
We need only **data.tar.gz**. All others can be deleted.

Step 3
=======

Install RPMBuild. On Fedora/CentOS/RHEL:

```
sudo yum -y install rpm-build
```

On openSUSE:

```
sudo zypper install rpmbuild
```

Step 4
=======

Rename and copy **data.tar.gz** to rpmbuild working directory:

```
cd ~
mkdir -p ~/rpmbuild/SOURCES/
cp -f data.tar.gz ~/rpmbuild/SOURCES/steam.tar.gz
```

Step 5
=======

Download spec file for rpmbuild:

```
cd ~
wget https://github.com/xvitaly/steamrpm/raw/master/steam.spec
```

Step 6
=======

Run rpmbuild:

```
cd ~
rpmbuild -bb --clean steam.spec
```

You will get Steam RPM Package for GNU/Linux in **~/rpmbuild/RPMS/i686/** (on 32-bit systems) or in **~/rpmbuild/RPMS/x86_64/** (on 64-bit).

Step 7
=======

Install package. On Fedora/CentOS/RHEL:

```
sudo yum -y install ~/rpmbuild/RPMS/`uname -m`/steam*
```

On openSUSE:

```
sudo zypper install ~/rpmbuild/RPMS/`uname -m`/steam*.rpm
```