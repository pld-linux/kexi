Summary:	Kexi is an integrated environment for managing data
Name:		kexi
Version:	0.1
%define		_beta	beta3
Release:	0.%{_beta}.1
License:	GPL v2
Group:		Applications/Databases
Source0:	ftp://ftp.kde.org/pub/kde/unstable/apps/KDE3.x/office/%{name}-%{version}%{_beta}.tar.bz2
# Source0-md5:	90ddba0742b9d1552d82d9f02e16d555
URL:		http://www.kexi-project.org/
#BuildRequires:	doxygen
BuildRequires:	kdelibs-devel
BuildRequires:	libpqxx-devel
BuildRequires:	libxml2-progs
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
#BuildRequires:	qsa
#BuildRequires:	unixODBC-devel (it needs fixes in kexi/kexidb/drivers/configure.in*)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kexi is an integrated environment for managing data. It helps creating
database schemas, inserting, querying and processing data.

%prep
%setup -q -n %{name}-%{version}%{_beta}

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_datadir}/applnk/{Office/kexi.desktop,Utilities/kformdesigner.desktop} \
	$RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc kexi/CHANGES AUTHORS README
%attr(755,root,root) %{_bindir}/kexi
%attr(755,root,root) %{_bindir}/kformdesigner
%{_libdir}/kde3/containers.la
%attr(755,root,root) %{_libdir}/kde3/containers.so
%{_libdir}/kde3/kexi.la
%attr(755,root,root) %{_libdir}/kde3/kexi.so
%{_libdir}/kde3/kexidb_mysqldriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_mysqldriver.so
%{_libdir}/kde3/kexidb_pqxxsqldriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_pqxxsqldriver.so
%{_libdir}/kde3/kexidb_sqlitedriver.la
%attr(755,root,root) %{_libdir}/kde3/kexidb_sqlitedriver.so
%{_libdir}/kde3/kexihandler_form.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_form.so
%{_libdir}/kde3/kexihandler_query.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_query.so
%{_libdir}/kde3/kexihandler_relation.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_relation.so
%{_libdir}/kde3/kexihandler_table.la
%attr(755,root,root) %{_libdir}/kde3/kexihandler_table.so
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
%{_libdir}/libkexipropertyeditor.la
%attr(755,root,root) %{_libdir}/libkexipropertyeditor.so.*.*.*
%{_libdir}/libkexirelationsview.la
%attr(755,root,root) %{_libdir}/libkexirelationsview.so.*.*.*
%{_libdir}/libkexisql.la
%attr(755,root,root) %{_libdir}/libkexisql.so.*.*.*
%{_libdir}/libkformeditor.la
%attr(755,root,root) %{_libdir}/libkformeditor.so.*.*.*
%dir %{_datadir}/apps/kexi
%dir %{_datadir}/apps/kexi/icons
%{_datadir}/apps/kexi/icons/crystalsvg
%{_datadir}/apps/kexi/pics
%{_datadir}/apps/kexi/*.rc
%{_datadir}/apps/kformdesigner
%{_desktopdir}/kexi.desktop
%{_desktopdir}/kformdesigner.desktop
%{_datadir}/config/kexirc
%dir %{_datadir}/config/magic
%{_datadir}/config/magic/kexi.magic
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_shortcut.png
%{_iconsdir}/crystalsvg/32x32/mimetypes/kexiproject_sqlite.png
%{_iconsdir}/crystalsvg/scalable/apps/kexi.svgz	       
%{_datadir}/mimelnk/application/x-kexiproject-shortcut.desktop
%{_datadir}/mimelnk/application/x-kexiproject-sqlite.desktop
%{_datadir}/services/kexi
%{_datadir}/services/*.desktop
%{_datadir}/services/kformeditor
%{_datadir}/servicetypes/*.desktop
