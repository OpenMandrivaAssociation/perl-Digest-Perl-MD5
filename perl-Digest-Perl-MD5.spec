%define upstream_name    Digest-Perl-MD5
%define upstream_version 1.8

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl implementation of Ron Rivests MD5 Algorithm
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/OLE/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	perl-devel

%description
This is not an interface (like Digest::MD5) but a Perl implementation of MD5. 
It is written in perl only and because of this it is slow but it works without 
C-Code. You should use Digest::MD5 instead of this module if it is available. 
This module is only useful for:
 *  computers where you cannot install Digest::MD5 (e.g. lack of a C-Compiler)
 *  encrypting only small amounts of data (less than one million bytes). 
    I use it to hash passwords.
 *  educational purposes


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make OPTIMIZE="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Digest
%{_mandir}/*/*
