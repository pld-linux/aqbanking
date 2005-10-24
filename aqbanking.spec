Summary:	A library for online banking functions and financial data import/export
Summary(pl):	Biblioteka do funkcji bankowych online oraz importu/eksportu danych finansowych
Name:		aqbanking
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/aqbanking/%{name}-%{version}.tar.gz
# Source0-md5:	b6afa0facd32be6f57b3b8f802a2eb6c
Patch0:		%{name}-link.patch
URL:		http://www.aquamaniac.de/aqbanking/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gwenhywfar-devel >= 1.14.0
BuildRequires:	ktoblzcheck-devel
BuildRequires:	libofx-devel >= 0.7.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	python-ctypes
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
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

%description -l pl
Celem projektu AqBanking jest dostarczenie warstwy po¶redniej miêdzy
programem a ró¿nymi bibliotekami us³ug bankowych online (np. AqHBCI).
Pierwszy ju¿ obs³ugiwany backend to AqHBCI - biblioteka implementuj±ca
klienta niemieckiego protoko³u HBCI (Home Baking Computer Interface).
Ponadto Aqbanking dostarcza ró¿ne wtyczki upraszczaj±ce importowanie i
eksportowanie danych finansowych. Aktualnie istniej± wtyczki do
importu nastêpuj±cych formatów: DTAUS (niemiecki format finansowy),
SWIFT (MT940 oraz MT942).

%package devel
Summary:	Header files for AqBanking library
Summary(pl):	Pliki nag³ówkowe biblioteki AqBanking
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gwenhywfar-devel >= 1.14.0
# for libaqbankingpp only
#Requires:	libstdc++-devel

%description devel
Header files for AqBanking library.

%description devel -l pl
Pliki nag³ówkowe biblioteki AqBanking.

%package static
Summary:	Static AqBanking libraries
Summary(pl):	Statyczne biblioteki AqBanking
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AqBanking libraries.

%description static -l pl
Statyczne biblioteki AqBanking.

%package -n python-%{name}
Summary:	Python binding for AqBanking library
Summary(pl):	Wi±zanie Pythona do biblioteki AqBanking
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-ctypes

%description -n python-%{name}
Python binding for AqBanking library.

%description -n python-%{name} -l pl
Wi±zanie Pythona do biblioteki AqBanking.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-libofx \
	--enable-python \
	--enable-static

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog README TODO
%attr(755,root,root) %{_bindir}/aqbanking-tool
%attr(755,root,root) %{_libdir}/libaqbanking.so.*.*.*
%attr(755,root,root) %{_libdir}/libaqbankingpp.so.*.*.*
%dir %{_libdir}/aqbanking
%dir %{_libdir}/aqbanking/plugins
%dir %{_libdir}/aqbanking/plugins/*
%dir %{_libdir}/aqbanking/plugins/*/bankinfo
%dir %{_libdir}/aqbanking/plugins/*/imexporters
%attr(755,root,root) %{_libdir}/aqbanking/plugins/*/*/*.so*
%{_libdir}/aqbanking/plugins/*/*/*.xml
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libaqbanking.a
%{_libdir}/libaqbankingpp.a

%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/aqbanking
%{py_sitescriptdir}/aqbanking/*.py[co]
