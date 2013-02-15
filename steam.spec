Name: steam
Version: 1.0.25
Release: 1
Group: Applications/Games
BuildArch: noarch
Source: steam.tar.gz
Summary: Steam Client
URL: http://www.steampowered.com/
License: EULA
BuildRoot: %{_tmppath}/%{name}-root
Vendor: Valve

# Setting macro...
%define pf %{nil}
%ifarch x86_64
  %if 0%{?suse_version}
    %define pf -32bit
  %endif
  %if 0%{?fedora}
    %define pf (x86-32)
  %endif
%endif

# Distribution independent dependecies...
Requires: cups-libs%{pf} >= 1.4.0
Requires: fontconfig%{pf} >= 2.8.0
Requires: glibc%{pf} >= 2.15
Requires: openal-soft >= 1.13
Requires: zlib%{pf} >= 1.2.3.3

# Dependencies for Fedora/CentOS/RHEL (taken from SPEC by Tom Callaway <spot@fedoraproject.org>)...
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
Requires: libcurl{pf} >= 7.16.2-1
Requires: libogg{pf} >= 1.0
Requires: pixman{pf} >= 0.24.4
Requires: SDL{pf} >= 1.2.10
Requires: libtheora{pf} >= 1.0
Requires: libvorbis{pf} >= 1.1.2
Requires: alsa-lib{pf} >= 1.0.23
Requires: cairo{pf} >= 1.6.0
Requires: dbus-libs{pf} >= 1.2.14
Requires: freetype{pf} >= 2.3.9
Requires: libgcc{pf} >= 4.1.1
Requires: libgcrypt{pf} >= 1.4.5
Requires: gdk-pixbuf2{pf} >= 2.22.0
Requires: glib2{pf} >= 2.14.0
Requires: gtk2{pf} >= 2.24.0
Requires: nspr{pf} >= 1.8.0.10
Requires: nss{pf} >= 3.12.3
Requires: openal-soft{pf} >= 1.13
Requires: pango{pf} >= 1.22.0
Requires: pulseaudio-libs{pf} >= 0.99.1
Requires: libstdc++{pf} >= 4.6
Requires: libX11{pf} >= 1.4.99.1
Requires: libXext{pf}
Requires: libXfixes{pf}
Requires: libXi{pf} >= 1.2.99.4
Requires: libXrandr{pf} >= 1.2.99.3
Requires: libXrender{pf}
Requires: mesa-dri-drivers{pf}
Requires: libasyncns{pf}
Requires: atk{pf}
Requires: avahi-libs{pf}
Requires: libcom_err{pf}
Requires: libdrm{pf}
Requires: mesa-libEGL{pf}
Requires: expat{pf}
Requires: libffi{pf}
Requires: flac{pf}
Requires: mesa-libGL{pf}
Requires: libgcrypt{pf}
Requires: gnutls{pf}
Requires: libgpg-error{pf}
Requires: gsm{pf}
Requires: krb5-libs{pf}
Requires: harfbuzz{pf}
Requires: libICE{pf}
Requires: libicu{pf}
Requires: json-c{pf}
Requires: keyutils-libs{pf}
Requires: p11-kit{pf}
Requires: pcre{pf}
Requires: libselinux{pf}
Requires: libSM{pf}
Requires: libsndfile{pf}
Requires: libtasn1{pf}
Requires: libuuid{pf}
Requires: tcp_wrappers-libs{pf}
Requires: libXau{pf}
Requires: libxcb{pf}
Requires: libXcomposite{pf}
Requires: libXcursor{pf}
Requires: libXdamage{pf}
Requires: libXinerama{pf}
Requires: libXtst{pf}
Requires: libXxf86vm{pf}
%if 0%{?fedora} >= 18
Requires: libpng12{pf} >= 1.2.13
Requires: systemd-libs{pf}
%else
Requires: libudev{pf}
%endif
%if 0%{?fedora} == 17
Requires: libpng-compat{pf} >= 1.2.13
%endif
%if 0%{?fedora} <= 16
Requires: libpng >= 1.2.13
%endif
%if 0%{?fedora} >= 17
Requires: mesa-libgbm{pf}
Requires: mesa-libglapi{pf}
Requires: libwayland-client{pf}
Requires: libwayland-server{pf}
%endif
%endif

