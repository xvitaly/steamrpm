Name: steam
Version: 1.0.22
Release: 2
Group: Applications/Games
BuildArch: noarch
Source: steam.tar.gz
Summary: Steam Client
URL: http://www.steampowered.com/
License: EULA
BuildRoot: %{_tmppath}/%{name}-root
Vendor: Valve

# Distribution independent dependecies...
Requires: libjpeg-turbo(x86-32)

# Dependencies for Fedora/CentOS/RHEL (taken from SPEC by Tom Callaway <spot@fedoraproject.org>)...
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
Requires: libcurl(x86-32) >= 7.16.2-1
Requires: libogg(x86-32) >= 1.0
Requires: pixman(x86-32) >= 0.24.4
Requires: SDL(x86-32) >= 1.2.10
Requires: libtheora(x86-32) >= 1.0
Requires: libvorbis(x86-32) >= 1.1.2
Requires: alsa-lib(x86-32) >= 1.0.23
Requires: glibc(x86-32) >= 2.15
Requires: cairo(x86-32) >= 1.6.0
Requires: cups-libs(x86-32) >= 1.4.0
Requires: dbus-libs(x86-32) >= 1.2.14
Requires: fontconfig(x86-32) >= 2.8.0
Requires: freetype(x86-32) >= 2.3.9
Requires: libgcc(x86-32) >= 4.1.1
Requires: libgcrypt(x86-32) >= 1.4.5
Requires: gdk-pixbuf2(x86-32) >= 2.22.0
Requires: glib2(x86-32) >= 2.14.0
Requires: gtk2(x86-32) >= 2.24.0
Requires: nspr(x86-32) >= 1.8.0.10
Requires: nss(x86-32) >= 3.12.3
Requires: openal-soft(x86-32) >= 1.13
Requires: pango(x86-32) >= 1.22.0
Requires: pulseaudio-libs(x86-32) >= 0.99.1
Requires: libstdc++(x86-32) >= 4.6
Requires: libX11(x86-32) >= 1.4.99.1
Requires: libXext(x86-32)
Requires: libXfixes(x86-32)
Requires: libXi(x86-32) >= 1.2.99.4
Requires: libXrandr(x86-32) >= 1.2.99.3
Requires: libXrender(x86-32)
Requires: zlib(x86-32) >= 1.2.3.3
Requires: mesa-dri-drivers(x86-32)
Requires: libasyncns(x86-32)
Requires: atk(x86-32)
Requires: avahi-libs(x86-32)
Requires: libcom_err(x86-32)
Requires: libdrm(x86-32)
Requires: mesa-libEGL(x86-32)
Requires: expat(x86-32)
Requires: libffi(x86-32)
Requires: flac(x86-32)
Requires: mesa-libGL(x86-32)
Requires: libgcrypt(x86-32)
Requires: gnutls(x86-32)
Requires: libgpg-error(x86-32)
Requires: gsm(x86-32)
Requires: krb5-libs(x86-32)
Requires: harfbuzz(x86-32)
Requires: libICE(x86-32)
Requires: libicu(x86-32)
Requires: json-c(x86-32)
Requires: keyutils-libs(x86-32)
Requires: p11-kit(x86-32)
Requires: pcre(x86-32)
Requires: libselinux(x86-32)
Requires: libSM(x86-32)
Requires: libsndfile(x86-32)
Requires: libtasn1(x86-32)
Requires: libuuid(x86-32)
Requires: tcp_wrappers-libs(x86-32)
Requires: libXau(x86-32)
Requires: libxcb(x86-32)
Requires: libXcomposite(x86-32)
Requires: libXcursor(x86-32)
Requires: libXdamage(x86-32)
Requires: libXinerama(x86-32)
Requires: libXtst(x86-32)
Requires: libXxf86vm(x86-32)
%if 0%{?fedora} >= 18
Requires: libpng12(x86-32) >= 1.2.13
Requires: systemd-libs(x86-32)
%else
Requires: libudev(x86-32)
%endif
%if 0%{?fedora} == 17
Requires: libpng-compat(x86-32) >= 1.2.13
%endif
%if 0%{?fedora} <= 16
Requires: libpng >= 1.2.13
%endif
%if 0%{?fedora} >= 17
Requires: mesa-libgbm(x86-32)
Requires: mesa-libglapi(x86-32)
Requires: libwayland-client(x86-32)
Requires: libwayland-server(x86-32)
%endif
%endif

