
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
BuildRequires:	rpm-pythonprov
BuildRequires:	python-pygtk-devel >= 1.99.11
BuildRequires:	python-orbit-devel >= 1.99.0
%pyrequires_eq	python-modules
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
N/A

%description -l pl
N/A

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
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