# Dependencies for openSUSE and SLES...
%if 0%{?suse_version} || 0%{?sles_version}
Requires: Mesa%{pf}
Requires: mozilla-nss{pf}
Requires: libcurl4{pf} >= 7.16.2-1
Requires: libogg0{pf} >= 1.0
Requires: libpixman-1-0{pf} >= 0.24.4
Requires: libSDL-1_2-0{pf} >= 1.2.10
Requires: libSDL2-2_0-0{pf}
Requires: libtheora0{pf} >= 1.0
Requires: libvorbis0{pf} >= 1.1.2
Requires: libcairo2{pf} >= 1.6.0
Requires: libdbus-1-3{pf} >= 1.2.14
Requires: libfreetype6{pf} >= 2.3.9
Requires: libgcc47{pf} >= 4.1.1
Requires: libgcrypt11{pf} >= 1.4.5
Requires: libgdk_pixbuf-2_0-0{pf} >= 2.22.0
Requires: libglib-2_0-0{pf} >= 2.14.0
Requires: libgtk-2_0-0{pf} >= 2.24.0
Requires: mozilla-nspr{pf} >= 1.8.0.10
Requires: libopenal1-soft{pf} >= 1.13
Requires: libpango-1_0-0{pf} >= 1.22.0
Requires: libpulse0{pf} >= 0.99.1
Requires: libstdc++47{pf} >= 4.6
Requires: libX11-6{pf} >= 1.4.99.1
Requires: libXext6{pf}
Requires: libXfixes3{pf}
Requires: libXi6{pf} >= 1.2.99.4
Requires: libXrandr2{pf} >= 1.2.99.3
Requires: libXrender1{pf}
Requires: Mesa-libIndirectGL1{pf}
Requires: Mesa-libEGL1{pf}
Requires: libcares2{pf}
Requires: libasound2{pf}
Requires: libatk-1_0-0{pf}
Requires: libavahi-client3{pf}
Requires: libavahi-common3{pf}
Requires: libcom_err2{pf}
Requires: libdrm2{pf}
Requires: libexpat1{pf}
Requires: libffi47{pf}
Requires: libFLAC8{pf}
Requires: Mesa-libGL1{pf}
Requires: libgcrypt11{pf}
Requires: libgnutls28{pf}
Requires: libgpg-error0{pf}
Requires: libgsm1{pf}
Requires: krb5{pf}
Requires: libharfbuzz0{pf}
Requires: libICE6{pf}
Requires: libicu49{pf}
Requires: libjson0{pf}
Requires: libkeyutils1{pf}
Requires: libp11-kit0{pf}
Requires: libpcre1{pf}
Requires: libselinux1{pf}
Requires: libSM6{pf}
Requires: libsndfile1{pf}
Requires: libtasn1-3{pf}
Requires: libuuid1{pf}
Requires: tcpd{pf}
Requires: libXau6{pf}
Requires: libxcb1{pf}
Requires: libXcomposite1{pf}
Requires: libXcursor1{pf}
Requires: libXdamage1{pf}
Requires: libXinerama1{pf}
Requires: libXtst6{pf}
Requires: libXxf86vm1{pf}
%endif


%description
Steam Client for GNU/Linux

%prep
%setup -q -c -n %{name}

%build
# Do nothing...

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/
cp -fpr %_builddir/steam/* %{buildroot}
rm -rf %{buildroot}/etc/apt/
chmod +x %{buildroot}/usr/bin/steam
chmod +x %{buildroot}/usr/bin/steamdeps
find %{buildroot} -not -type d -printf "/%%P\n" | sed '/\/man\//s/$/\*/' > manifest

%files -f manifest
%defattr(-,root,root)
