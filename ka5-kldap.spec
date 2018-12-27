%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kldap
Summary:	LDAP access API for KDE
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d0f4cc54408a59b277975f8b74ed4d7f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-kcalcore-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcompletion-devel >= 5.51.0
BuildRequires:	kf5-kdoctools-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kldap - an LDAP access API for KDE.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname}_qt --with-qm --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}_qt.lang
%defattr(644,root,root,755)
/etc/xdg/kldap.categories
/etc/xdg/kldap.renamecategories
%attr(755,root,root) %ghost %{_libdir}/libKF5Ldap.so.5
%attr(755,root,root) %{_libdir}/libKF5Ldap.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/ldap.so
%{_datadir}/kservices5/ldap.protocol
%{_datadir}/kservices5/ldaps.protocol

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KLDAP
%{_includedir}/KF5/kldap_version.h
%{_libdir}/cmake/KF5Ldap
%attr(755,root,root) %{_libdir}/libKF5Ldap.so
%{_libdir}/qt5/mkspecs/modules/qt_Ldap.pri
