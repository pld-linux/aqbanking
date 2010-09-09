#
# TODO: unpackaged files
#
Summary:	A library for online banking functions and financial data import/export
Summary(pl.UTF-8):	Biblioteka do funkcji bankowych online oraz importu/eksportu danych finansowych
Name:		aqbanking
Version:	5.0.1
Release:	0.1
License:	GPL v2
Group:		Libraries
# http://www2.aquamaniac.de/sites/download/packages.php
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	dc7dd799a4a50313b5f11b9a0861b72b
URL:		http://www.aquamaniac.de/aqbanking/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	gwenhywfar-devel >= 4.0.0
BuildRequires:	ktoblzcheck-devel >= 1.10
BuildRequires:	libofx-devel >= 0.8.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 1:3.0
BuildRequires:	which
Obsoletes:	aqbanking-backend-aqdtaus
Obsoletes:	aqbanking-backend-aqdtaus-devel
Obsoletes:	aqbanking-backend-aqdtaus-static
Obsoletes:	aqbanking-backend-aqgeldkarte
Obsoletes:	aqbanking-backend-aqgeldkarte-devel
Obsoletes:	aqbanking-backend-aqgeldkarte-static
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
Pierwszy już obsługiwany backend to AqHBCI - biblioteka implementująca
klienta niemieckiego protokołu HBCI (Home Baking Computer Interface).
Ponadto Aqbanking dostarcza różne wtyczki upraszczające importowanie i
eksportowanie danych finansowych. Aktualnie istnieją wtyczki do
importu następujących formatów: DTAUS (niemiecki format finansowy),
SWIFT (MT940 oraz MT942).

%package devel
Summary:	Header files for AqBanking library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AqBanking
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gwenhywfar-devel >= 3.0.0

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
Summary:	Header files for AqHBCI backend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki backendu AqHBCI
Group:		Development/Libraries
Requires:	%{name}-backend-aqhbci = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description backend-aqhbci-devel
Header files for AqHBCI backend library.

%description backend-aqhbci-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki backendu AqHBCI.

%package backend-aqhbci-static
Summary:	Static AqHBCI backend library
Summary(pl.UTF-8):	Statyczna biblioteka backendu AqHBCI
Group:		Development/Libraries
Requires:	%{name}-backend-aqhbci-devel = %{version}-%{release}

%description backend-aqhbci-static
Static AqHBCI backend library.

%description backend-aqhbci-static -l pl.UTF-8
Statyczna biblioteka backendu AqHBCI.

%package backend-aqnone
Summary:	Aqnone backend for AqBanking library
Summary(pl.UTF-8):	Backend Aqnone dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-aqnone
Aqnone backend for AqBanking library.

%description backend-aqnone -l pl.UTF-8
Backend Aqnone dla biblioteki AqBanking.

%package backend-aqnone-devel
Summary:	Header files for Aqnone backend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki backendu Aqnone
Group:		Development/Libraries
Requires:	%{name}-backend-aqnone = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description backend-aqnone-devel
Header files for Aqnone backend library.

%description backend-aqnone-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki backendu Aqnone.

%package backend-aqnone-static
Summary:	Static Aqnone backend library
Summary(pl.UTF-8):	Statyczna biblioteka backendu Aqnone
Group:		Development/Libraries
Requires:	%{name}-backend-aqnone-devel = %{version}-%{release}

%description backend-aqnone-static
Static Aqnone backend library.

%description backend-aqnone-static -l pl.UTF-8
Statyczna biblioteka backendu Aqnone.

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
Summary:	Header files for AqOFXConnect backend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki backendu AqOFXConnect
Group:		Development/Libraries
Requires:	%{name}-backend-aqofxconnect = %{version}-%{release}
Requires:	libofx-devel >= 0.8.0

%description backend-aqofxconnect-devel
Header files for AqOFXConnect backend library.

%description backend-aqofxconnect-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki backendu AqOFXConnect.

