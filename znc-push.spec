%global _version 2.0.0rc

%global hash 717a2b1741eee75456b0862ef76dbb5af906e936
%global shorthash %(bash -c 'c=%{hash}; echo ${c:0:7}')
%global zver %(rpm -q --queryformat='%{version}-%{release}' znc-devel)

Name: znc-push
Version: %{_version}.b_%{shorthash}
Release: 1
Summary: generic push notifications for ZNC
Requires: znc = %{zver}

BuildRequires: znc-devel libicu-devel

License: MIT
URL: http://noswap.com/projects/znc-push
Source0: https://github.com/jreese/%{name}/archive/${hash}.tar.gz#/%{name}-%{shorthash}.tar.gz

%description
Based around the core conditions and functionality from my original
project, ZNC Push is a module for ZNC that will send push notifications
to multiple services for any private message or channel highlight
that matches a configurable set of conditions, including
the user’s /away status, time since the last notification,
number of clients connected to ZNC, and more.

Currently supported push services include Boxcar, NMA, Notifo, Pushover,
Prowl, and Supertoasty.

%prep
%setup -qn %{name}-%{hash}

%build
znc-buildmod push.cpp

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/znc
cp push.so $RPM_BUILD_ROOT%{_libdir}/znc

%files
%defattr(-,root,root,-)
%{_libdir}/znc/push.so

%changelog
* Sun Feb  7 2016 RJ Bergeron <rbergero@gmail.com>
- initial packaging.
