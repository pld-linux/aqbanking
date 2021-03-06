#
# Conditional build:
%bcond_without	static_libs	# static libraries

%define	gwenhywfar_ver	4.10.0
Summary:	A library for online banking functions and financial data import/export
Summary(pl.UTF-8):	Biblioteka do funkcji bankowych online oraz importu/eksportu danych finansowych
Name:		aqbanking
Version:	5.6.12
Release:	1
License:	GPL v2 or GPL v3
Group:		Libraries
# https://www.aquamaniac.de/sites/download/packages.php?showall=1
Source0:	https://www.aquamaniac.de/sites/download/download.php?package=03&release=208&file=01&dummy=/%{name}-%{version}.tar.gz
# Source0-md5:	f4476db215fe08c73d35b2018cf24739
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
Obsoletes:	aqbanking-backend-aqgeldkarte
Obsoletes:	aqbanking-backend-aqgeldkarte-devel
Obsoletes:	aqbanking-backend-aqgeldkarte-static
Obsoletes:	aqbanking-backend-aqpaypal
Obsoletes:	aqbanking-backend-aqyellownet
Obsoletes:	aqbanking-backend-aqyellownet-devel
Obsoletes:	aqbanking-backend-aqyellownet-static
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

%package c++
Summary:	C++ interface for AqBanking library
Summary(pl.UTF-8):	Interfejs C++ do biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ interface for AqBanking library.

%description c++ -l pl.UTF-8
Interfejs C++ do biblioteki AqBanking.

%package c++-devel
Summary:	Header files for aqbankingpp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki aqbankingpp
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for aqbankingpp library.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki aqbankingpp.

%package c++-static
Summary:	Static aqbankingpp library
Summary(pl.UTF-8):	Statyczna biblioteka aqbankingpp
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static aqbankingpp library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka aqbankingpp.

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

%package backend-aqebics-devel
Summary:	Header files for AqEBICS client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej AqEBICS
Group:		Development/Libraries
Requires:	%{name}-backend-aqebics = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description backend-aqebics-devel
Header files for AqEBICS client library.

%description backend-aqebics-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej AqEBICS.

%package backend-aqebics-static
Summary:	Static AqEBICS client library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka AqEBICS
Group:		Development/Libraries
Requires:	%{name}-backend-aqebics-devel = %{version}-%{release}

%description backend-aqebics-static
Static AqEBICS client library.

%description backend-aqebics-static -l pl.UTF-8
Statyczna biblioteka kliencka AqEBICS.

%package backend-aqhbci
Summary:	AqHBCI backend for AqBanking library
Summary(pl.UTF-8):	Backend AqHBCI dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-aqhbci
AqHBCI backend for AqBanking library.

%description backend-aqhbci -l pl.UTF-8
Backend AqHBCI dla biblioteki AqBanking.

%package backend-aqhbci-devel
Summary:	Header files for AqHBCI client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej AqHBCI
Group:		Development/Libraries
Requires:	%{name}-backend-aqhbci = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description backend-aqhbci-devel
Header files for AqHBCI client library.

%description backend-aqhbci-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej AqHBCI.

%package backend-aqhbci-static
Summary:	Static AqHBCI client library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka AqHBCI
Group:		Development/Libraries
Requires:	%{name}-backend-aqhbci-devel = %{version}-%{release}

%description backend-aqhbci-static
Static AqHBCI client library.

%description backend-aqhbci-static -l pl.UTF-8
Statyczna biblioteka kliencka AqHBCI.

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

%package backend-aqofxconnect-devel
Summary:	Header files for AqOFXConnect client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej AqOFXConnect
Group:		Development/Libraries
Requires:	%{name}-backend-aqofxconnect = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description backend-aqofxconnect-devel
Header files for AqOFXConnect client library.

%description backend-aqofxconnect-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej AqOFXConnect.

%package backend-aqofxconnect-static
Summary:	Static AqOFXConnect client library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka AqOFXConnect
Group:		Development/Libraries
Requires:	%{name}-backend-aqofxconnect-devel = %{version}-%{release}

