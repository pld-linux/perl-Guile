#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Guile
Summary:	Guile perl module - a Perl binding to Guile interpreter
Summary(pl):	Modu³ perla Guile - dowi±zanie Perla do interpretera Guile
Name:		perl-Guile
Version:	0.001
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	4ea43e0435c44b93ddc91faec3f17b0a
Patch0:		%{name}-includes.patch
Patch1:		%{name}-warning.patch
BuildRequires:	guile-devel >= 1.5.0
BuildRequires:	perl-devel >= 5.6.1-66
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface to the GNU Guile system. Guile is an
interpreter for the Scheme programming language.

%description -l pl
Ten modu³ udostêpnia interfejs do systemu GNU Guile. Guile jest
interpterem jêzyka programowania Scheme.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Guile.pm
%{perl_vendorarch}/Guile
%dir %{perl_vendorarch}/auto/Guile
%dir %{perl_vendorarch}/auto/Guile/*
%{perl_vendorarch}/auto/Guile/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Guile/*/*.so
%{_mandir}/man3/*
