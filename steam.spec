Name: steam
Version: 1.0.22
Release: 1
Group: Applications/Games
BuildArch: noarch
Source: steam.tar.gz
Summary: Steam Client
URL: http://www.steampowered.com/
License: EULA
BuildRoot: %{_tmppath}/%{name}-root
Vendor: Valve

# Dependencies taken from SPEC by Tom Callaway <spot@fedoraproject.org>
%if 0%{?fedora_version}
Requires: libjpeg-turbo(x86-32)
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
Requires: mesa-libgbm(x86-32)
Requires: mesa-libglapi(x86-32)
Requires: systemd-libs(x86-32)
Requires: libwayland-client(x86-32)
Requires: libwayland-server(x86-32)
%endif
%if 0%{?fedora} == 17
Requires: libpng-compat(x86-32) >= 1.2.13
Requires: mesa-libgbm(x86-32)
Requires: mesa-libglapi(x86-32)
Requires: libudev(x86-32)
Requires: libwayland-client(x86-32)
Requires: libwayland-server(x86-32)
%endif
%if 0%{?fedora} <= 16
Requires: libpng >= 1.2.13
Requires: libudev(x86-32)
%endif
%endif

%if 0%{?suse_version}
%ifarch x86_64
Requires: Mesa-32bit
Requires: mozilla-nss-32bit
Requires: libcurl4-32bit >= 7.16.2-1
Requires: libogg0-32bit >= 1.0
Requires: libpixman-1-0-32bit >= 0.24.4
Requires: libSDL-1_2-0-32bit >= 1.2.10
Requires: libSDL2-2_0-0-32bit
Requires: libtheora0-32bit >= 1.0
Requires: libvorbis0-32bit >= 1.1.2
Requires: glibc-32bit >= 2.15
Requires: libcairo2-32bit >= 1.6.0
Requires: cups-libs-32bit >= 1.4.0
Requires: libdbus-1-3-32bit >= 1.2.14
Requires: fontconfig-32bit >= 2.8.0
Requires: libfreetype6-32bit >= 2.3.9
Requires: libgcc47-32bit >= 4.1.1
Requires: libgcrypt11-32bit >= 1.4.5
Requires: libgdk_pixbuf-2_0-0-32bit >= 2.22.0
Requires: libglib-2_0-0-32bit >= 2.14.0
Requires: libgtk-2_0-0-32bit >= 2.24.0
Requires: mozilla-nspr-32bit >= 1.8.0.10
Requires: libopenal1-soft-32bit >= 1.13
Requires: libpango-1_0-0-32bit >= 1.22.0
Requires: libpulse0-32bit >= 0.99.1
Requires: libstdc++47-32bit >= 4.6
Requires: libX11-6-32bit >= 1.4.99.1
Requires: libXext6-32bit
Requires: libXfixes3-32bit
Requires: libXi6-32bit >= 1.2.99.4
Requires: libXrandr2-32bit >= 1.2.99.3
Requires: libXrender1-32bit
Requires: zlib-32bit >= 1.2.3.3
Requires: Mesa-libIndirectGL1-32bit
Requires: Mesa-libEGL1-32bit
Requires: libcares2-32bit
Requires: libasound2-32bit
Requires: libatk-1_0-0-32bit
Requires: libavahi-client3-32bit
Requires: libavahi-common3-32bit
Requires: libcom_err2-32bit
Requires: libdrm2-32bit
Requires: libexpat1-32bit
Requires: libffi47-32bit
Requires: libFLAC8-32bit
Requires: Mesa-libGL1-32bit
Requires: libgcrypt11-32bit
Requires: libgnutls28-32bit
Requires: libgpg-error0-32bit
Requires: libgsm1-32bit
Requires: krb5-32bit
Requires: libharfbuzz0-32bit
Requires: libICE6-32bit
Requires: libicu49-32bit
Requires: libjson0-32bit
Requires: libkeyutils1-32bit
Requires: libp11-kit0-32bit
Requires: libpcre1-32bit
Requires: libselinux1-32bit
Requires: libSM6-32bit
Requires: libsndfile1-32bit
Requires: libtasn1-3-32bit
Requires: libuuid1-32bit
Requires: tcpd-32bit
Requires: libXau6-32bit
Requires: libxcb1-32bit
Requires: libXcomposite1-32bit
Requires: libXcursor1-32bit
Requires: libXdamage1-32bit
Requires: libXinerama1-32bit
Requires: libXtst6-32bit
Requires: libXxf86vm1-32bit
%else
Requires: Mesa
Requires: mozilla-nss
Requires: libcurl4 >= 7.16.2-1
Requires: libogg0 >= 1.0
Requires: libpixman-1-0 >= 0.24.4
Requires: libSDL-1_2-0 >= 1.2.10
Requires: libSDL2-2_0-0
Requires: libtheora0 >= 1.0
Requires: libvorbis0 >= 1.1.2
Requires: glibc >= 2.15
Requires: libcairo2 >= 1.6.0
Requires: cups-libs >= 1.4.0
Requires: libdbus-1-3 >= 1.2.14
Requires: fontconfig >= 2.8.0
Requires: libfreetype6 >= 2.3.9
Requires: libgcc47 >= 4.1.1
Requires: libgcrypt11 >= 1.4.5
Requires: libgdk_pixbuf-2_0-0 >= 2.22.0
Requires: libglib-2_0-0 >= 2.14.0
Requires: libgtk-2_0-0 >= 2.24.0
Requires: mozilla-nspr >= 1.8.0.10
Requires: libopenal1-soft >= 1.13
Requires: libpango-1_0-0 >= 1.22.0
Requires: libpulse0 >= 0.99.1
Requires: libstdc++47 >= 4.6
Requires: libX11-6 >= 1.4.99.1
Requires: libXext6-32bit
Requires: libXfixes3-32bit
Requires: libXi6 >= 1.2.99.4
Requires: libXrandr2 >= 1.2.99.3
Requires: libXrender1
Requires: zlib >= 1.2.3.3
Requires: Mesa-libIndirectGL1
Requires: Mesa-libEGL1
Requires: libatk-1_0-0
Requires: libcares2
Requires: libasound2
Requires: libatk-1_0-0
Requires: libavahi-client3
Requires: libavahi-common3
Requires: libcom_err2
Requires: libdrm2
Requires: libexpat1
Requires: libffi47
Requires: libFLAC8
Requires: Mesa-libGL1
Requires: libgcrypt11
Requires: libgnutls28
Requires: libgpg-error0
Requires: libgsm1
Requires: krb5
Requires: libharfbuzz0
Requires: libICE6
Requires: libicu49
Requires: libjson0
Requires: libkeyutils1
Requires: libp11-kit0
Requires: libpcre1
Requires: libselinux1
Requires: libSM6
Requires: libsndfile1
Requires: libtasn1-3
Requires: libuuid1
Requires: tcpd
Requires: libXau6
Requires: libxcb1
Requires: libXcomposite1
Requires: libXcursor1
Requires: libXdamage1
Requires: libXinerama1
Requires: libXtst6
Requires: libXxf86vm1
%endif
Requires: libjpeg-turbo
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
