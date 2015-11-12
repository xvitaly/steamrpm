Name: steam
Version: 1.0.0.50
Release: 1
Group: Applications/Games
Source: steam.tar.gz
Summary: Steam Client
URL: http://www.steampowered.com/
License: EULA
BuildRoot: %{_tmppath}/%{name}-root
Vendor: Valve

# Setting macro (taken from openSUSE official package)...
%define dep_postfix %{nil}
%ifarch x86_64
  %if 0%{?suse_version} || 0%{?sles_version}
    %define dep_postfix -32bit
  %endif
  %if 0%{?fedora} || 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
    %define dep_postfix (x86-32)
  %endif
%endif

# Distribution independent dependecies...
Requires: cups-libs%{dep_postfix} >= 1.4.0
Requires: fontconfig%{dep_postfix} >= 2.8.0
Requires: glibc%{dep_postfix} >= 2.15
Requires: openal-soft >= 1.13
Requires: zlib%{dep_postfix} >= 1.2.3.3

# Dependencies for Fedora/CentOS/RHEL (taken from SPEC by Tom Callaway <spot@fedoraproject.org>)...
%if 0%{?fedora} || 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
Requires: libcurl%{dep_postfix} >= 7.16.2-1
Requires: libogg%{dep_postfix} >= 1.0
Requires: pixman%{dep_postfix} >= 0.24.4
Requires: SDL%{dep_postfix} >= 1.2.10
Requires: libtheora%{dep_postfix} >= 1.0
Requires: libvorbis%{dep_postfix} >= 1.1.2
Requires: alsa-lib%{dep_postfix} >= 1.0.23
Requires: cairo%{dep_postfix} >= 1.6.0
Requires: dbus-libs%{dep_postfix} >= 1.2.14
Requires: freetype%{dep_postfix} >= 2.3.9
Requires: libgcc%{dep_postfix} >= 4.1.1
Requires: libgcrypt%{dep_postfix} >= 1.4.5
Requires: gdk-pixbuf2%{dep_postfix} >= 2.22.0
Requires: glib2%{dep_postfix} >= 2.14.0
Requires: gtk2%{dep_postfix} >= 2.24.0
Requires: nspr%{dep_postfix} >= 1.8.0.10
Requires: nss%{dep_postfix} >= 3.12.3
Requires: openal-soft%{dep_postfix} >= 1.13
Requires: pango%{dep_postfix} >= 1.22.0
Requires: pulseaudio-libs%{dep_postfix} >= 0.99.1
Requires: libstdc++%{dep_postfix} >= 4.6
Requires: libX11%{dep_postfix} >= 1.4.99.1
Requires: libXext%{dep_postfix}
Requires: libXfixes%{dep_postfix}
Requires: libXi%{dep_postfix} >= 1.2.99.4
Requires: libXrandr%{dep_postfix} >= 1.2.99.3
Requires: libXrender%{dep_postfix}
Requires: mesa-dri-drivers%{dep_postfix}
Requires: libasyncns%{dep_postfix}
Requires: atk%{dep_postfix}
Requires: avahi-libs%{dep_postfix}
Requires: libcom_err%{dep_postfix}
Requires: libdrm%{dep_postfix}
Requires: mesa-libEGL%{dep_postfix}
Requires: expat%{dep_postfix}
Requires: libffi%{dep_postfix}
Requires: mesa-libGL%{dep_postfix}
Requires: libgcrypt%{dep_postfix}
Requires: gnutls%{dep_postfix}
Requires: libgpg-error%{dep_postfix}
Requires: gsm%{dep_postfix}
Requires: krb5-libs%{dep_postfix}
Requires: harfbuzz%{dep_postfix}
Requires: libICE%{dep_postfix}
Requires: libicu%{dep_postfix}
Requires: json-c%{dep_postfix}
Requires: keyutils-libs%{dep_postfix}
Requires: p11-kit%{dep_postfix}
Requires: pcre%{dep_postfix}
Requires: libselinux%{dep_postfix}
Requires: libSM%{dep_postfix}
Requires: libsndfile%{dep_postfix}
Requires: libtasn1%{dep_postfix}
Requires: libuuid%{dep_postfix}
Requires: tcp_wrappers-libs%{dep_postfix}
Requires: libXau%{dep_postfix}
Requires: libxcb%{dep_postfix}
Requires: libXcomposite%{dep_postfix}
Requires: libXcursor%{dep_postfix}
Requires: libXdamage%{dep_postfix}
Requires: libXinerama%{dep_postfix}
Requires: libXtst%{dep_postfix}
Requires: libXxf86vm%{dep_postfix}
Requires: SDL2%{dep_postfix}
Requires: DevIL%{dep_postfix}
Requires: SDL_mixer%{dep_postfix}
%if 0%{?fedora} >= 18
Requires: libpng12%{dep_postfix} >= 1.2.13
Requires: systemd-libs%{dep_postfix}
%else
Requires: libudev%{dep_postfix}
%endif
%if 0%{?fedora} == 17
Requires: libpng-compat%{dep_postfix} >= 1.2.13
Requires: flac%{dep_postfix}
%endif
%if 0%{?fedora} <= 16
Requires: libpng >= 1.2.13
%endif
%if 0%{?fedora} >= 17
Requires: mesa-libgbm%{dep_postfix}
Requires: mesa-libglapi%{dep_postfix}
Requires: libwayland-client%{dep_postfix}
Requires: libwayland-server%{dep_postfix}
%endif
%endif

