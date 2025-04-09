%undefine _debugsource_packages

%define oname Cemu
Summary:	Cemu is a Wii U emulator
Name:		cemu
Version:	2.6
Release:	1
Group:		Emulators/Games
License:	MPL-2.0
Url:		https://cemu.info/
Source0:	https://github.com/cemu-project/Cemu/archive/refs/tags/v%{version}.tar.gz
# Pulled in as git submodules upstream.
# Check gitweb for correct versions.
Source1:	https://github.com/Exzap/ZArchive/archive/d2c717730092c7bf8cbb033b12fd4001b7c4d932.tar.gz#/zarchive.tar.gz
Source2:	https://github.com/ocornut/imgui/archive/f65bcf481ab34cd07d3909aab1479f409fa79f2f.tar.gz#/imgui.tar.gz
BuildRequires:  cmake
BuildRequires:  nasm
BuildRequires:  ninja
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(freeglut)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  cmake(glm)
BuildRequires:	cmake(hidapi)
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  cmake(glslang)
BuildRequires:  glslang
BuildRequires:  wxwidgets-devel
BuildRequires:  %{_lib}usb1.0_0
BuildRequires:  %{_lib}zstd-static-devel

BuildSystem:	cmake
BuildOption:	-DENABLE_VCPKG:BOOL=OFF
BuildOption:	-DBUILD_SHARED_LIBS:BOOL=OFF
BuildOption:	-DBUILD_STATIC_LIBS:BOOL=ON
BuildOption:	-DENABLE_CUBEB:BOOL=OFF

%patchlist
cemu-2.1-fix-build-without-cubeb.patch
https://github.com/cemu-project/Cemu/pull/1455.patch

%description
This is the code repository of Cemu, a Wii U emulator that is able to run most Wii U games and homebrew in a playable state. 
It's written in C/C++ and is being actively developed with new features and fixes to increase compatibility, convenience and usability.

Cemu is currently only available for 64-bit Windows and Linux devices.

#----------------------------------------------------------------------------

%prep
%autosetup -n %{oname}-%{version} -p1
cd dependencies
rm -rf ZArchive imgui
tar xf %{S:1}
mv ZArchive-* ZArchive
tar xf %{S:2}
mv imgui-* imgui

%install -a
# There's no install target -- so we have to do it manually

mkdir -p %{buildroot}%{_libdir}/%{name} %{buildroot}%{_bindir}
mv bin/Cemu_* %{buildroot}%{_libdir}/%{name}/Cemu
mv bin/{resources,gameProfiles} %{buildroot}%{_libdir}/%{name}/
cat >%{buildroot}%{_bindir}/Cemu <<'EOF'
#!/bin/sh
cd %{_libdir}/%{name}
exec ./Cemu "$@"
EOF
chmod +x %{buildroot}%{_bindir}/Cemu
mkdir -p %{buildroot}%{_datadir}/applications
mv dist/linux/info.cemu.Cemu.desktop %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
mv dist/linux/info.cemu.Cemu.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
mkdir -p %{buildroot}%{_datadir}/metainfo
mv dist/linux/info.cemu.Cemu.metainfo.xml %{buildroot}%{_datadir}/metainfo/

%files
%{_bindir}/Cemu
%{_libdir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*/*/*/*
%{_datadir}/metainfo/*.metainfo.xml
