%define _disable_ld_no_undefined 1
%define _libexecdir /usr/libexec

Summary:	A lightweight X11 desktop panel
Name:		fbpanel
Version:	6.1
Release:	4
License:	LGPLv2+ and GPLv2+
Group:		Graphical desktop/Other
Url:		http://fbpanel.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tbz2
Patch0:		fbpanel-6.1-dsofix.patch
# distro specific patches
Patch10:	fbpanel-6.1-default-config.patch
Patch11:	fbpanel-6.1-default-applications.patch
BuildRequires:	pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)
Requires:	xdg-utils

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
%patch0 -p1 -b .dsofix
%patch10 -p1 -b .default-config
%patch11 -p1 -b .default-applications

%build
%setup_compile_flags
# this script is really ugly and doesn't work with configure macro
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=%{_localstatedir}
%make cflagsx="%{optflags}"

%install
%makeinstall_std

# man page
install -Dpm 644 data/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# change some icon names that were also changed in the default panel config
mv %{buildroot}%{_datadir}/%{name}/images/logo.png \
	%{buildroot}%{_datadir}/%{name}/images/start-here.png

mv %{buildroot}%{_datadir}/%{name}/images/gnome-session-halt.png \
	%{buildroot}%{_datadir}/%{name}/images/system-shutdown.png

mv %{buildroot}%{_datadir}/%{name}/images/gnome-session-reboot.png \
	%{buildroot}%{_datadir}/%{name}/images/system-reboot.png

# volume plugin is not working and prevents starting of fbpanel, lets remove it.
# https://sourceforge.net/tracker/?func=detail&aid=3121295&group_id=66031&atid=513125
rm %{buildroot}%{_libdir}/%{name}/volume.so

%files
%doc CHANGELOG COPYING CREDITS README NOTES
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1.*
%{_libexecdir}/fbpanel/



