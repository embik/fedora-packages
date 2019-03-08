Name:		swayidle
Version:	1.2
Release:	1%{?dist}
Summary:	Idle management daemon for Wayland

Group:		User Interface/X
License:	MIT
URL:		https://github.com/swaywm/swayidle
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  git
BuildRequires:  make
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  scdoc
BuildRequires:  wayland-devel

Recommends:     sway
Recommends:     swaylock

%description
This is sway's idle management daemon, swayidle. It is compatible with any Wayland compositor which implements the KDE idle protocol.

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
%{_bindir}/swayidle
%{_mandir}/man1/swayidle.1*
%{_datadir}/bash-completion/completions/swayidle
%{_datadir}/zsh/site-functions/_swayidle
%exclude %{_datadir}/fish/completions/swayidle.fish

%changelog
* Fri Mar 08 2019 Marvin Beckers <mail@embik.me> 1.2-1
- Initial package release
