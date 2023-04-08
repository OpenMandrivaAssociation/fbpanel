%define _disable_ld_no_undefined 1

Summary:	A lightweight X11 desktop panel
Name:		fbpanel
Version:	7.0
Release:	1
License:	LGPLv2+ and GPLv2+
Group:		Graphical desktop/Other
Url:		https://github.com/aanatoly/fbpanel
Source0:	https://github.com/aanatoly/fbpanel/archive/%{version}/%{name}-%{version}.tar.gz
# (fedora)
Patch0:		fbpanel-7.0-script-py3.patch
Patch1:		fbpanel-7.0-script-py310.patch
Patch2:		fbpanel-7.0-clang.patch
# distro specific patches
Patch10:	fbpanel-7.0-default-config.patch
Patch11:	fbpanel-7.0-default-applications.patch

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

%files
%license COPYING
%doc CHANGELOG CREDITS README.md NOTES
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_libexecdir}/%{name}/
%{_mandir}/man1/%{name}.1*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%before_configure
# this script is really ugly and doesn't work with configure macro
./configure \
	--prefix=%{_prefix} \
    --libdir=%{_libdir}/%{name} \
    --libexecdir=%{_libexecdir}/%{name} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=%{_localstatedir} \
    --datadir=%{_datadir}/%{name} \
    --mandir=%{_mandir}/man1
%make_build cflagsx="%{optflags}"

%install
%make_install

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
rm %{buildroot}%{_libdir}/%{name}/libvolume.so