%package backend-aqofxconnect-static
Summary:	Static AqOFXConnect backend library
Summary(pl.UTF-8):	Statyczna biblioteka backendu AqOFXConnect
Group:		Development/Libraries
Requires:	%{name}-backend-aqofxconnect-devel = %{version}-%{release}

%description backend-aqofxconnect-static
Static AqOFXConnect backend library.

%description backend-aqofxconnect-static -l pl.UTF-8
Statyczna biblioteka backendu AqOFXConnect.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-qt3-libs=%{_libdir} \
	--enable-libofx \
	--enable-static \
	--with-backends="aqhbci aqofxconnect aqnone" \
	--with-frontends="qbanking"

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/aqbanking/plugins/*/*/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/aqbanking/plugins/*/frontends/qbanking/cfgmodules/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/gwenhywfar/plugins/*/*/*.{la,a}
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/aqbanking/*.py

%if %{with yellownet}
# soname is libaqyellownet.so.0
mv $RPM_BUILD_ROOT%{_libdir}/libaqyellownet.{so,so.0.0.0}
ln -sf libaqyellownet.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/libaqyellownet.so
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	backend-aqhbci -p /sbin/ldconfig
%postun	backend-aqhbci -p /sbin/ldconfig

%post	backend-aqnone -p /sbin/ldconfig
%postun	backend-aqnone -p /sbin/ldconfig

%post	backend-aqofxconnect -p /sbin/ldconfig
%postun	backend-aqofxconnect -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/aqbanking-cli
%attr(755,root,root) %{_libdir}/libaqbanking.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqbanking.so.33
%dir %{_libdir}/aqbanking
%dir %{_libdir}/aqbanking/plugins
%dir %{_libdir}/aqbanking/plugins/*
%dir %{_libdir}/aqbanking/plugins/*/bankinfo
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/bankinfo/*.so*
%{_libdir}/aqbanking/plugins/*/bankinfo/*.xml
%dir %{_libdir}/aqbanking/plugins/*/imexporters
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/imexporters/*.so*
%{_libdir}/aqbanking/plugins/*/imexporters/*.xml
%dir %{_libdir}/aqbanking/plugins/*/providers
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/dbio/*.so*
%{_libdir}/gwenhywfar/plugins/*/dbio/*.xml
%dir %{_datadir}/aqbanking
%{_datadir}/aqbanking/bankinfo
%{_datadir}/aqbanking/imexporters

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqbanking-config
%attr(755,root,root) %{_libdir}/libaqbanking.so
%{_libdir}/libaqbanking.la
%{_includedir}/aqbanking5
%{_aclocaldir}/aqbanking.m4
%{_pkgconfigdir}/aqbanking.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libaqbanking.a

%files backend-aqhbci
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqhbci-tool4
%attr(755,root,root) %{_bindir}/hbcixml3
%attr(755,root,root) %{_libdir}/libaqhbci.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqhbci.so.19
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqhbci.so*
%{_libdir}/aqbanking/plugins/*/providers/aqhbci.xml
%dir %{_datadir}/aqbanking/backends
%{_datadir}/aqbanking/backends/aqhbci

%files backend-aqhbci-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqhbci.so
%{_libdir}/libaqhbci.la

%files backend-aqhbci-static
%defattr(644,root,root,755)
%{_libdir}/libaqhbci.a

%files backend-aqnone
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqnone.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqnone.so.33
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqnone.so*
%{_libdir}/aqbanking/plugins/*/providers/aqnone.xml

%files backend-aqnone-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqnone.so
%{_libdir}/libaqnone.la

%files backend-aqnone-static
%defattr(644,root,root,755)
%{_libdir}/libaqnone.a

%files backend-aqofxconnect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqofxconnect.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqofxconnect.so.7
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqofxconnect.so*
%{_libdir}/aqbanking/plugins/*/providers/aqofxconnect.xml

%files backend-aqofxconnect-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqofxconnect.so
%{_libdir}/libaqofxconnect.la

%files backend-aqofxconnect-static
%defattr(644,root,root,755)
%{_libdir}/libaqofxconnect.a
