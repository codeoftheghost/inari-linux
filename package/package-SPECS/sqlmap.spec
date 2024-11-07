Name:           sqlmap
Version:        1.8.11
Release:        1inari
Summary:        Automatic SQL injection and database takeover tool
Group:          Security/database
License:        GPLv3
URL:            https://sqlmap.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        https://github.com/sqlmapproject/sqlmap/release/tag/%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-requests

%description
sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester, and a broad range of switches including database fingerprinting, over data fetching from the database, accessing the underlying file system, and executing commands on the operating system via out-of-band connections.

%prep
%autosetup

%install
install -d -m 775 %{buildroot}%{_datadir}/%{name}
install -m 755 sqlmap.py %{buildroot}%{_datadir}/%{name}
cp -pr extra %{buildroot}%{_datadir}/%{name}
cp -pr lib %{buildroot}%{_datadir}/%{name}
cp -pr plugins %{buildroot}%{_datadir}/%{name}
cp -pr data %{buildroot}%{_datadir}/%{name}
cp -pr thirdparty %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/sqlmap << 'EOF'
#!/bin/sh
cd %{_datadir}/%{name}
./sqlmap.py "$@"
EOF
chmod +x %{buildroot}%{_bindir}/sqlmap

install -d -m 755 %{buildroot}%{_sysconfdir}
install -m 644 sqlmap.conf %{buildroot}%{_sysconfdir}
pushd %{buildroot}%{_datadir}/%{name}
ln -s ../../..%{_sysconfdir}/sqlmap.conf .

%files
%doc doc/*
%{_datadir}/%{name}
%{_bindir}/%{name}
%condif(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Thu Nov 7 2024 Ghost <0x7ccghost@gmail.com> - 1.8.11.1-inari1
- Initial package sqlmap 1.8.11 for Inari Linux