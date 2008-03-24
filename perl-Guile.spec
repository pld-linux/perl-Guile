#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Guile
Summary:	Guile Perl module - a Perl binding to Guile interpreter
Summary(pl.UTF-8):	Moduł Perla Guile - dowiązanie Perla do interpretera Guile
Name:		perl-Guile
Version:	0.002
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Guile/%{pdir}-%{version}.tar.gz
# Source0-md5:	2bbb0979d1ab4c208e9614fb35496b0f
Patch0:		%{name}-includes.patch
Patch1:		%{name}-warning.patch
Patch2:		%{name}-types.patch
URL:		http://search.cpan.org/dist/Guile/
BuildRequires:	guile-devel >= 1.5.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface to the GNU Guile system. Guile is an
interpreter for the Scheme programming language.

%description -l pl.UTF-8
Ten moduł udostępnia interfejs do systemu GNU Guile. Guile jest
interpreterem języka programowania Scheme.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

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
