Name:           scdoc
Version:        1.9.4
Release:        2%{?dist}
Summary:        Tool for generating roff manual pages
License:        MIT
URL:            https://git.sr.ht/~sircmpwn/%{name}
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  sed

%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep
%setup -q

# Disable static linking
sed -i '/-static/d' Makefile

# Fix 'harcoded' installation path
sed -i 's/DESTDIR=/DESTDIR?=/g' Makefile
sed -i 's/PREFIX=/PREFIX?=/g' Makefile

# Fix 'hardcoded' CFLAGS
sed -i 's/CFLAGS=/CFLAGS+=/g' Makefile

# Use INSTALL provided by the make_install macro
sed -i 's/\tinstall/\t$(INSTALL)/g' Makefile

# Use lib64
sed -i 's/\/lib\/pkgconfig/\/lib64\/pkgconfig/g' Makefile

%build
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%check
make check

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man5/%{name}.5.gz
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Mar 8 2019 Marvin Beckers <mail@embik.me> - 1.9.4-2
- Install pkgconfig to lib64

* Thu Mar 7 2019 Marvin Beckers <mail@embik.me> - 1.9.4-1
- New release

* Sat Oct 14 2018 Sergey Korolev <korolev.srg@gmail.com> - 1.5.1-1
- New release

* Tue Aug 7 2018 Marcin Skarbek <rpm@skarbek.name> - 1.4.1-1
- New release

* Tue Jun 19 2018 Marcin Skarbek <rpm@skarbek.name> - 1.3.4-1
- New release

* Wed May 23 2018 Marcin Skarbek <rpm@skarbek.name> - 1.3.3-1
- Initial package
