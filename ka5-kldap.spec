%define		kdeappsver	21.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kldap
Summary:	LDAP access API for KDE
Name:		ka5-%{kaname}
Version:	21.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	67b79917dba53cba1c516eb7ae52e895
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Keychain-devel >= 0.12.0
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
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
%cmake -G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{ko,sr}
%find_lang %{kaname}_qt --with-qm --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}_qt.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5Ldap.so.5
%attr(755,root,root) %{_libdir}/libKF5Ldap.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/ldap.so
%{_datadir}/kservices5/ldap.protocol
%{_datadir}/kservices5/ldaps.protocol
%{_datadir}/qlogging-categories5/kldap.categories
%{_datadir}/qlogging-categories5/kldap.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KLDAP
%{_includedir}/KF5/kldap_version.h
%{_libdir}/cmake/KF5Ldap
%{_libdir}/libKF5Ldap.so
%{_libdir}/qt5/mkspecs/modules/qt_Ldap.pri
