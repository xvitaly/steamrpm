#!/bin/sh

TMPATH=/tmp/strpmgen/

echo Creating temporary directory for building process...
rm -rf $TMPATH
mkdir -p $TMPATH
cd $TMPATH

echo Downloading Ubuntu package...
wget http://media.steampowered.com/client/installer/steam.deb

echo Unpacking Ubuntu package...
ar vx steam.deb

echo Checking rpmbuild working directory...
if [ ! -d ~/rpmbuild/SOURCES/ ]; then
  echo Creating SOURCES in rpmbuild working directory...
  mkdir -p ~/rpmbuild/SOURCES/
fi

echo Copying archive with binaries to rpmbuild working directory...
cp -f data.tar.gz ~/rpmbuild/SOURCES/steam.tar.gz

echo Downloading SPEC file...
wget https://github.com/xvitaly/steamrpm/raw/master/steam.spec

echo Building package...
rpmbuild -ba steam.spec

echo Executting cleanup...
rm -rf $TMPATH