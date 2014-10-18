Summary:	Tool to manage user directories
Name:		xdg-user-dirs
Version:	0.15
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	f5aaf5686ad7d8809a664bfb4566a54d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-user-dirs is a tool to help manage "well known" user directories
like the desktop folder and the music folder. It also handles
localization (i.e. translation) of the filenames.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/xdg-user-dirs << EOF
#!/bin/sh

# setup XDG user directories
[ -x /usr/bin/xdg-user-dirs-update ] && /usr/bin/xdg-user-dirs-update

EOF

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/user-dirs.*
%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/xdg-user-dirs
%attr(755,root,root) %{_bindir}/xdg-user-dir
%attr(755,root,root) %{_bindir}/xdg-user-dirs-update
%{_mandir}/man1/xdg-user-dir.1*
%{_mandir}/man1/xdg-user-dirs-update.1*
%{_mandir}/man5/user-dirs.conf.5*
%{_mandir}/man5/user-dirs.defaults.5*
%{_mandir}/man5/user-dirs.dirs.5*

