Summary:	A graphical regular expression explorer
#Summary(pl):	-
Name:		gregexp
Version:	0.2.1
Release:	0.1
License:	GPL	
Group:		Development/Tools
Source0:	http://dentrassi.de/download/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ed3a9d13c050379d9062110b614dd1c3
URL:		http://dentrassi.de/download/gregexp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A graphical regular expression explorer that usees PCRE as regular
expression engine. 

#%description -l pl

%prep
%setup -q

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
