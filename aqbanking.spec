#
# - fix building without chipcard (aclocal fail) or drop bcond
# Conditional build:
%bcond_without	chipcard	# aqgeldkarte backend
%bcond_without	fox		# fbanking frontend
%bcond_with	yellownet	# yellownet backend (x86-only, no sources currently)
#
Summary:	A library for online banking functions and financial data import/export
Summary(pl.UTF-8):	Biblioteka do funkcji bankowych online oraz importu/eksportu danych finansowych
Name:		aqbanking
Version:	3.0.1
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/aqbanking/%{name}-%{version}.tar.gz
# Source0-md5:	be3bafd787973b33895d80bbc6104bf5
Patch0:		%{name}-link.patch
Patch1:		%{name}-nobash.patch
Patch2:		%{name}-fbanking.patch
Patch3:		%{name}-backends.patch
URL:		http://www.aquamaniac.de/aqbanking/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
%{?with_fox:BuildRequires:	fox-devel >= 1.6.0}
BuildRequires:	gettext-devel
BuildRequires:	gwenhywfar-devel >= 3.0.0
BuildRequires:	ktoblzcheck-devel
%{?with_chipcard:BuildRequires:	libchipcard-devel >= 4.0.0}
BuildRequires:	libofx-devel >= 0.8.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	qt-devel >= 1:3.0
BuildRequires:	rpm-pythonprov
Obsoletes:	aqbanking-frontend-cbanking
Obsoletes:	aqbanking-frontend-cbanking-devel
Obsoletes:	aqbanking-frontend-cbanking-static
Obsoletes:	aqbanking-frontend-g2banking
Obsoletes:	aqbanking-frontend-g2banking-devel
Obsoletes:	aqbanking-frontend-g2banking-static
Obsoletes:	aqbanking-frontend-kbanking
Obsoletes:	aqbanking-frontend-kbanking-devel
Obsoletes:	aqbanking-frontend-kbanking-static
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

%package backend-aqdtaus
Summary:	AqDTAUS backend for AqBanking library
Summary(pl.UTF-8):	Backend AqDTAUS dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-aqdtaus
AqDTAUS backend for AqBanking library.

%description backend-aqdtaus -l pl.UTF-8
Backend AqDTAUS dla biblioteki AqBanking.

%package backend-aqdtaus-devel
Summary:	Header files for AqDTAUS backend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki backendu AqDTAUS
Group:		Development/Libraries
Requires:	%{name}-backend-aqdtaus = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description backend-aqdtaus-devel
Header files for AqDTAUS backend library.

%description backend-aqdtaus-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki backendu AqDTAUS.

%package backend-aqdtaus-static
Summary:	Static AqDTAUS backend library
Summary(pl.UTF-8):	Statyczna biblioteka backendu AqDTAUS
Group:		Development/Libraries
Requires:	%{name}-backend-aqdtaus-devel = %{version}-%{release}

%description backend-aqdtaus-static
Static AqDTAUS backend library.

%description backend-aqdtaus-static -l pl.UTF-8
Statyczna biblioteka backendu AqDTAUS.

%package backend-aqgeldkarte
Summary:	AqGeldKarte backend for AqBanking library
Summary(pl.UTF-8):	Backend AqGeldKarte dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-aqgeldkarte
AqGeldKarte backend for AqBanking library.

%description backend-aqgeldkarte -l pl.UTF-8
Backend AqGeldKarte dla biblioteki AqBanking.

%package backend-aqgeldkarte-devel
Summary:	Header files for AqGeldKarte backend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki backendu AqGeldKarte
Group:		Development/Libraries
Requires:	%{name}-backend-aqgeldkarte = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libchipcard-devel >= 4.0.0

%description backend-aqgeldkarte-devel
Header files for AqGeldKarte backend library.

%description backend-aqgeldkarte-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki backendu AqGeldKarte.

%package backend-aqgeldkarte-static
Summary:	Static AqGeldKarte backend library
Summary(pl.UTF-8):	Statyczna biblioteka backendu AqGeldKarte
Group:		Development/Libraries
Requires:	%{name}-backend-aqgeldkarte-devel = %{version}-%{release}

