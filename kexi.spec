Summary:	Kexi - an integrated environment for managing data
Summary(pl):	Kexi - zintegrowane ¶rodowisko do zarz±dzania danymi
Name:		kexi
Version:	0.1
%define		_beta	beta5
%define		_snap	20041208
Release:	0.%{_snap}.3
License:	GPL v2
Group:		Applications/Databases
#Source0:	ftp://ftp.kde.org/pub/kde/unstable/apps/KDE3.x/office/%{name}-%{version}%{_beta}.tar.bz2
Source0:	kexi-0.1-cvs%{_snap}.tar.bz2
# Source0-md5:	a7a994493574ded550fc44420fb29eef
URL:		http://www.kexi-project.org/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	libpqxx-devel
BuildRequires:	libxml2-progs
BuildRequires:	mysql-devel
BuildRequires:	unsermake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kexi is an integrated environment for managing data. It helps creating
database schemas, inserting, querying and processing data.

%description -l pl
Kexi to zintegrowane ¶rodowisko do zarz±dzania danymi. Pomaga przy
tworzeniu schematów baz danych oraz wstawianiu, odpytywaniu i
przetwarzaniu danych.

%package backend-mysql
Summary:        mySQL backend for Kexi
Summary(pl):    Backend mySQL dla Kexi
Group:          Applications/Databases
Requires:       %{name} = %{version}-%{release}

%description backend-mysql
This package allows Kexi to access mySQL servers.

%description backend-mysql -l pl
Ten pakiet pozwala na ³±czenie siê Kexi z serwerem mySQL.

%package backend-pgsql
Summary:        PostgreSQL backend for Kexi
Summary(pl):    Backend PostgreSQL dla Kexi
Group:          Applications/Databases
Requires:       %{name} = %{version}-%{release}

%description backend-pgsql
This package allows Kexi to access PosgtresSQL servers.

%description backend-pgsql -l pl
Ten pakiet pozwala na ³±czenie siê Kexi z serwerem PostgreSQL.

%prep
%setup -q -n %{name}-%{version}-cvs

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
%doc kexi/CHANGES AUTHORS README
%attr(755,root,root) %{_bindir}/*
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
%{_libdir}/kde3/kexihandler_migration.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_migration.so
%{_libdir}/kde3/kexihandler_query.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_query.so
%{_libdir}/kde3/kexihandler_relation.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_relation.so
%{_libdir}/kde3/kexihandler_table.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_table.so
%{_libdir}/kde3/keximigrate_pqxxmigrate.la
%attr(755,root,root) %{_libdir}/kde3/keximigrate_pqxxmigrate.so
%{_libdir}/kde3/stdwidgets.la
%attr(755,root,root) %{_libdir}/kde3/stdwidgets.so
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
%dir %{_datadir}/apps/kexi
%dir %{_datadir}/apps/kexi/icons
%{_datadir}/apps/kexi/icons/crystalsvg
%{_datadir}/apps/kexi/pics
%{_datadir}/apps/kexi/*.rc
%{_datadir}/apps/kformdesigner
%{_datadir}/apps/kformdesigner_part
%{_desktopdir}/kexi.desktop
%{_desktopdir}/kformdesigner.desktop
%{_datadir}/config/kexirc
%dir %{_datadir}/config/magic
%{_datadir}/config/magic/kexi.magic
%{_iconsdir}/crystalsvg/32x32/apps/kexi.png
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_shortcut.png
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_sqlite.png
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_sqlite2.png
%{_iconsdir}/crystalsvg/scalable/apps/kexi.svgz	       
%{_datadir}/mimelnk/application/x-kexiproject-shortcut.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite2.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite3.desktop
%{_datadir}/services/kexi
%{_datadir}/services/*.desktop
%{_datadir}/services/kformdesigner
%{_datadir}/servicetypes/*.desktop

%files backend-mysql
%{_libdir}/kde3/kexidb_mysqldriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_mysqldriver.so

%files backend-pgsql
%{_libdir}/kde3/kexidb_pqxxsqldriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_pqxxsqldriver.so
