Name:           fierce
Version:        1.6.0
Release:        1.inari1
Summary:        A DNS reconnaissance tool for locating non-contigous IP space
Group:          Security/information-gathering
License:        GPLv3
URL:            https://github.com/mschwager/fierce.git
Source0:        https://github.com/mschwager/fierce/archive/refs/tags/1.6.0.tar.gz
BuildArch:      noarch
Requires:       python3-requests
Requires:	python3-dns

%description
Fierce is a semi-lightweight scanner that helps locate non-contiguous IP space and hostnames against specified domains. It's really meant as a pre-cursor to nmap, unicornscan, nessus, nikto, etc, since all of those require that you already know what IP space you are looking for. This does not perform exploitation and does not scan the whole internet indiscriminately. It is meant specifically to locate likely targets both inside and outside a corporate network. Because it uses DNS primarily you will often find mis-configured networks that leak internal address space. That's especially useful in targeted malware

%prep
%setup -q -n %{name}-%{version}

%install
install -d -m 775 %{buildroot}%{_datadir}/%{name}
install -m 755 fierce/fierce.py %{buildroot}%{_datadir}/%{name}
install -m 755 fierce/__init__.py %{buildroot}%{_datadir}/%{name}
cp -pr fierce/lists %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/fierce << 'EOF'
#!/usr/bin/bash
cd %{_datadir}/%{name}
./fierce.py "$@"
EOF
chmod +x %{buildroot}%{_bindir}/fierce

find %{buildroot}%{_datadir}/%{name} -type f -name "*.py" -exec sed -i 's|/usr/bin/env python$|/usr/bin/python3|' {} +

%files
%{_datadir}/%{name}
%{_bindir}/%{name}

%changelog
* Tue Nov 12 2024 Ghost <0x7ccghost@gmail.com> - 1.3.1.1-inari1
- Initial package fierce 1.6.0 for Inari Linux
