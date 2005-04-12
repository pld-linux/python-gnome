%define		module		gnome-python
%define		pygtk_req	2:2.6.0
%define		pyorbit_req	2.0.1
Summary:	GNOME bindings for Python
Summary(pl):	Wi±zania Pythona do bibliotek GNOME
Name:		python-gnome
Version:	2.10.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-python/2.10/%{module}-%{version}.tar.bz2
# Source0-md5:	018c210bc5e2e9be36791bede9dbdc73
BuildRequires:	GConf2-devel >= 2.9.90
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	libbonobo-devel >= 2.8.1
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-pyorbit-devel >= %{pyorbit_req}
BuildRequires:	python-pygtk-devel >= %{pygtk_req}
BuildRequires:	rpmbuild(macros) >= 1.197
%pyrequires_eq	python-modules
Requires:	python-pygtk-gobject >= %{pygtk_req}
Obsoletes:	gnome-python
Obsoletes:	gnome-python-nautilus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
GNOME bindings for Python.

%description -l pl
Wi±zania Pythona do bibliotek GNOME.

%package bonobo
Summary:	Bonobo bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki Bonobo
Group:		Libraries/Python
Requires:	python-pygtk-gobject >= %{pygtk_req}
Requires:	python-pyorbit >= %{pyorbit_req}

%description bonobo
Bonobo bindings for Python.

%description bonobo -l pl
Wi±zania Pythona do biblioteki Bonobo.

%package bonobo-ui
Summary:	Bonobo User Interface bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki interfejsu u¿ytkownika Bonobo
Group:		Libraries/Python
Requires:	%{name}-bonobo = %{version}-%{release}
Requires:	%{name}-canvas = %{version}-%{release}

%description bonobo-ui
Bonobo User Interface bindings for Python.

%description bonobo-ui -l pl
Wi±zania Pythona do biblioteki interfejsu u¿ytkownika Bonobo.

%package canvas
Summary:	GNOME Canvas bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki GNOME Canvas
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description canvas
GNOME Canvas bindings for Python.

%description canvas -l pl
Wi±zania Pythona do biblioteki GNOME Canvas.

%package gconf
Summary:	GConf bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki GConf
Group:		Libraries/Python
Requires:	python-pygtk-gobject >= %{pygtk_req}

%description gconf
GConf bindings for Python.

%description gconf -l pl
Wi±zania Pythona do biblioteki GConf.

%package ui
Summary:	GNOME User Interface bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki interfejsu u¿ytkownika GNOME
Group:		Libraries/Python
Requires:	%{name}-bonobo-ui = %{version}-%{release}

%description ui
GNOME User Interface bindings for Python.

%description ui -l pl
Wi±zania Pythona do biblioteki interfejsu u¿ytkownika GNOME.

%package vfs
Summary:	GNOME VFS bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki GNOME VFS
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description vfs
GNOME VFS bindings for Python.

%description vfs -l pl
Wi±zania Pythona do biblioteki GNOME VFS.

%package devel
Summary:	Development files for GNOME bindings for Python
Summary(pl):	Pliki programistyczne wi±zañ Pythona do GNOME
Group:		Libraries/Python
Requires:	%{name}-bonobo = %{version}-%{release}
Requires:	%{name}-bonobo-ui = %{version}-%{release}
Requires:	%{name}-canvas = %{version}-%{release}
Requires:	%{name}-gconf = %{version}-%{release}
Requires:	%{name}-ui = %{version}-%{release}
Requires:	%{name}-vfs = %{version}-%{release}
Requires:	python-pygtk-devel >= %{pygtk_req}

%description devel
Development files for GNOME bindings for Python.

%description devel -l pl
Pliki programistyczne wi±zañ Pythona do GNOME.

%prep
%setup -q -n %{module}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/{*.la,*/{*.la,*.py}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%dir %{py_sitedir}/gtk-2.0/gnome
%{py_sitedir}/gtk-2.0/gnome/__init__.py?
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/_gnome*.so
%dir %{_datadir}/pygtk/2.0/argtypes

%files bonobo
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/bonobo
%{py_sitedir}/gtk-2.0/bonobo/__init__.py?
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/_bonobo*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/activation*.so
%{_datadir}/pygtk/2.0/argtypes/bonobo-arg-types.py*

%files bonobo-ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/ui*.so

%files canvas
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomecanvas*.so
%{py_sitedir}/gtk-2.0/gnome/canvas.py[co]

%files gconf
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gconf*.so
%{_datadir}/pygtk/2.0/argtypes/gconf-arg-types.py*

%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/ui*.so

%files vfs
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomevfs*.so
%{py_sitedir}/gtk-2.0/gnome/vfs.py[co]

%files devel
%defattr(644,root,root,755)
%{pydefsdir}/*
%{_pkgconfigdir}/*
