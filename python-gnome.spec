
%include	/usr/lib/rpm/macros.python

%define		module	gnome-python

Summary:	Gnome bindings for Python
Summary(pl):	Wi±zania Pythona do bibliotek Gnome
Name:		python-gnome
Version:	1.99.16
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-python/1.99/%{module}-%{version}.tar.bz2
BuildRequires:	gnome-panel-devel >= 2.0.9
BuildRequires:	gnome-vfs2-devel >= 2.0.4
BuildRequires:	libgnomeprintui-devel >= 2.2.1.1
BuildRequires:	libgtkhtml-devel >= 2.0.2
BuildRequires:	nautilus-devel >= 2.0.7
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-pyorbit-devel >= 1.99.3
BuildRequires:	python-pygtk-devel >= 1.99.15
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
Wi±zania Pythona do bibliotek Gnome.

%package bonobo
Summary:	Bonobo bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki Bonobo
Group:		Libraries/Python
Requires:	python-pygtk-gobject

%description bonobo
Bonobo bindings for Python.

%description bonobo -l pl
Wi±zania Pythona do biblioteki Bonobo.

%package bonobo-ui
Summary:	Bonobo User Interface bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki interfejsu u¿ytkownika Bonobo
Group:		Libraries/Python
Requires:	%{name}-canvas = %{version}
Requires:	%{name}-bonobo = %{version}

%description bonobo-ui
Bonobo User Interface bindings for Python.

%description bonobo-ui -l pl
Wi±zania Pythona do biblioteki interfejsu u¿ytkownika Bonobo.

%package applet
Summary:	Gnome Applet bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki Gnome Applet
Group:		Libraries/Python
Requires:	python-pygtk-gtk
Requires:	%{name} = %{version}

%description applet
Gnome Applet bindings for Python.

%description applet -l pl
Wi±zania Pythona do biblioteki Gnome Applet.

%package canvas
Summary:	Gnome Canvas bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki Gnome Canvas
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description canvas
Gnome Canvas bindings for Python.

%description canvas -l pl
Wi±zania Pythona do biblioteki Gnome Canvas.

%package gconf
Summary:	GConf bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki GConf
Group:		Libraries/Python
Requires:	python-pygtk-gobject

%description gconf
GConf bindings for Python.

%description gconf -l pl
Wi±zania Pythona do biblioteki GConf.

%package gtkhtml
Summary:	GtkHtml bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki GtkHtml
Group:		Libraries/Python
Requires:	python-pygtk-gobject

%description gtkhtml
GtkHtml bindings for Python.

%description gtkhtml -l pl
Wi±zania Pythona do biblioteki GtkHtml.

%package nautilus
Summary:	Nautilus bindings for Python
Summary(pl):	Wi±zania Pythona do Nautilusa
Group:		Libraries/Python
Requires:	%{name}-bonobo-ui = %{version}

%description nautilus
Nautilus bindings for Python.

%description nautilus -l pl
Wi±zania Pythona do Nautilusa.

%package print
Summary:	Gnome Print bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki Gnome obs³ugi drukowania
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description print
Gnome Print bindings for Python.

%description print -l pl
Wi±zania Pythona do biblioteki Gnome obs³ugi drukowania.

%package print-ui
Summary:	Gnome Print User Interface bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki interfejsu u¿ytkownika Gnome obs³ugi drukowania
Group:		Libraries/Python
Requires:	%{name}-ui = %{version}

%description print-ui
Gnome Print User Interface bindings for Python.

%description print-ui -l pl
Wi±zania Pythona do biblioteki interfejsu u¿ytkownika Gnome obs³ugi
drukowania.

%package ui
Summary:	Gnome User Interface bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki interfejsu u¿ytkownika Gnome
Group:		Libraries/Python
Requires:	%{name}-bonobo-ui = %{version}

%description ui
Gnome User Interface bindings for Python.

%description ui -l pl
Wi±zania Pythona do biblioteki interfejsu u¿ytkownika Gnome.

%package vfs
Summary:	Gnome VFS bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki Gnome VFS
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description vfs
Gnome VFS bindings for Python.

%description vfs -l pl
Wi±zania Pythona do biblioteki Gnome VFS.

%package devel
Summary:	Development files for Gnome bindings for Python
Summary(pl):	Pliki programistyczne wi±zañ Pythona do Gnome
Group:		Libraries/Python
Requires:	python-pygtk-devel >= 1.99.13
Requires:	%{name}-bonobo = %{version}
Requires:	%{name}-bonobo-ui = %{version}
Requires:	%{name}-applet = %{version}
Requires:	%{name}-canvas = %{version}
Requires:	%{name}-gconf = %{version}
Requires:	%{name}-gtkhtml = %{version}
Requires:	%{name}-nautilus = %{version}
Requires:	%{name}-print = %{version}
Requires:	%{name}-print-ui = %{version}
Requires:	%{name}-ui = %{version}
Requires:	%{name}-vfs = %{version}

%description devel
Development files for Gnome bindings for Python.

%description devel -l pl
Pliki programistyczne wi±zañ Pythona do Gnome.

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
%{py_sitedir}/gtk-2.0/gnome/_gnome*.la

%files bonobo
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/bonobo
%{py_sitedir}/gtk-2.0/bonobo/__init__.py?
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/_bonobo*.so
%{py_sitedir}/gtk-2.0/bonobo/_bonobo*.la
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/activation*.so
%{py_sitedir}/gtk-2.0/bonobo/activation*.la

%files bonobo-ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/ui*.so
%{py_sitedir}/gtk-2.0/bonobo/ui*.la

%files applet
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/applet*.so
%{py_sitedir}/gtk-2.0/gnome/applet*.la

%files canvas
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/canvas*.so
%{py_sitedir}/gtk-2.0/gnome/canvas*.la

%files gconf
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gconf*.so
%{py_sitedir}/gtk-2.0/gconf*.la

%files gtkhtml
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkhtml*.so
%{py_sitedir}/gtk-2.0/gtkhtml*.la

%files nautilus
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/nautilus*.so
%{py_sitedir}/gtk-2.0/gnome/nautilus*.la

%files print
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gnomeprint
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomeprint/_printmod*.so
%{py_sitedir}/gtk-2.0/gnomeprint/_printmod*.la
%{py_sitedir}/gtk-2.0/gnomeprint/*.py[co]

%files print-ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomeprint/uimodule.so
%{py_sitedir}/gtk-2.0/gnomeprint/uimodule.la

%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/ui*.so
%{py_sitedir}/gtk-2.0/gnome/ui*.la

%files vfs
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/vfs*.so
%{py_sitedir}/gtk-2.0/gnome/vfs*.la

%files devel
%defattr(644,root,root,755)
%{pydefsdir}/*
%{_pkgconfigdir}/*
