Name:    janus-gateway
Version: 0.2.5.1
Release: 1%{?dist}
Summary: General purpose WebRTC gateway
Group: Network
License: GPLv2
Source0: https://github.com/meetecho/janus-gateway/archive/v0.2.5.tar.gz
Source1: janus-gateway.service
BuildRequires: libmicrohttpd-devel, jansson-devel, openssl-devel, libsrtp15-devel, glib-devel, opus-devel, libogg-devel, libcurl-devel, pkgconfig, gengetopt, libtool, autoconf, automake, libwebsockets-devel, doxygen, graphviz
BuildRequires: sofia-sip
BuildRequires: libnice-devel >= 0.1.4
Requires: libmicrohttpd, jansson, openssl, glib, sofia-sip libwebsockets
Requires: libsrtp15
Requires: libnice >= 0.1.4
%description
Janus is an open source, general purpose, WebRTC gateway designed and developed by Meetecho.

%prep
%autosetup -n janus-gateway-0.2.5

%build
./autogen.sh
./configure --prefix=/opt/janus
make

%install
DESTDIR=%buildroot make install
DESTDIR=%buildroot make configs
mkdir -p  %{buildroot}%{_unitdir}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/janus-gateway.service

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) /opt/janus/etc/janus/*
%doc /opt/janus/share/doc/*
%doc /opt/janus/share/man/*
/opt/janus/share/janus/
/opt/janus/bin
/opt/janus/include
/opt/janus/lib
%{_unitdir}/janus-gateway.service

%changelog
* Thu Mar 08 2018 Stefano Fancello <stefano.fancello@nethesis.it> - 0.2.5.1-1
- janus-gateway: Janus doesn't try to restart if it fails - Bug NethServer/dev#5426

* Mon Nov 20 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.2.5-1
- janus-gateway ignores rtp_port_range option - Bug NethServer/dev#5374


