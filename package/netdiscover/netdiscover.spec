Name:           netdiscover
Version:        0.10
Release:        1.inari1
Summary:        A network address discovring/monitoring tool
Group:          Security/information-gathering
License:        GPLv3
URL:            https://netdiscover-scanner/netdiscover.git
Source0:        https://github.com/netdiscover-scanner/netdiscover/archive/refs/tags/0.10.tar.gz
BuildRequires:  libpcap-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  hwdata
BuildRequires:  libnet-devel >= 1.1.2

%description
Nerdiscover is an active/passive address reconnaissance tool, mainly developed for those wireless networks without dhcp server, when you are wardriving. It can be also used on hub/switched networks.

Built on top of libnet and libpcap, it can passively detect online hosts, or search for them, by actively sending arp request, it can also be used to inspect your network arp traffic, and find network address using auto scan mode, which will scan for common local networks.

%prep
%setup

%build
if [ ! -f configure ]
then
    ./autogen.sh
fi

%configure
make

%install
%makeinstall
rm -rf $RPM_BUILD_ROOT/usr/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS TODO COPYING README.md
%{_sbindir}/netdiscover
%dir %{_mandir}
%{_mandir}/*

%changelog
* Wed Nov 13 2024 Ghost <0x7ccghost@gmail.com> - 0.10.1-inari1
- Use netdiscover 0.10 from tag release
