#
# Conditional build:
%bcond_with	chipcard	# aqgeldkarte backend
%bcond_without	gtk		# g2banking frontend
%bcond_without	kde		# kbanking frontend
#
Summary:	A library for online banking functions and financial data import/export
Summary(pl.UTF-8):	Biblioteka do funkcji bankowych online oraz importu/eksportu danych finansowych
Name:		aqbanking
Version:	1.6.2
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/aqbanking/%{name}-%{version}.tar.gz
# Source0-md5:	cb8337cf12072a304217379b7ea23df2
Patch0:		%{name}-link.patch
Patch1:		%{name}-glade.patch
Patch2:		%{name}-libsuffix.patch
URL:		http://www.aquamaniac.de/aqbanking/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gwenhywfar-devel >= 1.18.0
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2.0.0}
%{?with_kde:BuildRequires:	kdelibs-devel >= 3.0}
BuildRequires:	ktoblzcheck-devel
%{?with_chipcard:BuildRequires:	libchipcard2-devel >= 1.9.15}
BuildRequires:	libofx-devel >= 0.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	python-ctypes
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	qt-devel >= 1:3.0
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
Requires:	gwenhywfar-devel >= 1.18.0
# for libaqbankingpp only
#Requires:	libstdc++-devel

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
Requires:	libchipcard2-devel >= 1.9.15

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

%package frontend-cbanking
Summary:	Cbanking frontend for AqBanking library
Summary(pl.UTF-8):	Frontend Cbanking dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description frontend-cbanking
Cbanking frontend for AqBanking library.

%description frontend-cbanking -l pl.UTF-8
Frontend Cbanking dla biblioteki AqBanking.

%package frontend-cbanking-devel
Summary:	Header files for Cbanking frontend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki frontendu Cbanking
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-frontend-cbanking = %{version}-%{release}

%description frontend-cbanking-devel
Header files for Cbanking frontend library.

%description frontend-cbanking-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki frontendu Cbanking.

%package frontend-cbanking-static
Summary:	Static Cbanking frontend library
Summary(pl.UTF-8):	Statyczna biblioteka frontendu Cbanking
Group:		Development/Libraries
Requires:	%{name}-frontend-cbanking-devel = %{version}-%{release}

%description frontend-cbanking-static
Static Cbanking frontend library.

%description frontend-cbanking-static -l pl.UTF-8
Statyczna biblioteka frontendu Cbanking.

%package frontend-g2banking
Summary:	G2Banking - GTK+ based frontend for AqBanking library
Summary(pl.UTF-8):	G2Bbanking - oparty na GTK+ frontend dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description frontend-g2banking
G2Banking - GTK+ based frontend for AqBanking library.

%description frontend-g2banking -l pl.UTF-8
G2Bbanking - oparty na GTK+ frontend dla biblioteki AqBanking.

%package frontend-g2banking-devel
Summary:	Header files for G2Banking frontend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki frontendu G2Banking
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-frontend-g2banking = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0.0

%description frontend-g2banking-devel
Header files for G2Banking frontend library.

%description frontend-g2banking-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki frontendu G2Banking.

%package frontend-g2banking-static
Summary:	Static G2Banking frontend library
Summary(pl.UTF-8):	Statyczna biblioteka frontendu G2Banking
Group:		Development/Libraries
Requires:	%{name}-frontend-g2banking-devel = %{version}-%{release}

%description frontend-g2banking-static
Static G2Banking frontend library.

%description frontend-g2banking-static -l pl.UTF-8
Statyczna biblioteka frontendu G2Banking.

%package frontend-kbanking
Summary:	KBanking - KDE-based frontend for AqBanking library
Summary(pl.UTF-8):	KBanking - oparty na KDE frontend dla biblioteki AqBanking
Group:		Libraries
Requires:	%{name}-frontend-qbanking = %{version}-%{release}

%description frontend-kbanking
KBanking - KDE-based frontend for AqBanking library.

%description frontend-kbanking -l pl.UTF-8
KBanking - oparty na KDE frontend dla biblioteki AqBanking.

