%include	/usr/lib/rpm/macros.python

%define		module	gnome-python

Summary:	Gnome bindings for Python
Summary(pl):	Wi±zania Pythona do bibliotek Gnome
Name:		python-gnome
Version:	1.99.11
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	ftp://ftp.gnome.org/pub/GNOME/pre-gnome2/sources/%{module}/%{module}-%{version}.tar.gz
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-orbit-devel >= 1.99.0
BuildRequires:	python-pygtk-devel >= 1.99.11
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
%attr(755,root,root) %{py_sitedir}/gconfmodule.*
%attr(755,root,root) %{py_sitedir}/gtkhtml2module.*
%dir %{py_sitedir}/gnome
%attr(755,root,root) %{py_sitedir}/gnome/_gnomemodule.*
%attr(755,root,root) %{py_sitedir}/gnome/appletmodule.*
%attr(755,root,root) %{py_sitedir}/gnome/canvasmodule.*
%attr(755,root,root) %{py_sitedir}/gnome/nautilusmodule.*
%attr(755,root,root) %{py_sitedir}/gnome/uimodule.*
%attr(755,root,root) %{py_sitedir}/gnome/vfsmodule.*
%attr(755,root,root) %{py_sitedir}/gnome/zvtmodule.*
%{py_sitedir}/gnome/__init__.py?
%dir %{py_sitedir}/bonobo
%attr(755,root,root) %{py_sitedir}/bonobo/_bonobomodule.*
%attr(755,root,root) %{py_sitedir}/bonobo/activationmodule.*
%attr(755,root,root) %{py_sitedir}/bonobo/uimodule.*
%{py_sitedir}/bonobo/__init__.py?

#file devel
%defattr(644,root,root,755)
%{_datadir}/pygtk/2.0/defs/*
%{_pkgconfigdir}/*
