%define		module		gnome-python
%define		pygobject_ver	2.17.0
%define		pygtk_ver	2:2.16.0
%define		pyorbit_ver	2.14.2
Summary:	GNOME bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek GNOME
Name:		python-gnome
Version:	2.28.1
Release:	12
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.28/%{module}-%{version}.tar.bz2
# Source0-md5:	a17ad952813ed86f520de8e07194a2bf
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	libbonobo-devel >= 2.22.0
BuildRequires:	libbonoboui-devel >= 2.22.0
BuildRequires:	libgnome-devel >= 2.22.0
BuildRequires:	libgnomecanvas-devel >= 2.8.0
BuildRequires:	libgnomeui-devel >= 2.22.0
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-pygobject-devel >= %{pygobject_ver}
BuildRequires:	python-pygtk-devel >= %{pygtk_ver}
BuildRequires:	python-pyorbit-devel >= %{pyorbit_ver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}
Requires:	libgnome-libs >= 2.22.0
Requires:	python-pygobject >= %{pygobject_ver}
Obsoletes:	gnome-python
Obsoletes:	gnome-python-nautilus
Obsoletes:	python-gnome-nautilus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
GNOME bindings for Python.

%description -l pl.UTF-8
Wiązania Pythona do bibliotek GNOME.

%package bonobo
Summary:	Bonobo bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Bonobo
Group:		Libraries/Python
Requires:	libbonobo >= 2.22.0
Requires:	python-pygobject >= %{pygobject_ver}
Requires:	python-pyorbit >= %{pyorbit_ver}

%description bonobo
Bonobo bindings for Python.

%description bonobo -l pl.UTF-8
Wiązania Pythona do biblioteki Bonobo.

%package bonobo-ui
Summary:	Bonobo User Interface bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki interfejsu użytkownika Bonobo
Group:		Libraries/Python
Requires:	%{name}-bonobo = %{version}-%{release}
Requires:	%{name}-canvas = %{version}-%{release}
Requires:	libbonoboui >= 2.22.0
Requires:	libgnome-libs >= 2.22.0
Requires:	python-pygobject >= %{pygobject_ver}
Requires:	python-pygtk-gtk >= %{pygtk_ver}

%description bonobo-ui
Bonobo User Interface bindings for Python.

%description bonobo-ui -l pl.UTF-8
Wiązania Pythona do biblioteki interfejsu użytkownika Bonobo.

%package canvas
Summary:	GNOME Canvas bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GNOME Canvas
Group:		Libraries/Python
Requires:	%{name}-common = %{version}-%{release}
Requires:	libgnomecanvas >= 2.8.0
Requires:	python-pygobject >= %{pygobject_ver}
Requires:	python-pygtk-gtk >= %{pygtk_ver}

%description canvas
GNOME Canvas bindings for Python.

%description canvas -l pl.UTF-8
Wiązania Pythona do biblioteki GNOME Canvas.

%package gconf
Summary:	GConf bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GConf
Group:		Libraries/Python
Requires:	%{name}-common = %{version}-%{release}
Requires:	GConf2-libs >= 2.22.0
Requires:	python-pygobject >= %{pygobject_ver}

%description gconf
GConf bindings for Python.

%description gconf -l pl.UTF-8
Wiązania Pythona do biblioteki GConf.

%package ui
Summary:	GNOME User Interface bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki interfejsu użytkownika GNOME
Group:		Libraries/Python
Requires:	%{name}-bonobo-ui = %{version}-%{release}
Requires:	%{name}-canvas = %{version}-%{release}
Requires:	libgnomeui >= 2.22.0
Requires:	python-pygobject >= %{pygobject_ver}
Requires:	python-pygtk-gtk >= %{pygtk_ver}

%description ui
GNOME User Interface bindings for Python.

%description ui -l pl.UTF-8
Wiązania Pythona do biblioteki interfejsu użytkownika GNOME.

