Summary:	Kexi - an integrated environment for managing data
Summary(pl.UTF-8):	Kexi - zintegrowane środowisko do zarządzania danymi
Name:		kexi
Version:	0.9
Release:	7
License:	GPL v2
Group:		Applications/Databases
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/database/%{name}-%{version}.tar.bz2
# Source0-md5:	c599372caca7a4c8976a4c0258145035
URL:		http://www.kexi-project.org/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	libpqxx-devel
BuildRequires:	mysql-devel
BuildRequires:	unsermake
Provides:	koffice-kexi
Obsoletes:	koffice-kexi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kexi is an integrated environment for managing data. It helps creating
database schemas, inserting, querying and processing data.

%description -l pl.UTF-8
Kexi to zintegrowane środowisko do zarządzania danymi. Pomaga przy
tworzeniu schematów baz danych oraz wstawianiu, odpytywaniu i
przetwarzaniu danych.

%package backend-mysql
Summary:	mySQL backend for Kexi
Summary(pl.UTF-8):	Backend mySQL dla Kexi
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description backend-mysql
This package allows Kexi to access mySQL servers.

%description backend-mysql -l pl.UTF-8
Ten pakiet pozwala na łączenie się Kexi z serwerem mySQL.

%package backend-pgsql
Summary:	PostgreSQL backend for Kexi
Summary(pl.UTF-8):	Backend PostgreSQL dla Kexi
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description backend-pgsql
This package allows Kexi to access PosgtresSQL servers.

%description backend-pgsql -l pl.UTF-8
Ten pakiet pozwala na łączenie się Kexi z serwerem PostgreSQL.

%package devel
Summary:	Developement files for Kexi
Summary(pl.UTF-8):	Pliki nagłówkowe dla Kexi
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel

%description devel
This package contains the development header files for applications
using Kexi.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe dla aplikacji korzystających
z Kexi.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake

%configure \
	--with-qt-libraries=%{_libdir} \
	--with-pgsqllibdir=%{_libdir} \
	--with-pqxxlibdir=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_datadir}{/applnk/Utilities/kformdesigner.desktop,/applications/kde/kexi.desktop} \
	$RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libkdeinit_kexi.la
