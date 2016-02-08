%global _version 1.6.0

%global hash cdfd1965e3056a5d85f110b93509d9cd94545154
%global shorthash %(bash -c 'c=%{hash}; echo ${c:0:7}')
%global zver %(rpm -q --queryformat='%{version}-%{release}' znc-devel)

Name: znc-chanfilter
Version: %{_version}.b_%{shorthash}
Release: 1
Summary: ZNC channel filter module for identified clients
Requires: znc = %{zver}

BuildRequires: znc-devel libicu-devel

License: ASL 2.0
URL: http://wiki.znc.in/Chanfilter
Source0: https://github.com/jpnurmi/%{name}/archive/${hash}.tar.gz#/%{name}-%{shorthash}.tar.gz

%description
The channel filter module maintains client specific channel lists for
identified clients. A typical use case is to have a subset of channels
visible for a mobile client.

%prep
%setup -qn %{name}-%{hash}

%build
znc-buildmod chanfilter.cpp

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/znc
cp chanfilter.so $RPM_BUILD_ROOT%{_libdir}/znc

%files
%defattr(-,root,root,-)
%{_libdir}/znc/chanfilter.so

%changelog
* Sun Feb  7 2016 RJ Bergeron <rbergero@gmail.com>
- initial packaging.
