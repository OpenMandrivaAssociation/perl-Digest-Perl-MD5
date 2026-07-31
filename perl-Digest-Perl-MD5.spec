%define upstream_name    Digest-Perl-MD5
%define upstream_version 1.91
%if %{_use_internal_dependency_generator}
%define __noautoreq '/bin/false'
%endif

Name:		perl-%{upstream_name}
Version:	1.91
Release:	24

Summary:	Perl implementation of Ron Rivests MD5 Algorithm
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}/
Source0:	https://cpan.metacpan.org/authors/id/D/DE/DELTA/Digest-Perl-MD5-1.91.tar.gz

BuildArch:	noarch
BuildRequires:	make
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
%setup -q -n Digest-Perl-MD5-1.91

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor 
%make OPTIMIZE="%{optflags}"

%check
make test || :

%install
%makeinstall_std

%files
%doc META.yml README.md
%{perl_vendorlib}/Digest
%{_mandir}/*/*

