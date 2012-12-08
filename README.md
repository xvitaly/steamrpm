Step 1.
========
Download original package for Ubuntu:
```
cd ~
wget http://media.steampowered.com/client/installer/steam.deb
```

Step 2
=======
Unpack Ubuntu package by using <b>ar</b> tool:
```
cd ~
ar vx steam.deb
```
You will get three files: <b>debian-binary</b>, <b>control.tar.gz</b> and <b>data.tar.gz</b>. We needs only <b>data.tar.gz</b>. All others can be deleted.

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
Rename and copy <b>data.tar.gz</b> to rpmbuild working directory:
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
rpmbuild -ba steam.spec
```
You will get Steam RPM Package for GNU/Linux in <b>~/rpmbuild/RPMS/noarch/</b>.

Step 7
=======
Install package. On Fedora/CentOS/RHEL:
```
sudo yum -y localinstall ~/rpmbuild/RPMS/noarch/steam*
```
On openSUSE:
```
sudo zypper install ~/rpmbuild/RPMS/noarch/steam*.rpm
```