%package frontend-kbanking-devel
Summary:	Header files for KBanking frontend library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki frontendu KBanking
Group:		Development/Libraries
Requires:	%{name}-frontend-kbanking = %{version}-%{release}
Requires:	%{name}-frontend-qbanking-devel = %{version}-%{release}
Requires:	kdelibs-devel >= 3.0

%description frontend-kbanking-devel
Header files for KBanking frontend library.

%description frontend-kbanking-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki frontendu KBanking.

%package frontend-kbanking-static
Summary:	Static KBanking frontend library
Summary(pl.UTF-8):	Statyczna biblioteka frontendu KBanking
Group:		Development/Libraries
Requires:	%{name}-frontend-kbanking-devel = %{version}-%{release}

%description frontend-kbanking-static
Static KBanking frontend library.

%description frontend-kbanking-static -l pl.UTF-8
Statyczna biblioteka frontendu KBanking.

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
Requires:	python-ctypes
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

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_kde:--disable-kde3} \
	--enable-libofx \
	--enable-python \
	--enable-static \
	--with-backends="aqhbci aqdtaus%{?with_chipcard: aqgeldkarte} aqofxconnect" \
	--with-frontends="cbanking%{?with_gtk: g2banking} qbanking%{?with_kde: kbanking}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*/plugins/*/*/*.{la,a}
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/aqbanking/*.py

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

%post	backend-aqofxconnect -p /sbin/ldconfig
%postun	backend-aqofxconnect -p /sbin/ldconfig

%post	frontend-cbanking -p /sbin/ldconfig
%postun	frontend-cbanking -p /sbin/ldconfig

%post	frontend-g2banking -p /sbin/ldconfig
%postun	frontend-g2banking -p /sbin/ldconfig

%post	frontend-kbanking -p /sbin/ldconfig
%postun	frontend-kbanking -p /sbin/ldconfig

%post	frontend-qbanking -p /sbin/ldconfig
%postun	frontend-qbanking -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libaqbanking.so.*.*.*
%attr(755,root,root) %{_libdir}/libaqbankingpp.so.*.*.*
%dir %{_libdir}/aqbanking
%dir %{_libdir}/aqbanking/plugins
%dir %{_libdir}/aqbanking/plugins/*
%dir %{_libdir}/aqbanking/plugins/*/bankinfo
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/bankinfo/*.so*
%{_libdir}/aqbanking/plugins/*/bankinfo/*.xml
%dir %{_libdir}/aqbanking/plugins/*/debugger
%dir %{_libdir}/aqbanking/plugins/*/imexporters
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/imexporters/*.so*
%{_libdir}/aqbanking/plugins/*/imexporters/*.xml
%dir %{_libdir}/aqbanking/plugins/*/providers
%dir %{_libdir}/aqbanking/plugins/*/wizards
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/dbio/*.so*
%{_libdir}/gwenhywfar/plugins/*/dbio/*.xml
%{_datadir}/aqbanking

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqbanking-config
%attr(755,root,root) %{_libdir}/libaqbanking.so
%attr(755,root,root) %{_libdir}/libaqbankingpp.so
%{_libdir}/libaqbanking.la
%{_libdir}/libaqbankingpp.la
%{_includedir}/aqbanking
%{_includedir}/aqbanking++
%{_aclocaldir}/aqbanking.m4
%{_pkgconfigdir}/aqbanking.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libaqbanking.a
%{_libdir}/libaqbankingpp.a

%files backend-aqdtaus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqdtaus.so.*.*.*
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqdtaus.so*
%{_libdir}/aqbanking/plugins/*/providers/aqdtaus.xml
%dir %{_libdir}/aqbanking/plugins/*/wizards/aqdtaus
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/wizards/aqdtaus/aqdtaus-qt3-wizard
%{_libdir}/aqbanking/plugins/*/wizards/aqdtaus/qt_wizard.xml

