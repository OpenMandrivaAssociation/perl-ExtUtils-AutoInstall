%define upstream_name    ExtUtils-AutoInstall
%define upstream_version 0.63

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	ExtUtils::AutoInstall - Automatic install of dependencies via CPAN
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		eai.patch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sort::Versions) >= 1.2
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(CPAN)
BuildRequires:	ncftp
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
ExtUtils-AutoInstall module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%{__make}

#check
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/ExtUtils/AutoInstall.pm
%{_mandir}/*/*
