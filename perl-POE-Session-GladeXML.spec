#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Session-GladeXML
Summary:	POE::Session::GladeXML - emit POE events for Gtk callbacks
Summary(pl):	POE::Session::GladeXML - wywo³ywanie zdarzeñ POE dla callbacków Gtk
Name:		perl-POE-Session-GladeXML
Version:	0.1.3
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27f4d1bc11e96b5705aeff0ae04b3850
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Gtk-GladeXML >= 0.7008
BuildRequires:	perl-POE >= 0.23
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple helper module that lets you connect callback names from your
.glade file with methods of an object. These methods are called as POE
postback methods.

%description -l pl
Prosty modu³ pomocniczy pozwalaj±cy na ³±czenie nazw callbacków z
pliku .glade z metodami obiektu. Te metody s± nazywane tak, jak metody
postback POE.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