# Dependencies for openSUSE and SLES...
%if 0%{?suse_version} || 0%{?sles_version}
%ifarch x86_64
Requires: Mesa-32bit(x86-64)
Requires: mozilla-nss-32bit(x86-64)
Requires: libcurl4-32bit(x86-64) >= 7.16.2-1
Requires: libogg0-32bit(x86-64) >= 1.0
Requires: libpixman-1-0-32bit(x86-64) >= 0.24.4
Requires: libSDL-1_2-0-32bit(x86-64) >= 1.2.10
Requires: libSDL2-2_0-0-32bit(x86-64)
Requires: libtheora0-32bit(x86-64) >= 1.0
Requires: libvorbis0-32bit(x86-64) >= 1.1.2
Requires: glibc-32bit(x86-64) >= 2.15
Requires: libcairo2-32bit(x86-64) >= 1.6.0
Requires: cups-libs-32bit(x86-64) >= 1.4.0
Requires: libdbus-1-3-32bit(x86-64) >= 1.2.14
Requires: fontconfig-32bit(x86-64) >= 2.8.0
Requires: libfreetype6-32bit(x86-64) >= 2.3.9
Requires: libgcc47-32bit(x86-64) >= 4.1.1
Requires: libgcrypt11-32bit(x86-64) >= 1.4.5
Requires: libgdk_pixbuf-2_0-0-32bit(x86-64) >= 2.22.0
Requires: libglib-2_0-0-32bit(x86-64) >= 2.14.0
Requires: libgtk-2_0-0-32bit(x86-64) >= 2.24.0
Requires: mozilla-nspr-32bit(x86-64) >= 1.8.0.10
Requires: libopenal1-soft-32bit(x86-64) >= 1.13
Requires: libpango-1_0-0-32bit(x86-64) >= 1.22.0
Requires: libpulse0-32bit(x86-64) >= 0.99.1
Requires: libstdc++47-32bit(x86-64) >= 4.6
Requires: libX11-6-32bit(x86-64) >= 1.4.99.1
Requires: libXext6-32bit(x86-64)
Requires: libXfixes3-32bit(x86-64)
Requires: libXi6-32bit(x86-64) >= 1.2.99.4
Requires: libXrandr2-32bit(x86-64) >= 1.2.99.3
Requires: libXrender1-32bit(x86-64)
Requires: zlib-32bit(x86-64) >= 1.2.3.3
Requires: Mesa-libIndirectGL1-32bit(x86-64)
Requires: Mesa-libEGL1-32bit(x86-64)
Requires: libcares2-32bit(x86-64)
Requires: libasound2-32bit(x86-64)
Requires: libatk-1_0-0-32bit(x86-64)
Requires: libavahi-client3-32bit(x86-64)
Requires: libavahi-common3-32bit(x86-64)
Requires: libcom_err2-32bit(x86-64)
Requires: libdrm2-32bit(x86-64)
Requires: libexpat1-32bit(x86-64)
Requires: libffi47-32bit(x86-64)
Requires: libFLAC8-32bit(x86-64)
Requires: Mesa-libGL1-32bit(x86-64)
Requires: libgcrypt11-32bit(x86-64)
Requires: libgnutls28-32bit(x86-64)
Requires: libgpg-error0-32bit(x86-64)
Requires: libgsm1-32bit(x86-64)
Requires: krb5-32bit(x86-64)
Requires: libharfbuzz0-32bit(x86-64)
Requires: libICE6-32bit(x86-64)
Requires: libicu49-32bit(x86-64)
Requires: libjson0-32bit(x86-64)
Requires: libkeyutils1-32bit(x86-64)
Requires: libp11-kit0-32bit(x86-64)
Requires: libpcre1-32bit(x86-64)
Requires: libselinux1-32bit(x86-64)
Requires: libSM6-32bit(x86-64)
Requires: libsndfile1-32bit(x86-64)
Requires: libtasn1-3-32bit(x86-64)
Requires: libuuid1-32bit(x86-64)
Requires: tcpd-32bit(x86-64)
Requires: libXau6-32bit(x86-64)
Requires: libxcb1-32bit(x86-64)
Requires: libXcomposite1-32bit(x86-64)
Requires: libXcursor1-32bit(x86-64)
Requires: libXdamage1-32bit(x86-64)
Requires: libXinerama1-32bit(x86-64)
Requires: libXtst6-32bit(x86-64)
Requires: libXxf86vm1-32bit(x86-64)
%else
Requires: Mesa(x86-32)
Requires: mozilla-nss(x86-32)
Requires: libcurl4(x86-32) >= 7.16.2-1
Requires: libogg0(x86-32) >= 1.0
Requires: libpixman-1-0(x86-32) >= 0.24.4
Requires: libSDL-1_2-0(x86-32) >= 1.2.10
Requires: libSDL2-2_0-0(x86-32)
Requires: libtheora0(x86-32) >= 1.0
Requires: libvorbis0(x86-32) >= 1.1.2
Requires: glibc(x86-32) >= 2.15
Requires: libcairo2(x86-32) >= 1.6.0
Requires: cups-libs(x86-32) >= 1.4.0
Requires: libdbus-1-3(x86-32) >= 1.2.14
Requires: fontconfig(x86-32) >= 2.8.0
Requires: libfreetype6(x86-32) >= 2.3.9
Requires: libgcc47(x86-32) >= 4.1.1
Requires: libgcrypt11(x86-32) >= 1.4.5
Requires: libgdk_pixbuf-2_0-0(x86-32) >= 2.22.0
Requires: libglib-2_0-0(x86-32) >= 2.14.0
Requires: libgtk-2_0-0(x86-32) >= 2.24.0
Requires: mozilla-nspr(x86-32) >= 1.8.0.10
Requires: libopenal1-soft(x86-32) >= 1.13
Requires: libpango-1_0-0(x86-32) >= 1.22.0
Requires: libpulse0(x86-32) >= 0.99.1
Requires: libstdc++47(x86-32) >= 4.6
Requires: libX11-6(x86-32) >= 1.4.99.1
Requires: libXext6(x86-32)
Requires: libXfixes3(x86-32)
Requires: libXi6(x86-32) >= 1.2.99.4
Requires: libXrandr2(x86-32) >= 1.2.99.3
Requires: libXrender1(x86-32)
Requires: zlib(x86-32) >= 1.2.3.3
Requires: Mesa-libIndirectGL1(x86-32)
Requires: Mesa-libEGL1(x86-32)
Requires: libatk-1_0-0(x86-32)
Requires: libcares2(x86-32)
Requires: libasound2(x86-32)
Requires: libatk-1_0-0(x86-32)
Requires: libavahi-client3(x86-32)
Requires: libavahi-common3(x86-32)
Requires: libcom_err2(x86-32)
Requires: libdrm2(x86-32)
Requires: libexpat1(x86-32)
Requires: libffi47(x86-32)
Requires: libFLAC8(x86-32)
Requires: Mesa-libGL1(x86-32)
Requires: libgcrypt11(x86-32)
Requires: libgnutls28(x86-32)
Requires: libgpg-error0(x86-32)
Requires: libgsm1(x86-32)
Requires: krb5(x86-32)
Requires: libharfbuzz0(x86-32)
Requires: libICE6(x86-32)
Requires: libicu49(x86-32)
Requires: libjson0(x86-32)
Requires: libkeyutils1(x86-32)
Requires: libp11-kit0(x86-32)
Requires: libpcre1(x86-32)
Requires: libselinux1(x86-32)
Requires: libSM6(x86-32)
Requires: libsndfile1(x86-32)
Requires: libtasn1-3(x86-32)
Requires: libuuid1(x86-32)
Requires: tcpd(x86-32)
Requires: libXau6(x86-32)
Requires: libxcb1(x86-32)
Requires: libXcomposite1(x86-32)
Requires: libXcursor1(x86-32)
Requires: libXdamage1(x86-32)
Requires: libXinerama1(x86-32)
Requires: libXtst6(x86-32)
Requires: libXxf86vm1(x86-32)
%endif
%endif


%description
Steam Client for GNU/Linux

%prep
%setup -q -c -n %{name}

%build
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/
cp -fpr %_builddir/steam/* %{buildroot}
rm -rf %{buildroot}/etc/apt/
chmod +x %{buildroot}/usr/bin/steam
chmod +x %{buildroot}/usr/bin/steamdeps

%install
find %{buildroot} -not -type d -printf "/%%P\n" | sed '/\/man\//s/$/\*/' > manifest

%files -f manifest
