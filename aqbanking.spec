#
# Conditional build:
%bcond_without	static_libs	# static libraries

%define	gwenhywfar_ver	5.5.1.1
Summary:	A library for online banking functions and financial data import/export
Summary(pl.UTF-8):	Biblioteka do funkcji bankowych online oraz importu/eksportu danych finansowych
Name:		aqbanking
Version:	6.3.2
Release:	2
License:	GPL v2 or GPL v3
Group:		Libraries
# https://www.aquamaniac.de/sites/download/packages.php?showall=1
Source0:	https://www.aquamaniac.de/rdm/attachments/download/386/%{name}-%{version}.tar.gz
# Source0-md5:	a96307ed3b144fb799af87ed0e2c6225
URL:		https://www.aquamaniac.de/sites/aqbanking/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gmp-devel
BuildRequires:	gwenhywfar-devel >= %{gwenhywfar_ver}
BuildRequires:	ktoblzcheck-devel >= 1.10
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 2
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	which
BuildRequires:	xmlsec1-gnutls-devel >= 1.0.0
Requires:	gwenhywfar >= %{gwenhywfar_ver}
Requires:	ktoblzcheck >= 1.10
Obsoletes:	aqbanking-backend-aqdtaus
Obsoletes:	aqbanking-backend-aqdtaus-devel
Obsoletes:	aqbanking-backend-aqdtaus-static
Obsoletes:	aqbanking-backend-aqebics-devel < 6.0
Obsoletes:	aqbanking-backend-aqebics-static < 6.0
Obsoletes:	aqbanking-backend-aqgeldkarte
Obsoletes:	aqbanking-backend-aqgeldkarte-devel
Obsoletes:	aqbanking-backend-aqgeldkarte-static
Obsoletes:	aqbanking-backend-aqhbci-devel < 6.0
Obsoletes:	aqbanking-backend-aqhbci-static < 6.0
Obsoletes:	aqbanking-backend-aqofxconnect-devel < 6.0
Obsoletes:	aqbanking-backend-aqofxconnect-static < 6.0
Obsoletes:	aqbanking-backend-aqpaypal
Obsoletes:	aqbanking-backend-aqyellownet
Obsoletes:	aqbanking-backend-aqyellownet-devel
Obsoletes:	aqbanking-backend-aqyellownet-static
Obsoletes:	aqbanking-c++ < 6.0
Obsoletes:	aqbanking-c++-devel < 6.0
Obsoletes:	aqbanking-c++-static < 6.0
Obsoletes:	aqbanking-frontend-cbanking
Obsoletes:	aqbanking-frontend-cbanking-devel
Obsoletes:	aqbanking-frontend-cbanking-static
Obsoletes:	aqbanking-frontend-fbanking
Obsoletes:	aqbanking-frontend-fbanking-devel
Obsoletes:	aqbanking-frontend-fbanking-static
Obsoletes:	aqbanking-frontend-g2banking
Obsoletes:	aqbanking-frontend-g2banking-devel
Obsoletes:	aqbanking-frontend-g2banking-static
Obsoletes:	aqbanking-frontend-kbanking
Obsoletes:	aqbanking-frontend-kbanking-devel
Obsoletes:	aqbanking-frontend-kbanking-static
Obsoletes:	aqbanking-frontend-qbanking
Obsoletes:	aqbanking-frontend-qbanking-devel
Obsoletes:	aqbanking-frontend-qbanking-static
Obsoletes:	python-aqbanking
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%description -l pl.UTF-8
Celem projektu AqBanking jest dostarczenie warstwy pośredniej między
programem a różnymi bibliotekami usług bankowych online (np. AqHBCI).
Pierwszy, już obsługiwany backend to AqHBCI - biblioteka
implementująca klienta niemieckiego protokołu HBCI (Home Baking
Computer Interface). Ponadto Aqbanking dostarcza różne wtyczki
upraszczające importowanie i eksportowanie danych finansowych.
Aktualnie istnieją wtyczki do importu następujących formatów: DTAUS
(niemiecki format finansowy), SWIFT (MT940 oraz MT942).

%package devel
Summary:	Header files for AqBanking library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AqBanking
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gwenhywfar-devel >= %{gwenhywfar_ver}

%description devel
Header files for AqBanking library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AqBanking.

%package static
Summary:	Static AqBanking libraries
Summary(pl.UTF-8):	Statyczne biblioteki AqBanking
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AqBanking libraries.

%description static -l pl.UTF-8
Statyczne biblioteki AqBanking.

%package backend-aqebics
Summary:	AqEBICS backend for AqBanking library
Summary(pl.UTF-8):	Backend AqEBICS dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xmlsec1-gnutls >= 1.0.0

%description backend-aqebics
AqEBICS backend for AqBanking library.