%description backend-aqgeldkarte-static
Static AqGeldKarte backend library.

%description backend-aqgeldkarte-static -l pl.UTF-8
Statyczna biblioteka backendu AqGeldKarte.

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

%package backend-aqyellownet
Summary:	AqYellowNet backend for AqBanking library
Summary(pl.UTF-8):	Backend AqYellowNet dla biblioteki AqBanking
License:	custom
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-aqyellownet
AqYellowNet backend for AqBanking library.

%description backend-aqyellownet -l pl.UTF-8
Backend AqYellowNet dla biblioteki AqBanking.

%package backend-aqyellownet-devel
Summary:	Header files for AqYellowNet backend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki backendu AqYellowNet
License:	custom
Group:		Development/Libraries
Requires:	%{name}-backend-aqyellownet = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description backend-aqyellownet-devel
Header files for AqYellowNet backend library.

%description backend-aqyellownet-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki backendu AqYellowNet.

%package backend-aqyellownet-static
Summary:	Static AqYellowNet backend library
Summary(pl.UTF-8):	Statyczna biblioteka backendu AqYellowNet
License:	custom
Group:		Development/Libraries
Requires:	%{name}-backend-aqyellownet-devel = %{version}-%{release}

%description backend-aqyellownet-static
Static AqYellowNet backend library.

%description backend-aqyellownet-static -l pl.UTF-8
Statyczna biblioteka backendu AqYellowNet.

%package frontend-fbanking
Summary:	Fbanking frontend for AqBanking library
Summary(pl.UTF-8):	Frontend Fbanking dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description frontend-fbanking
Fbanking frontend for AqBanking library.

%description frontend-fbanking -l pl.UTF-8
Frontend Fbanking dla biblioteki AqBanking.

%package frontend-fbanking-devel
Summary:	Header files for Fbanking frontend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki frontendu Fbanking
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-frontend-fbanking = %{version}-%{release}
Requires:	fox-devel >= 1.6.0

%description frontend-fbanking-devel
Header files for Fbanking frontend library.

%description frontend-fbanking-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki frontendu Fbanking.

%package frontend-fbanking-static
Summary:	Static Fbanking frontend library
Summary(pl.UTF-8):	Statyczna biblioteka frontendu Fbanking
Group:		Development/Libraries
Requires:	%{name}-frontend-fbanking-devel = %{version}-%{release}

%description frontend-fbanking-static
Static Fbanking frontend library.

%description frontend-fbanking-static -l pl.UTF-8
Statyczna biblioteka frontendu Fbanking.

%package frontend-qbanking
Summary:	QBanking - Qt-based frontend for AqBanking library
Summary(pl.UTF-8):	QBanking - oparty na Qt frontend dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description frontend-qbanking
QBanking - Qt-based frontend for AqBanking library.

%description frontend-qbanking -l pl.UTF-8
QBanking - oparty na Qt frontend dla biblioteki AqBanking.

%package frontend-qbanking-devel
Summary:	Header files for QBanking frontend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki frontendu QBanking
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-frontend-qbanking = %{version}-%{release}
Requires:	qt-devel >= 1:3.0

%description frontend-qbanking-devel
Header files for QBanking frontend library.

%description frontend-qbanking-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki frontendu QBanking.

%package frontend-qbanking-static
Summary:	Static QBanking frontend library
Summary(pl.UTF-8):	Statyczna biblioteka frontendu QBanking
Group:		Development/Libraries
Requires:	%{name}-frontend-qbanking-devel = %{version}-%{release}

%description frontend-qbanking-static
Static QBanking frontend library.

%description frontend-qbanking-static -l pl.UTF-8
Statyczna biblioteka frontendu QBanking.

%package -n python-%{name}
Summary:	Python binding for AqBanking library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki AqBanking
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
# for python-ctypes
Requires:	python-modules >= 1:2.5
%pyrequires_eq	python-libs

%description -n python-%{name}
Python binding for AqBanking library.

