%define		module		gnome-python
%define		pygtk_req	2:2.12.0
%define		pyorbit_req	2.14.2
Summary:	GNOME bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek GNOME
Name:		python-gnome
Version:	2.22.0
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.22/%{module}-%{version}.tar.bz2
# Source0-md5:	ff84c54314adec195149c59365e35a13
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	libbonoboui-devel >= 2.22.0
BuildRequires:	libgnomeui-devel >= 2.22.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-pygtk-devel >= %{pygtk_req}
BuildRequires:	python-pyorbit-devel >= %{pyorbit_req}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
%pyrequires_eq	python-modules
Requires:	%{name}-bonobo = %{version}-%{release}
Requires:	%{name}-gconf = %{version}-%{release}
Requires:	%{name}-vfs = %{version}-%{release}
Requires:	libgnomeui >= 2.22.0
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
Requires:	python-pygobject >= 2.14.0
Requires:	python-pyorbit >= %{pyorbit_req}

%description bonobo
Bonobo bindings for Python.

%description bonobo -l pl.UTF-8
Wiązania Pythona do biblioteki Bonobo.

%package bonobo-ui
Summary:	Bonobo User Interface bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki interfejsu użytkownika Bonobo
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-bonobo = %{version}-%{release}
Requires:	%{name}-canvas = %{version}-%{release}
Requires:	%{name}-gconf = %{version}-%{release}
Requires:	%{name}-vfs = %{version}-%{release}

%description bonobo-ui
Bonobo User Interface bindings for Python.

%description bonobo-ui -l pl.UTF-8
Wiązania Pythona do biblioteki interfejsu użytkownika Bonobo.

%package canvas
Summary:	GNOME Canvas bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GNOME Canvas
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description canvas
GNOME Canvas bindings for Python.

%description canvas -l pl.UTF-8
Wiązania Pythona do biblioteki GNOME Canvas.

%package gconf
Summary:	GConf bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GConf
Group:		Libraries/Python
Requires:	python-pygobject >= 2.14.0
Requires:	python-pyorbit >= %{pyorbit_req}

%description gconf
GConf bindings for Python.

%description gconf -l pl.UTF-8
Wiązania Pythona do biblioteki GConf.

%package ui
Summary:	GNOME User Interface bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki interfejsu użytkownika GNOME
Group:		Libraries/Python
Requires:	%{name}-bonobo-ui = %{version}-%{release}

%description ui
GNOME User Interface bindings for Python.

%description ui -l pl.UTF-8
Wiązania Pythona do biblioteki interfejsu użytkownika GNOME.

%package vfs
Summary:	GNOME VFS bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GNOME VFS
Group:		Libraries/Python
Requires:	%{name}-bonobo = %{version}-%{release}
Requires:	%{name}-gconf = %{version}-%{release}

%description vfs
GNOME VFS bindings for Python.

%description vfs -l pl.UTF-8
Wiązania Pythona do biblioteki GNOME VFS.

%package devel
Summary:	Development files for GNOME bindings for Python
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do GNOME
Group:		Libraries/Python
Requires:	%{name}-ui = %{version}-%{release}
Requires:	python-pygtk-devel >= %{pygtk_req}

%description devel
Development files for GNOME bindings for Python.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do GNOME.

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

%build
./waf configure \
	--prefix %{_prefix} \
	--libdir %{_libdir}
./waf build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

./waf install \
	--destdir $RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/{*.la,*/{*.la,*.py}}
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%dir %{py_sitedir}/gtk-2.0/gnome
%{py_sitedir}/gtk-2.0/gnome/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/_gnome.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-python-2.0
%dir %{_datadir}/pygtk/2.0/argtypes
%{_datadir}/pygtk/2.0/argtypes/bonobo-arg-types.py*
%{_datadir}/pygtk/2.0/argtypes/gconf-arg-types.py*
%{pydefsdir}/*.defs
%{_pkgconfigdir}/gnome-python-2.0.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

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
%{py_sitedir}/gtk-2.0/gnome/vfs.py[co]
%dir %{py_sitedir}/gtk-2.0/gnomevfs
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomevfs/_gnomevfs.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomevfs/gnomevfsbonobo.so
%{py_sitedir}/gtk-2.0/gnomevfs/__init__.py[co]
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/libpythonmethod.so
