Name: steam
Version: 1.0
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