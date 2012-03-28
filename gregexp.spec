Summary:	A graphical regular expression explorer
Summary(pl.UTF-8):	Graficzny eksplorator wyrażeń regularnych
Name:		gregexp
Version:	0.4
Release:	3
License:	GPL
Group:		Development/Tools
Source0:	http://dentrassi.de/download/gregexp/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ac1a6421b5cae83f6c541d2263f8d533
URL:		http://dentrassi.de/download/gregexp/
Patch0:		%{name}-desktop.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A graphical regular expression explorer that uses PCRE as regular
expression engine.

%description -l pl.UTF-8
Graficzny eksplorator wyrażeń regularnych, który używa PCRE jako
silnika wyrażeń regularnych.

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
