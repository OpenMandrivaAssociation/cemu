%define oname Cemu
Summary:	Cemu is a Wii U emulator
Name:		cemu
Version:	2.0
Release:	1
Group:    Emulators/Games
License:	MPL-2.0
Group:		Emulators
Url:		https://cemu.info/
Source0:	https://github.com/cemu-project/Cemu/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  nasm
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(freeglut)

%description
This is the code repository of Cemu, a Wii U emulator that is able to run most Wii U games and homebrew in a playable state. 
It's written in C/C++ and is being actively developed with new features and fixes to increase compatibility, convenience and usability.

Cemu is currently only available for 64-bit Windows and Linux devices.

#----------------------------------------------------------------------------

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_C_COMPILER=/usr/bin/clang-14 -DCMAKE_CXX_COMPILER=/usr/bin/clang++-14

%make_build

%install
%make_install -C build

%files
