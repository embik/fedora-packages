Name:           libinput-gestures
Version:        2.50
Release:        1%{?dist}
Summary:        Actions gestures on your touchpad using libinput

License:        GPL-3
URL:            https://github.com/bulletmark/libinput-gestures
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python38
BuildRequires:  python3-flake8
Requires:       python38
Requires:       libinput

%description
Libinput-gestures is a utility which reads libinput gestures from your touchpad and maps them to gestures you configure in a configuration file. Each gesture can be configured to activate a shell command which is typically an xdotool command to action desktop/window/application keyboard combinations and commands.

%prep

%setup

%build

%install
install -p -D -m755 libinput-gestures %{buildroot}%{_bindir}/libinput-gestures
install -p -D -m644 libinput-gestures.conf %{buildroot}%{_sysconfdir}/libinput-gestures.conf

%check
flake8 libinput-gestures internal internal-test

%files
%doc README.md
%{_bindir}/libinput-gestures
%config %{_sysconfdir}/libinput-gestures.conf

%changelog
* Sat May 02 2020 Marvin Beckers <mail@embik.me> 2.50-1
- initial packaging with script and configuration file
