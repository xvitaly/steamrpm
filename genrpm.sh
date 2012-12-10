#!/bin/sh

TMPATH=/tmp/strpmgen/

echo Creating temporary directory for building process...
rm -rf $TMPATH
mkdir -p $TMPATH
cd $TMPATH

echo Downloading Ubuntu package...
wget http://media.steampowered.com/client/installer/steam.deb

if [ -f "$TMPATH/steam.deb" ]; then
  echo Unpacking Ubuntu package...
  ar vx steam.deb

  echo Checking rpmbuild working directory...
  if [ ! -d ~/rpmbuild/SOURCES/ ]; then
    echo Creating SOURCES in rpmbuild working directory...
    mkdir -p ~/rpmbuild/SOURCES/
  fi

  if [ -f "$TMPATH/data.tar.gz" ]; then
    echo Copying archive with binaries to rpmbuild working directory...
    cp -f data.tar.gz ~/rpmbuild/SOURCES/steam.tar.gz
    
    echo Downloading SPEC file...
    wget https://github.com/xvitaly/steamrpm/raw/master/steam.spec

    if [ -f "$TMPATH/steam.spec" ]; then
      echo Building package...
      rpmbuild -ba steam.spec
    fi
  fi
fi

echo Executting cleanup...
rm -rf $TMPATH