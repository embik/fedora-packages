Name:   	grim
Version:	1.1
Release:	1%{?dist}
Summary:	Grab images from a Wayland compositor

Group:		User Interface/X
License:	MIT
URL:		https://github.com/emersion/grim
Source0:	%{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:  meson
BuildRequires:  make
BuildRequires:  scdoc
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)

Requires:	    cairo

Recommends:     sway
Recommends:     slurp

%description
Grab images from a Wayland compositor. Works great with slurp and with sway >= 1.0.

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
%{_bindir}/grim
%{_mandir}/man1/grim*.1*

%changelog
* Sun Mar 10 2019 Marvin Beckers <mail@embik.me> 1.1-1
- Initial package release
