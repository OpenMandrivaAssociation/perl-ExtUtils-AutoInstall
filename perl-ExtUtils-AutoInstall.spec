%define real_name ExtUtils-AutoInstall

Summary:	ExtUtils::AutoInstall - Automatic install of dependencies via CPAN
Name:		perl-%{real_name}
Version:	0.63
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Sort-Versions
BuildRequires:	ncftp
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ExtUtils-AutoInstall module for perl

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%{__make}

%check
%{__make} test

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


