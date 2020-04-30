%global srcname pywal

Name:       python-%{srcname}
Version:    3.3.0
Release:    1%{?dist}
Summary:    Generate and change color-schemes on the fly.

License:    MIT
URL:        https://pypi.python.org/pypi/pywal
Source0:    %{pypi_source}

BuildArch:  noarch

%global _description %{expand:
Pywal is a tool that generates a color palette from the dominant colors in an image. It then applies the colors system-wide and on-the-fly in all of your favourite programs.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       GraphicsMagick
Requires:       procps-ng

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/wal

%changelog
* Thu Apr 30 2020 Marvin Beckers <mail@embik.me> 3.3.0-1
- Initial packaging based on Fedora python guidelines
