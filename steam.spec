Name: steam
Version: 0.1
Release: 2
Group: Applications/Games
BuildArch: noarch
Source: steam.tar.gz
Summary: Steam Client
URL: http://www.steampowered.com/
License: EULA
Vendor: Valve

# Dependencies taken from SPEC by Tom Callaway <spot@fedoraproject.org>
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
%if 0%{?fedora} >= 18
Requires: libpng12(x86-32) >= 1.2.13
%endif
%if 0%{?fedora} == 17
Requires: libpng-compat(x86-32) >= 1.2.13
%endif
%if 0%{?fedora} <= 16
Requires: libpng >= 1.2.13
%endif
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
%if 0%{?fedora} >= 17
Requires: mesa-libgbm(x86-32)
Requires: mesa-libglapi(x86-32)
%endif
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
%if 0%{?fedora} >= 18
Requires: systemd-libs(x86-32)
%else
Requires: libudev(x86-32)
%endif
Requires: libuuid(x86-32)
%if 0%{?fedora} >= 17
Requires: libwayland-client(x86-32)
Requires: libwayland-server(x86-32)
%endif
Requires: tcp_wrappers-libs(x86-32)
Requires: libXau(x86-32)
Requires: libxcb(x86-32)
Requires: libXcomposite(x86-32)
Requires: libXcursor(x86-32)
Requires: libXdamage(x86-32)
Requires: libXinerama(x86-32)
Requires: libXtst(x86-32)
Requires: libXxf86vm(x86-32)
%if 0%{?suse_version}
Requires: SDL2(x86-32)
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
cp -r %{buildroot} /tmp/buildcpy

%install
cp -r /tmp/buildcpy/* %{buildroot}
find %{buildroot} -not -type d -printf "/%%P\n" | sed '/\/man\//s/$/\*/' > manifest
rm -rf /tmp/buildcpy

%files -f manifest