%attr(755,root,root) %{_libdir}/libkdeinit_kexi.so
%{_libdir}/libkexicore.la
%attr(755,root,root) %{_libdir}/libkexicore.so.*.*.*
%{_libdir}/libkexidatatable.la
%attr(755,root,root) %{_libdir}/libkexidatatable.so.*.*.*
%{_libdir}/libkexidb.la
%attr(755,root,root) %{_libdir}/libkexidb.so.*.*.*
%{_libdir}/libkexidbparser.la
%attr(755,root,root) %{_libdir}/libkexidbparser.so.*.*.*
%{_libdir}/libkexiextendedwidgets.la
%attr(755,root,root) %{_libdir}/libkexiextendedwidgets.so.*.*.*
%{_libdir}/libkexiformutils.la
%attr(755,root,root) %{_libdir}/libkexiformutils.so.*.*.*
%{_libdir}/libkexiguiutils.la
%attr(755,root,root) %{_libdir}/libkexiguiutils.so.*.*.*
%{_libdir}/libkeximain.la
%attr(755,root,root) %{_libdir}/libkeximain.so.*.*.*
%{_libdir}/libkeximigrate.la
%attr(755,root,root) %{_libdir}/libkeximigrate.so.*.*.*
%{_libdir}/libkexipropertyeditor.la
%attr(755,root,root) %{_libdir}/libkexipropertyeditor.so.*.*.*
%{_libdir}/libkexirelationsview.la
%attr(755,root,root) %{_libdir}/libkexirelationsview.so.*.*.*
%{_libdir}/libkexisql2.la
%attr(755,root,root) %{_libdir}/libkexisql2.so.*.*.*
%{_libdir}/libkexisql3.la
%attr(755,root,root) %{_libdir}/libkexisql3.so.*.*.*
%{_libdir}/libkformdesigner.la
%attr(755,root,root) %{_libdir}/libkformdesigner.so.*.*.*
%{_libdir}/kde3/containers.la
%attr(755,root,root) %{_libdir}/kde3/containers.so
%{_libdir}/kde3/kexi.la
%attr(755,root,root) %{_libdir}/kde3/kexi.so
%{_libdir}/kde3/kexidb_sqlite2driver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_sqlite2driver.so
%{_libdir}/kde3/kexidb_sqlite3driver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_sqlite3driver.so
%{_libdir}/kde3/kexidbwidgets.la
%attr(755,root,root) %{_libdir}/kde3/kexidbwidgets.so
%{_libdir}/kde3/libkformdesigner_part.la
%attr(755,root,root) %{_libdir}/kde3/libkformdesigner_part.so
%{_libdir}/kde3/kexihandler_form.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_form.so
%{_libdir}/kde3/kexihandler_script.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_script.so
%{_libdir}/kde3/kexihandler_migration.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_migration.so
%{_libdir}/kde3/kexihandler_query.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_query.so
%{_libdir}/kde3/kexihandler_relation.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_relation.so
%{_libdir}/kde3/kexihandler_table.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_table.so
%{_libdir}/kde3/stdwidgets.la
%attr(755,root,root) %{_libdir}/kde3/stdwidgets.so
%dir %{_datadir}/apps/kexi
%dir %{_datadir}/apps/kexi/icons
%{_datadir}/apps/kexi/icons/crystalsvg
%{_datadir}/apps/kexi/pics
%{_datadir}/apps/kexi/*.rc
%{_datadir}/apps/kexi/readme_en
%{_datadir}/apps/kformdesigner
%{_datadir}/apps/kformdesigner_part
%{_desktopdir}/kexi.desktop
%{_desktopdir}/kformdesigner.desktop
%{_datadir}/config/kexirc
%{_datadir}/config/magic/kexi.magic
%{_iconsdir}/crystalsvg/*/apps/kexi.png
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_shortcut.png
%{_iconsdir}/crystalsvg/*/mimetypes/kexiproject_sqlite.png
%{_iconsdir}/crystalsvg/*/mimetypes/kexiproject_sqlite2.png
%{_iconsdir}/crystalsvg/scalable/apps/kexi.svgz
%{_datadir}/mimelnk/application/x-kexiproject-shortcut.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite2.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite3.desktop
%{_datadir}/services/kexi
%{_datadir}/services/kexidb_sqlite2driver.desktop
%{_datadir}/services/kexidb_sqlite3driver.desktop
%{_datadir}/services/kformdesigner_part.desktop
%{_datadir}/services/kformdesigner
%{_datadir}/servicetypes/*.desktop

%files backend-mysql
%defattr(644,root,root,755)
%{_libdir}/kde3/kexidb_mysqldriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_mysqldriver.so
%{_libdir}/kde3/keximigrate_mysql.la
%attr(755,root,root) %{_libdir}/kde3/keximigrate_mysql.so
%{_datadir}/services/kexidb_mysqldriver.desktop
%{_datadir}/services/keximigrate_mysql.desktop

%files backend-pgsql
%defattr(644,root,root,755)
%{_libdir}/kde3/kexidb_pqxxsqldriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_pqxxsqldriver.so
%{_libdir}/kde3/keximigrate_pqxx.la
%attr(755,root,root) %{_libdir}/kde3/keximigrate_pqxx.so
%{_datadir}/services/kexidb_pqxxsqldriver.desktop
%{_datadir}/services/keximigrate_pqxx.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkexicore.so
%attr(755,root,root) %{_libdir}/libkexidatatable.so
%attr(755,root,root) %{_libdir}/libkexidb.so
%attr(755,root,root) %{_libdir}/libkexidbparser.so
%attr(755,root,root) %{_libdir}/libkexiextendedwidgets.so
%attr(755,root,root) %{_libdir}/libkexiformutils.so
%attr(755,root,root) %{_libdir}/libkexiguiutils.so
%attr(755,root,root) %{_libdir}/libkeximain.so
%attr(755,root,root) %{_libdir}/libkeximigrate.so
%attr(755,root,root) %{_libdir}/libkexipropertyeditor.so
%attr(755,root,root) %{_libdir}/libkexirelationsview.so
%attr(755,root,root) %{_libdir}/libkexisql2.so
%attr(755,root,root) %{_libdir}/libkexisql3.so
%attr(755,root,root) %{_libdir}/libkformdesigner.so
%dir %{_includedir}/kexidb
%{_includedir}/kexidb/*
