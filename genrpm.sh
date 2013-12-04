#!/bin/sh

echo Creating temporary directory for building process...
TMPATH=`mktemp -d`
cd $TMPATH

echo Downloading Ubuntu package...
wget http://media.steampowered.com/client/installer/steam.deb -O $TMPATH/steam.deb 2> /dev/null

if [ -f "$TMPATH/steam.deb" ]; then
  echo Unpacking Ubuntu package...
  ar vx steam.deb > /dev/null 2> /dev/null
  
  if [ -f "$TMPATH/data.tar.gz" ]; then
    echo Checking rpmbuild working directory...
    if [ ! -d ~/rpmbuild/SOURCES/ ]; then
      echo Creating SOURCES in rpmbuild working directory...
      mkdir -p ~/rpmbuild/SOURCES/
    fi
    
    echo Copying archive with binaries to rpmbuild working directory...
    cp -f data.tar.gz ~/rpmbuild/SOURCES/steam.tar.gz
    
    echo Downloading SPEC file...
    wget https://github.com/xvitaly/steamrpm/raw/master/steam.spec -O $TMPATH/steam.spec 2> /dev/null
    
    if [ -f "$TMPATH/steam.spec" ]; then
      
      if [ -f "$TMPATH/data.tar.gz" ]; then
	tar -zxf control.tar.gz -C $TMPATH > /dev/null 2> /dev/null
	if [ -f "$TMPATH/control" ]; then
	  echo Updating version info from DEB package...
	  sed -i "s/Version: .*/Version: `awk '/Version:/ {print $2}' control`/g" steam.spec
	fi
      fi
      
      echo Building package...
      rpmbuild -bb --clean --buildroot ~/rpmbuild/BUILDROOT/steam-root steam.spec > /dev/null 2> /dev/null
    fi
  fi
fi

echo Executting cleanup...
rm -rf $TMPATH