%package vfs
Summary:	GNOME VFS bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GNOME VFS
Group:		Libraries/Python
Requires:	%{name}-common = %{version}-%{release}
Requires:	gnome-vfs2-libs >= 2.22.0
Requires:	libbonobo >= 2.22.0
Requires:	python-pygobject >= %{pygobject_ver}
Requires:	python-pyorbit >= %{pyorbit_ver}

%description vfs
GNOME VFS bindings for Python.

%description vfs -l pl.UTF-8
Wiązania Pythona do biblioteki GNOME VFS.

%package common
Summary:	Common files for Python GNOME bindings
Summary(pl.UTF-8):	Pliki wspólne wiązań Pythona do GNOME
Group:		Libraries/Python
Requires:	python-libs >= 1:2.3.2
Requires:	python-pygobject >= %{pygobject_ver}

%description common
Common files for Python GNOME bindings.

%description common -l pl.UTF-8
Pliki wspólne wiązań Pythona do GNOME.

%package devel
Summary:	Development files for Python GNOME bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do GNOME
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-bonobo = %{version}-%{release}
Requires:	%{name}-bonobo-ui = %{version}-%{release}
Requires:	%{name}-canvas = %{version}-%{release}
Requires:	%{name}-gconf = %{version}-%{release}
Requires:	%{name}-ui = %{version}-%{release}
Requires:	%{name}-vfs = %{version}-%{release}
Requires:	gnome-vfs2-devel >= 2.22.0
Requires:	python-pygtk-devel >= %{pygtk_ver}

%description devel
Development files for Python GNOME bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do GNOME.

%package apidocs
Summary:	API documentation for Python GNOME bindings
Summary(pl.UTF-8):	Dokumentacja API wiązań Pythona do GNOME
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python GNOME bindings.

%description apidocs -l pl.UTF-8
Dokumentacja API wiązań Pythona do GNOME.

%package examples
Summary:	Example programs for python-gnome
Summary(pl.UTF-8):	Przykładowe programy do python-gnome
Group:		Libraries/Python
Requires:	%{name}-devel = %{version}-%{release}

%description examples
This package contains example programs for python-gnome.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy dla python-gnome.

%prep
%setup -q -n %{module}-%{version}

%{__sed} -i -e 's,${DATADIR}/gtk-doc/html/,%{_gtkdocdir}/,' docs/gnomevfs/wscript

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python}\1,' \
      examples/*/*.py \
      examples/*/*/*.py

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./waf configure \
	--prefix %{_prefix} \
	--libdir %{_libdir}
./waf build \
	--verbose

%install
rm -rf $RPM_BUILD_ROOT
./waf install \
	--destdir $RPM_BUILD_ROOT

# waf is sucker, and does not +x executables
find $RPM_BUILD_ROOT -name '*.so' | xargs chmod a+rx

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{py_sitedir}/gtk-2.0/gnome/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/_gnome.so

%files bonobo
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/bonobo
%{py_sitedir}/gtk-2.0/bonobo/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/_bonobo.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/activation.so

%files bonobo-ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/ui.so

%files canvas
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomecanvas.so
%{py_sitedir}/gtk-2.0/gnome/canvas.py[co]

%files gconf
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gconf.so

%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/ui.so

%files vfs
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gnomevfs
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomevfs/_gnomevfs.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomevfs/gnomevfsbonobo.so
%{py_sitedir}/gtk-2.0/gnomevfs/__init__.py[co]
%{py_sitedir}/gtk-2.0/gnome/vfs.py[co]
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/libpythonmethod.so

%files common
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{py_sitedir}/gtk-2.0/gnome

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-python-2.0
%dir %{_datadir}/pygtk/2.0/argtypes
%{_datadir}/pygtk/2.0/argtypes/bonobo-arg-types.py*
%{_datadir}/pygtk/2.0/argtypes/gconf-arg-types.py*
%{pydefsdir}/*.defs
%{_pkgconfigdir}/gnome-python-2.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pygnomevfs

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