%description backend-aqofxconnect-static
Static AqOFXConnect client library.

%description backend-aqofxconnect-static -l pl.UTF-8
Statyczna biblioteka kliencka AqOFXConnect.

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

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la \
	$RPM_BUILD_ROOT%{_libdir}/aqbanking/plugins/*/*/*.la
# no public API
%{__rm}	$RPM_BUILD_ROOT%{_libdir}/libaqnone.so
%if %{with static_libs}
%{__rm}	$RPM_BUILD_ROOT%{_libdir}/libaqnone.a \
	$RPM_BUILD_ROOT%{_libdir}/aqbanking/plugins/*/*/*.a
%endif

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/aqbanking/{AUTHORS,COPYING,ChangeLog,README} \
	$RPM_BUILD_ROOT%{_docdir}/aqhbci/aqhbci-tool/README
# empty
%{__rm} $RPM_BUILD_ROOT%{_docdir}/aqebics/aqebics-tool/README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

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
%attr(755,root,root) %ghost %{_libdir}/libaqbanking.so.35
%dir %{_libdir}/aqbanking
%dir %{_libdir}/aqbanking/plugins
%dir %{_libdir}/aqbanking/plugins/*
%dir %{_libdir}/aqbanking/plugins/*/bankinfo
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/bankinfo/*.so
%{_libdir}/aqbanking/plugins/*/bankinfo/*.xml
%dir %{_libdir}/aqbanking/plugins/*/dbio
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/dbio/*.so
%{_libdir}/aqbanking/plugins/*/dbio/*.xml
%dir %{_libdir}/aqbanking/plugins/*/imexporters
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/imexporters/*.so
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
%dir %{_includedir}/aqbanking5
%{_includedir}/aqbanking5/aqbanking
%{_pkgconfigdir}/aqbanking.pc
%{_libdir}/cmake/aqbanking-5.6
%{_aclocaldir}/aqbanking.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libaqbanking.a
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqbankingpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqbankingpp.so.0

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqbankingpp.so
%{_includedir}/aqbanking5/aqbankingpp

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libaqbankingpp.a
%endif

%files backend-aqebics
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqebics-tool
%attr(755,root,root) %{_libdir}/libaqebics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqebics.so.0
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqebics.so
%{_libdir}/aqbanking/plugins/*/providers/aqebics.xml
%{_datadir}/aqbanking/backends/aqebics

%files backend-aqebics-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqebics.so
%{_includedir}/aqebics

%if %{with static_libs}
%files backend-aqebics-static
%defattr(644,root,root,755)
%{_libdir}/libaqebics.a
%endif

%files backend-aqhbci
%defattr(644,root,root,755)
%doc src/plugins/backends/aqhbci/tools/aqhbci-tool/README
%attr(755,root,root) %{_bindir}/aqhbci-tool4
%attr(755,root,root) %{_bindir}/hbcixml3
%attr(755,root,root) %{_libdir}/libaqhbci.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqhbci.so.23
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqhbci.so
%{_libdir}/aqbanking/plugins/*/providers/aqhbci.xml
%{_datadir}/aqbanking/backends/aqhbci

%files backend-aqhbci-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqhbci.so
%{_includedir}/aqbanking5/aqhbci

%if %{with static_libs}
%files backend-aqhbci-static
%defattr(644,root,root,755)
%{_libdir}/libaqhbci.a
%endif

%files backend-aqnone
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqnone.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqnone.so.35
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqnone.so
%{_libdir}/aqbanking/plugins/*/providers/aqnone.xml

%files backend-aqofxconnect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqofxconnect.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqofxconnect.so.7
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqofxconnect.so
%{_libdir}/aqbanking/plugins/*/providers/aqofxconnect.xml
%{_datadir}/aqbanking/backends/aqofxconnect

%files backend-aqofxconnect-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqofxconnect.so
%{_includedir}/aqbanking5/aqofxconnect

%if %{with static_libs}
%files backend-aqofxconnect-static
%defattr(644,root,root,755)
%{_libdir}/libaqofxconnect.a
%endif
