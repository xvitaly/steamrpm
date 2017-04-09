About
========
This package is no longer supported. Use `steam` package from RPMFusion on Fedora and from main repositories on openSUSE.

Installation on Fedora
========
Add [RPMFusion repositories](https://rpmfusion.org/):
```bash
sudo dnf install --nogpgcheck https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

Install [steam package](http://koji.rpmfusion.org/koji/packageinfo?packageID=413):
```bash
sudo dnf install steam
```

Installation on openSUSE
========
Install [steam package](https://software.opensuse.org/package/steam):
```bash
sudo zypper in steam
```
