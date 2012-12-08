Name: steam
Version: 0.1
Release: 1
Group: Applications/Games
BuildArch: noarch
Source: steam.tar.gz
Summary: Steam Client
URL: http://www.steampowered.com/
License: EULA
BuildRoot: %{_tmppath}/%{name}-root
Vendor: Valve
Packager: V1TSK <vitaly@easycoding.org>
Requires: ld-linux.so.2
Requires: libX11.so.6
Requires: libstdc++.so.6
Requires: libXrandr.so.2
Requires: libXext.so.6
Requires: libGL.so.1
Requires: libpangoft2-1.0.so.0
Requires: libpango-1.0.so.0
Requires: libfreetype.so.6
Requires: libfontconfig.so.1
Requires: libgobject-2.0.so.0
Requires: libgtk-x11-2.0.so.0
Requires: librt.so.1
Requires: libm.so.6
Requires: libdl.so.2
Requires: libpthread.so.0
Requires: libc.so.6
Requires: libxcb.so.1
Requires: libgcc_s.so.1
Requires: libXau.so.6

%description
Steam Client for GNU/Linux

%prep
%setup -q -c -n %{name}

%build
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/
cp -fpr %_builddir/steam/* %{buildroot}
chmod +x %{buildroot}/usr/bin/steam

%install
find %{buildroot} -not -type d -printf "/%%P\n" | sed '/\/man\//s/$/\*/' > manifest

%files -f manifest