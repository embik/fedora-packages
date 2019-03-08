Name:		waybar
Version:	0.4.0
Release:	1%{?dist}
Summary:	Highly customizable Wayland bar for Sway and Wlroots based compositors.

Group:		User Interface/X
License:	MIT
URL:		https://github.com/Alexays/Waybar
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  git
BuildRequires:  make
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  libsigc++20-devel
BuildRequires:  fmt-devel
BuildRequires:  wayland-devel
BuildRequires:  wlroots-devel

Requires:       wlroots
Requires:       libnl3
Requires:       libdbusmenu-gtk3

Recommends:     sway

%description
Highly customizable Wayland bar for Sway and Wlroots based compositors.

%prep
%autosetup -p 1 -n Waybar-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/waybar
%{_sysconfdir}/xdg/waybar/*

%changelog
* Fri Mar 08 2019 Marvin Beckers <mail@embik.me> 0.4.0-1
- Initial package release