%files backend-aqdtaus-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqdtaus-config
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
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqgeldkarte.so*
%{_libdir}/aqbanking/plugins/*/providers/aqgeldkarte.xml
%dir %{_libdir}/aqbanking/plugins/*/wizards/aqgeldkarte
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/wizards/aqgeldkarte/aqgeldkarte-qt3-wizard
%{_libdir}/aqbanking/plugins/*/wizards/aqgeldkarte/qt_wizard.xml

%files backend-aqgeldkarte-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqgeldkarte-config
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
%attr(755,root,root) %{_bindir}/aqhbci-tool
%attr(755,root,root) %{_bindir}/hbcixml2
%attr(755,root,root) %{_libdir}/libaqhbci.so.*.*.*
%dir %{_libdir}/aqbanking/plugins/*/debugger/aqhbci
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/debugger/aqhbci/aqhbci-qt3-debug
%{_libdir}/aqbanking/plugins/*/debugger/aqhbci/qt_debug.xml
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqhbci.so*
%{_libdir}/aqbanking/plugins/*/providers/aqhbci.xml
%dir %{_libdir}/aqbanking/plugins/*/wizards/aqhbci
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/wizards/aqhbci/aqhbci-qt3-wizard
%{_libdir}/aqbanking/plugins/*/wizards/aqhbci/kde_wizard.xml
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/crypttoken/pintan.so
%{_libdir}/gwenhywfar/plugins/*/crypttoken/pintan.xml
%{_datadir}/aqhbci

%files backend-aqhbci-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqhbci-config
%attr(755,root,root) %{_libdir}/libaqhbci.so
%{_libdir}/libaqhbci.la
%{_includedir}/aqhbci
%{_aclocaldir}/aqhbci.m4

%files backend-aqhbci-static
%defattr(644,root,root,755)
%{_libdir}/libaqhbci.a

%files backend-aqofxconnect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaqofxconnect.so.*.*.*
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/providers/aqofxconnect.so*
%{_libdir}/aqbanking/plugins/*/providers/aqofxconnect.xml
%dir %{_libdir}/aqbanking/plugins/*/wizards/aqofxconnect
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/wizards/aqofxconnect/aqofxconnect-qt3-wizard
%{_libdir}/aqbanking/plugins/*/wizards/aqofxconnect/qt_wizard.xml

%files backend-aqofxconnect-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqofxconnect-config
%attr(755,root,root) %{_libdir}/libaqofxconnect.so
%{_libdir}/libaqofxconnect.la
%{_includedir}/aqofxconnect
%{_aclocaldir}/aqofxconnect.m4

%files backend-aqofxconnect-static
%defattr(644,root,root,755)
%{_libdir}/libaqofxconnect.a

%files frontend-cbanking
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aqbanking-tool
%attr(755,root,root) %{_libdir}/libcbanking.so.*.*.*

%files frontend-cbanking-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcbanking.so
%{_libdir}/libcbanking.la
%{_includedir}/cbanking

%files frontend-cbanking-static
%defattr(644,root,root,755)
%{_libdir}/libcbanking.a

%if %{with gtk}
%files frontend-g2banking
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg2banking.so.*.*.*

%files frontend-g2banking-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g2banking-config
%attr(755,root,root) %{_libdir}/libg2banking.so
%{_libdir}/libg2banking.la
%{_includedir}/g2banking
%{_aclocaldir}/g2banking.m4

%files frontend-g2banking-static
%defattr(644,root,root,755)
%{_libdir}/libg2banking.a
%endif

%if %{with kde}
%files frontend-kbanking
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkbanking.so.*.*.*

%files frontend-kbanking-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbanking-config
%attr(755,root,root) %{_libdir}/libkbanking.so
%{_libdir}/libkbanking.la
%{_includedir}/kbanking
%{_aclocaldir}/kbanking.m4

%files frontend-kbanking-static
%defattr(644,root,root,755)
%{_libdir}/libkbanking.a
%endif

%files frontend-qbanking
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqbanking.so.*.*.*

%files frontend-qbanking-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qbanking-config
%attr(755,root,root) %{_libdir}/libqbanking.so
%{_libdir}/libqbanking.la
%{_includedir}/qbanking
%{_aclocaldir}/qbanking.m4

%files frontend-qbanking-static
%defattr(644,root,root,755)
%{_libdir}/libqbanking.a

%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/aqbanking
%{py_sitescriptdir}/aqbanking/*.py[co]
