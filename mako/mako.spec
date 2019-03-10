Name:       mako
Version:	1.2
Release:	1%{?dist}
Summary:	A lightweight Wayland notification daemon

Group:		User Interface/X
License:	MIT
URL:		https://github.com/emersion/mako
Source0:	%{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  make
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)

Requires:	    cairo
Requires:       pango

%description
A lightweight notification daemon for Wayland.

%prep
%autosetup -p 1 -n %{name}-%{version}
mkdir %{_target_Platform}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/mako*
%{_mandir}/man1/mako*.1*

%changelog
* Sun Mar 10 2019 Marvin Beckers <mail@embik.me> 1.2-1
- Initial package release
