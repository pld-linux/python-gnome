
%include	/usr/lib/rpm/macros.python

%define		module	gnome-python

Summary:	Gnome bindings for Python
Summary(pl):	Wi您ania Pythona do bibliotek Gnome
Name:		python-gnome
Version:	1.99.13
Release:	4
License:	GPL
Group:		Libraries/Python
Source0:	ftp://ftp.gnome.org/pub/GNOME/2.0.2/sources/%{module}/%{module}-%{version}.tar.gz
BuildRequires:	gnome-panel-devel >= 2.0.9
BuildRequires:	gnome-vfs2-devel >= 2.0.4
BuildRequires:	libgtkhtml-devel >= 2.0.2
BuildRequires:	libzvt-devel >= 2.0.1
BuildRequires:	nautilus-devel >= 2.0.7
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-orbit-devel >= 1.99.0
BuildRequires:	python-pygtk-devel >= 1.99.13
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:		python-pygtk-gobject
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
Gnome bindings for Python.

%description -l pl
Wi您ania Pythona do bibliotek Gnome.

%package bonobo
Summary:	Bonobo bindings for Python
Summary(pl):	Wi您ania Pythona do biblioteki Bonobo
Group:		Libraries/Python
Requires:	python-pygtk-gobject

%description bonobo
Bonobo bindings for Python.

%description bonobo -l pl
Wi您ania Pythona do biblioteki Bonobo.

%package bonobo-ui
Summary:	Bonobo User Interface bindings for Python
Summary(pl):	Wi您ania Pythona do biblioteki interfejsu u篡tkownika Bonobo
Group:		Libraries/Python
Requires:	%{name}-canvas = %{version}
Requires:	%{name}-bonobo = %{version}

%description bonobo-ui
Bonobo User Interface bindings for Python.

%description bonobo-ui -l pl
Wi您ania Pythona do biblioteki interfejsu u篡tkownika Bonobo.

%package applet
Summary:	Gnome Applet bindings for Python
Summary(pl):	Wi您ania Pythona do biblioteki Gnome Applet
Group:		Libraries/Python
Requires:	python-pygtk-gtk
Requires:	%{name} = %{version}

%description applet
Gnome Applet bindings for Python.

%description applet -l pl
Wi您ania Pythona do biblioteki Gnome Applet.

%package canvas
Summary:	Gnome Canvas bindings for Python
Summary(pl):	Wi您ania Pythona do biblioteki Gnome Canvas
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description canvas
Gnome Canvas bindings for Python.

%description canvas -l pl
Wi您ania Pythona do biblioteki Gnome Canvas.

%package gconf
Summary:	GConf bindings for Python
Summary(pl):	Wi您ania Pythona do biblioteki GConf
Group:		Libraries/Python
Requires:	python-pygtk-gobject

%description gconf
GConf bindings for Python.

%description gconf -l pl
Wi您ania Pythona do biblioteki GConf.

%package gtkhtml
Summary:	GtkHtml bindings for Python
Summary(pl):	Wi您ania Pythona do biblioteki GtkHtml
Group:		Libraries/Python
Requires:	python-pygtk-gobject

%description gtkhtml
GtkHtml bindings for Python.

%description gtkhtml -l pl
Wi您ania Pythona do biblioteki GtkHtml.

%package nautilus
Summary:	Nautilus bindings for Python
Summary(pl):	Wi您ania Pythona do Nautilusa
Group:		Libraries/Python
Requires:	%{name}-bonobo-ui = %{version}

%description nautilus
Nautilus bindings for Python.

%description nautilus -l pl
Wi您ania Pythona do Nautilusa.

%package ui
Summary:	Gnome User Interface bindings for Python
Summary(pl):	Wi您ania Pythona do biblioteki interfejsu u篡tkownika Gnome
Group:		Libraries/Python
Requires:	%{name}-bonobo-ui = %{version}

%description ui
Gnome User Interface bindings for Python.

%description ui -l pl
Wi您ania Pythona do biblioteki interfejsu u篡tkownika Gnome.

%package vfs
Summary:	Gnome VFS bindings for Python
Summary(pl):	Wi您ania Pythona do biblioteki Gnome VFS
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description vfs
Gnome VFS bindings for Python.

%description vfs -l pl
Wi您ania Pythona do biblioteki Gnome VFS.

%package zvt
Summary:	Gnome terminal widget bindings for Python
Summary(pl):	Wi您ania Pythona do biblioteki terminala Gnome
Group:		Libraries/Python
Requires:	python-pygtk-gtk

%description zvt
Gnome terminal bindings for Python.

%description zvt -l pl
Wi您ania Pythona do biblioteki terminala Gnome.

%package devel
Summary:	Development files for Gnome bindings for Python
Summary(pl):	Pliki programistyczne wi您a� Pythona do Gnome
Group:		Libraries/Python
Requires:	python-pygtk-devel >= 1.99.13
Requires:	%{name}-bonobo = %{version}
Requires:	%{name}-bonobo-ui = %{version}
Requires:	%{name}-applet = %{version}
Requires:	%{name}-canvas = %{version}
Requires:	%{name}-gconf = %{version}
Requires:	%{name}-gtkhtml = %{version}
Requires:	%{name}-nautilus = %{version}
Requires:	%{name}-ui = %{version}
Requires:	%{name}-vfs = %{version}
Requires:	%{name}-zvt = %{version}

%description devel
Development files for Gnome bindings for Python.

%description devel -l pl
Pliki programistyczne wi您a� Pythona do Gnome.

%prep
%setup -q -n %{module}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%dir %{py_sitedir}/gtk-2.0/gnome
%{py_sitedir}/gtk-2.0/gnome/__init__.py?
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/_gnome*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/_gnome*.la

%files bonobo
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/bonobo
%{py_sitedir}/gtk-2.0/bonobo/__init__.py?
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/_bonobo*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/_bonobo*.la
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/activation*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/activation*.la

%files bonobo-ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/ui*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/ui*.la

%files applet
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/applet*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/applet*.la

%files canvas
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/canvas*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/canvas*.la

%files gconf
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gconf*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gconf*.la

%files gtkhtml
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkhtml*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkhtml*.la

%files nautilus
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/nautilus*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/nautilus*.la

%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/ui*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/ui*.la

%files vfs
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/vfs*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/vfs*.la

%files zvt
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/zvt*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/zvt*.la

%files devel
%defattr(644,root,root,755)
%{pydefsdir}/*
%{_datadir}/pygtk/2.0/defs/*
%{_pkgconfigdir}/*
