%define version          1.1.3
%define release          0
%define sourcename       check_procs_multi
%define packagename      nagios-plugins-check-procs-multi
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package %{nil}

Summary:   Nagios plugin similar to check_procs able to check several processes at once.
Name:      %{packagename}
Version:   %{version}
Obsoletes: check_procs_multi <= 100
Release:   %{release}%{?dist}
License:   GPLv3+
Packager:  Matteo Corti <matteo@corti.li>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:       https://github.com/matteocorti/%{sourcename}
Source:    https://github.com/matteocorti/%{sourcename}/releases/download/v%{version}/%{sourcename}-%{version}.tar.gz

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)

Requires:  nagios-plugins
Requires:  perl(File::Slurp)

%description
check_procs_multi is a Nagios plugin similar to check_procs able to
check several processes at once.

%prep
%setup -q -n %{sourcename}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor \
        INSTALLSCRIPT=%{nagiospluginsdir} \
        INSTALLVENDORSCRIPT=%{nagiospluginsdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.pod" -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS Changes NEWS README.md INSTALL  TODO COPYING COPYRIGHT VERSION
%{nagiospluginsdir}/%{sourcename}
%{_mandir}/man1/%{sourcename}.1*

%changelog
* Tue Jul  8 2025 Matteo Corti <matteo@corti..i> - 1.1.3-0%{?dist}
- Updated to 1.1.3

* Fri Jun 26 2020 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.2-1%{?dist}
- Added dependency to File::Slurp

* Thu Feb 10 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.2-0%{?dist}
- renamed to nagios-plugins-check-procs-multi

* Mon Jan 25 2010 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.1-0
- Updated to 1.1.1 + several spec file fixes 

* Tue Jul  7 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.0-0
- check with pgrep if ps fails

* Mon Jun 15 2009 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.1-0
- removed dep on Net::DNS

* Mon Jun  9 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.0-0
- grepping in perl

* Mon May 26 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.5-0
- fixed a bug when command name != proc name

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.4-0
- fixed the missing usage message

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.3-0
- ePN compatibility

* Tue Feb 12 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.2-0
- fixed a bug in the sanity checks

* Tue Feb 12 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.1-0
- version 0.9.1 (default min 1)

* Mon Feb 11 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.0-0
- Initial release
