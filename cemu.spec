%define oname Cemu
Summary:	Cemu is a Wii U emulator
Name:		cemu
Version:	2.1
Release:	1
Group:    Emulators/Games
License:	MPL-2.0
Group:		Emulators
Url:		https://cemu.info/
Source0:	https://github.com/cemu-project/Cemu/archive/v2.1/%{oname}-2.1.tar.gz

BuildRequires:  cmake
BuildRequires:  nasm
BuildRequires:  ninja
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(freeglut)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  cmake(glm)
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
BuildRequires:  cmake(glslang)
BuildRequires:  glslang
BuildRequires:  wxwidgets-devel
BuildRequires:  lib64usb1.0_0

%description
This is the code repository of Cemu, a Wii U emulator that is able to run most Wii U games and homebrew in a playable state. 
It's written in C/C++ and is being actively developed with new features and fixes to increase compatibility, convenience and usability.

Cemu is currently only available for 64-bit Windows and Linux devices.

#----------------------------------------------------------------------------

%prep
%autosetup -n %{oname}-2.1 -p1

%build
%cmake \
        -DENABLE_VCPKG=OFF \
        -DCMAKE_BUILD_TYPE=release

%make_build

%install
%make_install -C build

%files
