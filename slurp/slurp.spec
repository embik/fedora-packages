Name:		slurp
Version:	1.1.0
Release:	1%{?dist}
Summary:	Select a region in a Wayland compositor

Group:		User Interface/X
License:	MIT
URL:		https://github.com/emersion/slurp
Source0:	%{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:  meson
BuildRequires:  make
BuildRequires:  scdoc
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)

Requires:	    cairo

Recommends:     sway
Recommends:     grim

%description
Select a region in a Wayland compositor and print it to the standard output.

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
%{_bindir}/slurp
%{_mandir}/man1/slurp*.1*

%changelog
* Sun Mar 10 2019 Marvin Beckers <mail@embik.me> 1.1.0-1
- Initial package release
