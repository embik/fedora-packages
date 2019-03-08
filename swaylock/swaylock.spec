Name:		swaylock
Version:	1.3
Release:	1%{?dist}
Summary:	Screen locker for Wayland

Group:		User Interface/X
License:	MIT
URL:		https://github.com/swaywm/swaylock
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  git
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  libxkbcommon-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  scdoc
BuildRequires:  wayland-devel

Requires:       libxkbcommon
Requires:       cairo
Requires:       pam

%description
swaylock is a screen locking utility for Wayland compositors. It is compatible with any Wayland compositor which implements the following Wayland protocols:
- wlr-layer-shell
- wlr-input-inhibitor
- xdg-output
- xdg-shell

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
%{_sysconfdir}/pam.d/swaylock
%{_bindir}/swaylock
%{_mandir}/man1/swaylock.1*
%{_datadir}/bash-completion/completions/swaylock
%{_datadir}/zsh/site-functions/_swaylock
%exclude %{_datadir}/fish/completions/swaylock.fish

%changelog
* Fri Mar 08 2019 Marvin Beckers <mail@embik.me> 1.3-1
- Initial package release