# Dependencies for openSUSE and SLES...
%if 0%{?suse_version} || 0%{?sles_version}
Requires: Mesa-libGL1%{dep_postfix}
Requires: alsa%{dep_postfix} >= 1.0.23
Requires: alsa-devel%{dep_postfix} >= 1.0.23
Requires: dbus-1-glib%{dep_postfix}
Requires: gtk2-engine-oxygen%{dep_postfix}
Requires: libSDL-1_2-0%{dep_postfix} >= 1.2.10
Requires: libX11-6%{dep_postfix} >= 1.4.99.1
Requires: libXdmcp6%{dep_postfix}
Requires: libXext6%{dep_postfix}
Requires: libXfixes3%{dep_postfix}
Requires: libXi6%{dep_postfix} >= 1.2.99.4
Requires: libXrandr2%{dep_postfix} >= 1.2.99.3
Requires: libXrender1%{dep_postfix}
Requires: libatk-1_0-0%{dep_postfix}
Requires: libcairo2%{dep_postfix} >= 1.6.0
Requires: libcurl4%{dep_postfix} >= 7.16.2-1
Requires: libdbus-1-3%{dep_postfix} >= 1.2.14
Requires: libfreetype6%{dep_postfix} >= 2.3.9
%if 0%{?suse_version} >= 1320
Requires: libgcrypt20%{dep_postfix} >= 1.6.1
%else
Requires: libgcrypt11%{dep_postfix} >= 1.4.5
%endif
Requires: libgdk_pixbuf-2_0-0%{dep_postfix} >= 2.22.0
Requires: libglib-2_0-0%{dep_postfix} >= 2.14.0
Requires: libgmodule-2_0-0%{dep_postfix}
Requires: libgobject-2_0-0%{dep_postfix}
Requires: libgtk-2_0-0%{dep_postfix} >= 2.24.0
Requires: libnm-glib4%{dep_postfix}
Requires: libnm-util2%{dep_postfix}
Requires: libogg0%{dep_postfix} >= 1.0
Requires: libpango-1_0-0%{dep_postfix} >= 1.22.0
Requires: libpixman-1-0%{dep_postfix} >= 0.24.4
Requires: libpng12-0%{dep_postfix} >= 1.2.13
Requires: libpulse0%{dep_postfix} >= 0.99.1
Requires: libtheora0%{dep_postfix} >= 1.0
Requires: libvorbis0%{dep_postfix} >= 1.1.2
Requires: mozilla-nspr%{dep_postfix} >= 1.8.0.10
Requires: mozilla-nss%{dep_postfix} >= 3.12.3
Requires: cups-libs%{dep_postfix} >= 1.4.0
Requires: fontconfig%{dep_postfix} >= 2.8.0
Requires: glibc%{dep_postfix} >= 2.15
Requires: openal-soft >= 1.13
Requires: zlib%{dep_postfix} >= 1.2.3.3
# openSUSE 12.3 changed the name of some libs
%if 0%{?suse_version} >= 1230
Requires: libgcc_s1%{dep_postfix} >= 4.1.1
Requires: libopenal1%{dep_postfix} >= 1.13
Requires: libstdc++6%{dep_postfix} >= 4.6
%endif
%if 0%{?suse_version} < 1230
Requires: libgcc47%{dep_postfix} >= 4.1.1
Requires: libopenal1-soft%{dep_postfix} >= 1.13
Requires: libstdc++47%{dep_postfix} >= 4.6
%endif
Requires: curl
Requires: xz
Requires: zenity
Requires: libxcb-dri2-0%{dep_postfix}
Requires: libxcb-glx0%{dep_postfix}
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
rm -f %{buildroot}/usr/bin/steamdeps
chmod +x %{buildroot}/usr/bin/steam
find %{buildroot} -not -type d -printf "/%%P\n" | sed '/\/man\//s/$/\*/' > manifest

%files -f manifest
%defattr(-,root,root)

%changelog
* Thu Oct 08 2015 V1TSK <vitaly@easycoding.org>
- Updated to latest Steam version (r50). Updated deps.

* Sat Dec 27 2014 V1TSK <vitaly@easycoding.org>
- Updated to latest Steam version (r49).

* Mon Aug 18 2014 V1TSK <vitaly@easycoding.org>
- Updated to latest Steam version (r48).

* Wed Nov 06 2013 V1TSK <vitaly@easycoding.org>
- Updated to latest Steam version (r43).

* Fri Jul 26 2013 V1TSK <vitaly@easycoding.org>
- Updated to latest Steam version. Fixed build under new versions of Fedora and openSUSE.
