%define version 0.9.1
%define release 0
%define name    check_procs_multi
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin that checks the available bandwidth
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires: perl

%description
check_procs_multi is a Nagios plugin similar to check_procs able to
check several processes at once.

%prep
%setup -q

%build
%__perl Makefile.PL  INSTALLSCRIPT=%{buildroot}%{_prefix} INSTALLSITEMAN1DIR=%{buildroot}/usr/share/man/man1
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS Changes NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/%{name}
%attr(0755, root, root) /usr/share/man/man1/%{name}.1.gz

%changelog
* Tue Feb 12 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.1-0
- version 0.9.1 (default min 1)

* Mon Feb 11 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.0-0
- Initial release
