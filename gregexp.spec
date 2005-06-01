Summary:	A graphical regular expression explorer
Summary(pl):	Graficzny eksplorator wyra¿eñ regularnych
Name:		gregexp
Version:	0.3
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dentrassi.de/download/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	67310625715c4f13ec65e2ebb90a3654
URL:		http://dentrassi.de/download/gregexp/
Patch0:		%{name}-desktop.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libglade-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A graphical regular expression explorer that uses PCRE as regular
expression engine. 

%description -l pl
Graficzny eksplorator wyra¿eñ regularnych, który u¿ywa PCRE jako silnika
wyra¿eñ regularnych.

%prep
%setup -q
%patch0 -p1

%build
glib-gettextize --copy --force
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