%description backend-aqebics -l pl.UTF-8
Backend AqEBICS dla biblioteki AqBanking.

%package backend-aqhbci
Summary:	AqHBCI backend for AqBanking library
Summary(pl.UTF-8):	Backend AqHBCI dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-aqhbci
AqHBCI backend for AqBanking library.

%description backend-aqhbci -l pl.UTF-8
Backend AqHBCI dla biblioteki AqBanking.

%package backend-aqnone
Summary:	Aqnone backend for AqBanking library
Summary(pl.UTF-8):	Backend Aqnone dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	aqbanking-backend-aqnone-devel
Obsoletes:	aqbanking-backend-aqnone-static

%description backend-aqnone
Aqnone backend for AqBanking library.

%description backend-aqnone -l pl.UTF-8
Backend Aqnone dla biblioteki AqBanking.

%package backend-aqofxconnect
Summary:	AqOFXConnect backend for AqBanking library
Summary(pl.UTF-8):	Backend AqOFXConnect dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-aqofxconnect
AqOFXConnect backend for AqBanking library.

%description backend-aqofxconnect -l pl.UTF-8
Backend AqOFXConnect dla biblioteki AqBanking.

%package backend-aqpaypal
Summary:	AqPayPal backend for AqBanking library
Summary(pl.UTF-8):	Backend AqPayPal dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-aqpaypal
AqPayPal backend for AqBanking library.

%description backend-aqpaypal -l pl.UTF-8
Backend AqPayPal dla biblioteki AqBanking.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la \
	$RPM_BUILD_ROOT%{_libdir}/aqbanking/plugins/*/*/*.la
# no public API
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/aqbanking/plugins/*/*/*.a
%endif

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/aqbanking/{AUTHORS,COPYING,ChangeLog,README}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	backend-aqebics -p /sbin/ldconfig
%postun	backend-aqebics -p /sbin/ldconfig

%post	backend-aqhbci -p /sbin/ldconfig
%postun	backend-aqhbci -p /sbin/ldconfig

%post	backend-aqnone -p /sbin/ldconfig
%postun	backend-aqnone -p /sbin/ldconfig

%post	backend-aqofxconnect -p /sbin/ldconfig
%postun	backend-aqofxconnect -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/aqbanking-cli
%attr(755,root,root) %{_libdir}/libaqbanking.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqbanking.so.44
%dir %{_libdir}/aqbanking
%dir %{_libdir}/aqbanking/plugins
%dir %{_libdir}/aqbanking/plugins/*
%dir %{_libdir}/aqbanking/plugins/*/bankinfo
%{_libdir}/aqbanking/plugins/*/bankinfo/*.xml
%dir %{_libdir}/aqbanking/plugins/*/dbio
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/dbio/*.so
%{_libdir}/aqbanking/plugins/*/dbio/*.xml
%dir %{_libdir}/aqbanking/plugins/*/imexporters
%{_libdir}/aqbanking/plugins/*/imexporters/*.xml
%dir %{_libdir}/aqbanking/plugins/*/providers
%dir %{_datadir}/aqbanking
%dir %{_datadir}/aqbanking/backends
%dir %{_datadir}/aqbanking/aqbanking
%{_datadir}/aqbanking/aqbanking/typemaker2
%{_datadir}/aqbanking/bankinfo
%{_datadir}/aqbanking/dialogs
%{_datadir}/aqbanking/imexporters
%{_datadir}/aqbanking/typemaker2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqbanking-config
%attr(755,root,root) %{_libdir}/libaqbanking.so
%dir %{_includedir}/aqbanking6
%{_includedir}/aqbanking6/aqbanking
%{_pkgconfigdir}/aqbanking.pc
%{_libdir}/cmake/aqbanking-6.3
%{_aclocaldir}/aqbanking.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libaqbanking.a
%endif

%files backend-aqebics
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqebics-tool
%{_libdir}/aqbanking/plugins/*/providers/aqebics.xml
%{_datadir}/aqbanking/backends/aqebics

%files backend-aqhbci
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqhbci-tool4
%{_libdir}/aqbanking/plugins/*/providers/aqhbci.xml
%{_datadir}/aqbanking/backends/aqhbci

%files backend-aqnone
%defattr(644,root,root,755)
%{_libdir}/aqbanking/plugins/*/providers/aqnone.xml

%files backend-aqofxconnect
%defattr(644,root,root,755)
%{_libdir}/aqbanking/plugins/*/providers/aqofxconnect.xml
%{_datadir}/aqbanking/backends/aqofxconnect

%files backend-aqpaypal
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqpaypal-tool
%{_libdir}/aqbanking/plugins/*/providers/aqpaypal.xml
%{_datadir}/aqbanking/backends/aqpaypal

