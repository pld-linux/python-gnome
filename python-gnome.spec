
#
# todo:
# - more build requirements
# - more subpackages: gconf, bonobo, nautilus, etc.
#

%include	/usr/lib/rpm/macros.python

%define		module	gnome-python

Summary:	Gnome bindings for Python
Summary(pl):	Wi±zania Pythona do bibliotek Gnome
Name:		python-gnome
Version:	1.99.13
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	ftp://ftp.gnome.org/pub/GNOME/2.0.2/sources/%{module}/%{module}-%{version}.tar.gz
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-orbit-devel >= 1.99.0
BuildRequires:	python-pygtk-devel >= 1.99.13
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome bindings for Python.

%description -l pl
Wi±zania Pythona do bibliotek Gnome.

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

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%attr(755,root,root) %{py_sitedir}/gtk-2.0/*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/*.la

%dir %{py_sitedir}/gtk-2.0/bonobo
%{py_sitedir}/gtk-2.0/bonobo/__init__.py?
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/bonobo/*.la

%dir %{py_sitedir}/gtk-2.0/gnome
%{py_sitedir}/gtk-2.0/gnome/__init__.py?
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnome/*.la

#%files devel
%defattr(644,root,root,755)
%{_datadir}/pygtk/2.0/defs/*
%{_pkgconfigdir}/*
