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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
#attr(755,root,root) %{_bindir}/*
#{_datadir}/%{name}
