Name:		alacritty
Version:	0.3.0
Release:	1%{?dist}
Summary:	A cross-platform, GPU enhanced terminal emulator

License:	ASL 2.0
URL:		https://github.com/jwilm/alacritty
Source0:	%{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:	freetype-devel
BuildRequires:  fontconfig-devel

Requires:       freetype
Requires:       fontconfig
Requires:       xclip

%description
Alacritty is the fastest terminal emulator in existence. Using the GPU for
rendering enables optimizations that simply aren't possible in other emulators.

%prep
%setup -qn %{name}-%{version}

%build
cargo build --release

%install
install -D -m755 target/release/%{name} %{buildroot}/%{_bindir}/%{name}
install -D -m644 extra/linux/alacritty.desktop %{buildroot}/%{_datadir}/applications/alacritty.desktop
install -D -m644 extra/completions/alacritty.bash %{buildroot}/%{_datadir}/bash-completion/completions/alacritty
install -D -m644 extra/completions/_alacritty %{buildroot}/%{_datadir}/zsh/site-functions/_alacritty
install -d -m755 %{buildroot}/%{_datadir}/%{name}
install -m644 alacritty*.yml %{buildroot}/%{_datadir}/%{name}
install -d -m755 %{buildroot}/%{_datadir}/terminfo/a
tic -o %{buildroot}/%{_datadir}/terminfo -xe alacritty,alacritty-direct extra/alacritty.info

%files
%doc README.md
%{_bindir}/alacritty
%{_datadir}/applications/alacritty.desktop
%{_datadir}/bash-completion/completions/alacritty
%{_datadir}/zsh/site-functions/_alacritty
%{_datadir}/%{name}/*.yml
%{_datadir}/terminfo/*

%changelog
* Tue Apr 09 2019 Marvin Beckers <mail@embik.me> 0.3.0-1
- Update to upstream release 0.3.0

* Fri Mar 08 2019 Marvin Beckers <mail@embik.me> 0.2.9-1
- Initial package version