%description -n python-%{name} -l pl.UTF-8
Wiązanie Pythona do biblioteki AqBanking.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

ln -s ../../qbanking/lib/banking.h src/frontends/fbanking/lib
ln -s ../../qbanking/lib/banking.cpp src/frontends/fbanking/lib

%ifnarch %{ix86}
%{?with_yellownet:%{error: yellownet backend is x86-only}exit 1}
%endif

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-qt3-libs=%{_libdir} \
	--enable-libofx \
	--enable-python \
	--enable-static \
	--with-backends="aqhbci aqdtaus%{?with_chipcard: aqgeldkarte} aqofxconnect%{?with_yellownet: aqyellownet}" \
	--with-frontends="%{?with_fox:fbanking }qbanking"

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

%post	backend-aqdtaus -p /sbin/ldconfig
%postun	backend-aqdtaus -p /sbin/ldconfig

%post	backend-aqgeldkarte -p /sbin/ldconfig
%postun	backend-aqgeldkarte -p /sbin/ldconfig

%post	backend-aqhbci -p /sbin/ldconfig
%postun	backend-aqhbci -p /sbin/ldconfig

%post	backend-aqnone -p /sbin/ldconfig
%postun	backend-aqnone -p /sbin/ldconfig

%post	backend-aqofxconnect -p /sbin/ldconfig
%postun	backend-aqofxconnect -p /sbin/ldconfig

%post	backend-aqyellownet -p /sbin/ldconfig
%postun	backend-aqyellownet -p /sbin/ldconfig

%post	frontend-fbanking -p /sbin/ldconfig
%postun	frontend-fbanking -p /sbin/ldconfig

%post	frontend-qbanking -p /sbin/ldconfig
%postun	frontend-qbanking -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libaqbanking.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqbanking.so.20
%dir %{_libdir}/aqbanking
%dir %{_libdir}/aqbanking/plugins
%dir %{_libdir}/aqbanking/plugins/*
%dir %{_libdir}/aqbanking/plugins/*/bankinfo
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/bankinfo/*.so*
%{_libdir}/aqbanking/plugins/*/bankinfo/*.xml
%dir %{_libdir}/aqbanking/plugins/*/debugger
%dir %{_libdir}/aqbanking/plugins/*/frontends
%dir %{_libdir}/aqbanking/plugins/*/frontends/qbanking
%dir %{_libdir}/aqbanking/plugins/*/frontends/qbanking/cfgmodules
%dir %{_libdir}/aqbanking/plugins/*/imexporters
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/imexporters/*.so*
%{_libdir}/aqbanking/plugins/*/imexporters/*.xml
%dir %{_libdir}/aqbanking/plugins/*/providers
%dir %{_libdir}/aqbanking/plugins/*/wizards
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/dbio/*.so*
%{_libdir}/gwenhywfar/plugins/*/dbio/*.xml
%dir %{_datadir}/aqbanking
%dir %{_datadir}/aqbanking/backends
%{_datadir}/aqbanking/bankinfo
%dir %{_datadir}/aqbanking/frontends
%dir %{_datadir}/aqbanking/i18n
%{_datadir}/aqbanking/imexporters

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqbanking-config
%attr(755,root,root) %{_libdir}/libaqbanking.so
%{_libdir}/libaqbanking.la
%{_includedir}/aqbanking
%{_aclocaldir}/aqbanking.m4
%{_pkgconfigdir}/aqbanking.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libaqbanking.a

%files backend-aqdtaus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqdtaus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqdtaus.so.4
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqdtaus.so*
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/frontends/qbanking/cfgmodules/aqdtaus.so*
%{_libdir}/aqbanking/plugins/*/providers/aqdtaus.xml

%files backend-aqdtaus-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqdtaus.so
%{_libdir}/libaqdtaus.la
%{_includedir}/aqdtaus
%{_aclocaldir}/aqdtaus.m4

%files backend-aqdtaus-static
%defattr(644,root,root,755)
%{_libdir}/libaqdtaus.a

