%define upstream_name    ExtUtils-AutoInstall
%define upstream_version 0.63

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	ExtUtils::AutoInstall - Automatic install of dependencies via CPAN
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		eai.patch

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Sort::Versions) >= 1.2
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(CPAN)
BuildRequires:	ncftp
BuildArch:	noarch

%description
ExtUtils-AutoInstall module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
make

#check
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/ExtUtils/AutoInstall.pm
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.630.0-1mdv2010.0
+ Revision: 407034
- rebuild using %%perl_convert_version

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.63-5mdv2009.0
+ Revision: 289486
- sync with fedora
- disable the tests for now

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.63-2mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.63-2mdv2007.0
+ Revision: 108540
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-ExtUtils-AutoInstall

* Tue Sep 27 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.63-1mdk
- 0.63

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.62-1mdk
- initial Mandriva package

