Name:           wsmancli
Version:        2.2.3
Release:        1%{?dist}
License:        BSD
Url:            http://www.openwsman.org/
Source:         http://downloads.sourceforge.net/project/openwsman/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:        COPYING
Source2:        README
Source3:        AUTHORS
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXXX)
Group:          Applications/System
BuildRequires:  openwsman-devel >= 2.1.0 pkgconfig curl-devel
Requires:       openwsman curl
Summary:        WS-Management-Command line Interface

%description
Command line interface for managing 
systems using Web Services Management protocol.

%prep
%setup -q
cp -fp %SOURCE1 %SOURCE2 %SOURCE3 .;

%build
%configure --disable-more-warnings 
make %{?_smp_flags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/wsman
%{_bindir}/wseventmgr
%doc COPYING README AUTHORS

%changelog
* Mon Mar 15 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.3-1
- Update to wsmancli-2.1.3
- Fix dist tag

* Thu Jan 14 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.0-5
- Use tarball from upstream
- Add COPYING, README and AUTHORS to sources (previously placed in the, probably modified, tarball)

* Wed Jan 13 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.0-4
- Fix Source

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.1.0-3.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 30 2008  <srinivas_ramanatha@dell.com> - 2.1.0-1%{?dist}
- Modified the spec file to adhere to fedora packaging guidelines.

