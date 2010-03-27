%define name	fbpanel
%define version	6.0
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Lightweight desktop panel
Version: 	%{version}
Release: 	%{release}

Source:		http://downloads.sourceforge.net/project/fbpanel/fbpanel/%{version}/%{name}-%{version}.tbz2
URL:		http://fbpanel.sourceforge.net/
License:	GPL
Group:		Graphical desktop/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk2-devel

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
./configure --prefix=%{_prefix} --libdir=%{_libdir} --libexecdir=%{_libexecdir} \
	--sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir}
%define _disable_ld_no_undefined 1
%setup_compile_flags
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGELOG CREDITS README
%{_bindir}/%name
%{_datadir}/%name
%dir %{_libdir}/%name
%{_libdir}/%name/*.so
%{_libexecdir}/%name/make_profile
%{_libexecdir}/%name/xlogout
