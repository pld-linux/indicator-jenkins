# TODO
# - desktop file
# - xdg-autostart file?
%define		bzrrev	49
%define		rel		1
Summary:	Jenkins job status indicator
Name:		indicator-jenkins
Version:	1.0
Release:	0.bzr%{bzrrev}.%{rel}
License:	GPL v3
Group:		Applications
# bzr branch lp:indicator-jenkins
# tar czf indicator-jenkins-1.0-bzr49.tar.gz --exclude-vcs indicator-jenkins
Source0:	%{name}-%{version}-bzr%{bzrrev}.tar.gz
# Source0-md5:	3bbc617e1b64db92add8a871c6d591fe
URL:		http://tech-foo.blogspot.co.nz/2012/02/introducing-indicator-jenkins.html
Requires:	libappindicator-gtk3
Requires:	python-jenkins
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
An indicator that allows you to keep an eye on jenkins jobs.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}
cp -a indicator-jenkins images *.py *.ui $RPM_BUILD_ROOT%{_appdir}
ln -s %{_appdir}/indicator-jenkins $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc VERSION COPYING
%attr(755,root,root) %{_bindir}/indicator-jenkins
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/indicator-jenkins
%{_appdir}/*.py
%{_appdir}/settings.ui
%{_appdir}/images
