%global _version 0

%global hash 989bb187106be43e8e9946e82bcd9f2177d13ae5
%global shorthash %(bash -c 'c=%{hash}; echo ${c:0:7}')
%global zver %(rpm -q --queryformat='%{version}-%{release}' znc-devel)
%global _name colloquypush

Name: znc-colloquypush
Version: %{_version}.b_%{shorthash}
Release: 1
Summary: Colloquy mobile push notifications for ZNC
Requires: znc = %{zver}

BuildRequires: znc-devel libicu-devel

License: GPLv2
URL: https://github.com/wired/colloquypush
Source0: https://github.com/wired/%{_name}/archive/${hash}.tar.gz#/%{name}-%{shorthash}.tar.gz
# https://github.com/wired/colloquypush/commit/683d4360d112fad1a741136049e105fad86a5e32
Patch0: znc-colloquypush.patch

%description
A znc module that pushes priv messages and hilights to Colloquy Mobile.

%prep
%setup -qn %{_name}-%{hash}
%patch0 -p1

%build
znc-buildmod znc/colloquy.cpp

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/znc
cp colloquy.so $RPM_BUILD_ROOT%{_libdir}/znc

%files
%defattr(-,root,root,-)
%{_libdir}/znc/colloquy.so

%changelog
* Sun Feb  7 2016 RJ Bergeron <rbergero@gmail.com>
- initial packaging. includes patch for znc 1.6.