%if %{with chipcard}
%files backend-aqgeldkarte
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqgeldkarte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqgeldkarte.so.5
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqgeldkarte.so*
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/frontends/qbanking/cfgmodules/aqgeldkarte.so*
%{_libdir}/aqbanking/plugins/*/providers/aqgeldkarte.xml

%files backend-aqgeldkarte-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqgeldkarte.so
%{_libdir}/libaqgeldkarte.la
%{_includedir}/aqgeldkarte
%{_aclocaldir}/aqgeldkarte.m4

%files backend-aqgeldkarte-static
%defattr(644,root,root,755)
%{_libdir}/libaqgeldkarte.a
%endif

%files backend-aqhbci
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqhbci-tool3
%attr(755,root,root) %{_bindir}/hbcixml3
%attr(755,root,root) %{_libdir}/libaqhbci.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqhbci.so.12
%dir %{_libdir}/aqbanking/plugins/*/debugger/aqhbci
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/debugger/aqhbci/aqhbci-qt3-debug
%{_libdir}/aqbanking/plugins/*/debugger/aqhbci/qt_debug.xml
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqhbci.so*
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/frontends/qbanking/cfgmodules/aqhbci.so*
%{_libdir}/aqbanking/plugins/*/providers/aqhbci.xml
%{_datadir}/aqbanking/backends/aqhbci

%files backend-aqhbci-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqhbci.so
%{_libdir}/libaqhbci.la
%{_includedir}/aqhbci

%files backend-aqhbci-static
%defattr(644,root,root,755)
%{_libdir}/libaqhbci.a

%files backend-aqnone
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqnone.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaqnone.so.20
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
%attr(755,root,root) %ghost %{_libdir}/libaqofxconnect.so.4
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqofxconnect.so*
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/frontends/qbanking/cfgmodules/aqofxconnect.so*
%{_libdir}/aqbanking/plugins/*/providers/aqofxconnect.xml

%files backend-aqofxconnect-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqofxconnect.so
%{_libdir}/libaqofxconnect.la
%{_includedir}/aqofxconnect

%files backend-aqofxconnect-static
%defattr(644,root,root,755)
%{_libdir}/libaqofxconnect.a

%if %{with yellownet}
%files backend-aqyellownet
%defattr(644,root,root,755)
%doc src/plugins/backends/aqyellownet/plugin/COPYING
%attr(755,root,root) %{_libdir}/libaqyellownet.so.*.*.*
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqyellownet.so*
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/frontends/qbanking/cfgmodules/aqyellownet.so*
%{_libdir}/aqbanking/plugins/*/providers/aqyellownet.xml

%files backend-aqyellownet-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqyellownet.so
#%{_libdir}/libaqyellownet.la
%{_includedir}/aqyellownet
%{_aclocaldir}/aqyellownet.m4

#%files backend-aqyellownet-static
#%defattr(644,root,root,755)
#%{_libdir}/libaqyellownet.a
%endif

%if %{with fox}
%files frontend-fbanking
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfbanking.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfbanking.so.2

%files frontend-fbanking-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfbanking.so
%{_libdir}/libfbanking.la
%{_includedir}/fbanking
%{_pkgconfigdir}/fbanking.pc

%files frontend-fbanking-static
%defattr(644,root,root,755)
%{_libdir}/libfbanking.a
%endif

%files frontend-qbanking
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qb-help5
%attr(755,root,root) %{_libdir}/libqbanking.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqbanking.so.5
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/wizards/qt3-wizard
%{_libdir}/aqbanking/plugins/*/wizards/qt3_wizard.xml
%dir %{_datadir}/aqbanking/frontends/qbanking
%dir %{_datadir}/aqbanking/frontends/qbanking/help
%lang(de) %{_datadir}/aqbanking/frontends/qbanking/help/de
%lang(de) %{_datadir}/aqbanking/i18n/de.qm

%files frontend-qbanking-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqbanking.so
%{_libdir}/libqbanking.la
%{_includedir}/qbanking

%files frontend-qbanking-static
%defattr(644,root,root,755)
%{_libdir}/libqbanking.a

%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/aqbanking
%{py_sitescriptdir}/aqbanking/*.py[co]
