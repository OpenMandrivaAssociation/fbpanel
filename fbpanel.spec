%define name	fbpanel
%define version	4.12
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Lightweight desktop panel
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://fbpanel.sourceforge.net/
License:	GPL
Group:		Graphical desktop/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk2-devel xpm-devel libxmu-devel

%description
fbpanel is a lightweight, NETWM compliant desktop panel. It works with any
NETWM compliant window manager (eg xfwm4, sawfish, openbox, metacity, kde).

It provides:
    * variety of plugins
    * ability to replace window icons
    * all icons follow your current GTK+ icon theme
    * transparency support
    * customizable size and screen position
    * ability to run many instances each with its own configuration
    * modest resource usage

%prep
%setup -q

%build
./configure --prefix=%_prefix
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%buildroot/%_prefix

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGELOG CREDITS README
%{_bindir}/%name
%{_datadir}/%name
%{_mandir}/man1/*
