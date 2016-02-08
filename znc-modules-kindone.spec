%global _version 0

# let's try avoiding this name
%global _name znc-modules

%global hash c5a2093bc1572529cf5622e4c5a7db52429c1deb
%global shorthash %(bash -c 'c=%{hash}; echo ${c:0:7}')
%global zver %(rpm -q --queryformat='%{version}-%{release}' znc-devel)

Name: znc-modules-kindone
Version: %{_version}.b_%{shorthash}
Release: 1
Summary: Miscellanous ZNC modules
Requires: znc = %{zver}

BuildRequires: znc-devel libicu-devel

License: Freely redistributable without restriction
URL: https://github.com/KindOne-/znc-modules
Source0: https://github.com/KindOne-/%{_name}/archive/${hash}.tar.gz#/%{_name}-%{shorthash}.tar.gz

%description
This is just a collection of crude znc modules I (KindOne-) have created.
Run at own risk as they might crash your znc.
not responsible for crashing your znc with these modules.
tl;dr, experimenting/learning how to write modules. 

%package -n znc-autojoin
Summary: EXTREMELY CRUDE ZNC module to join channels on invite.
%description -n znc-autojoin
EXTREMELY CRUDE ZNC module to join channels on invite.

%package -n znc-block_botserv
Summary: ZNC module to block irc client from sending commands to BotServ
%description -n znc-block_botserv
ZNC module to block irc client from sending commands to BotServ

%package -n znc-block_chanserv
Summary: ZNC module to block irc client from sending commands to ChanServ
%description -n znc-block_chanserv
ZNC module to block irc client from sending commands to ChanServ

%package -n znc-block_hostserv
Summary: ZNC module to block irc client from sending commands to HostServ
%description -n znc-block_hostserv
ZNC module to block irc client from sending commands to HostServ

%package -n znc-block_join
Summary: ZNC module to block irc client from sending /join
%description -n znc-block_join
ZNC module to block irc client from sending /join

%package -n znc-block_join_0
Summary: ZNC module to block irc client from sending /join 0
%description -n znc-block_join_0
ZNC module to block irc client from sending /join 0

%package -n znc-block_memoserv
Summary: ZNC module to block irc client from sending commands to MemoServ
%description -n znc-block_memoserv
ZNC module to block irc client from sending commands to MemoServ

%package -n znc-block_nickserv
Summary: ZNC module to block irc client from sending commands to NickServ
%description -n znc-block_nickserv
ZNC module to block irc client from sending commands to NickServ

%package -n znc-block_notice
Summary: ZNC module to block irc client from sending /notice commands
%description -n znc-block_notice
ZNC module to block irc client from sending /notice commands

%package -n znc-block_operserv
Summary: ZNC module to block irc client from sending commands to OperServ
%description -n znc-block_operserv
ZNC module to block irc client from sending commands to OperServ

%package -n znc-block_services
Summary: ZNC module to block irc client from sending commands to service bots
%description -n znc-block_services
ZNC module to block irc client from sending commands to
{Bot,Chan,Host,Memo,Nick,Oper}Serv

%package -n znc-block_who
Summary: ZNC module to block irc client from sending /who #channel
%description -n znc-block_who
ZNC module to block irc client from sending /who #channel

%package -n znc-channelurl
Summary: ZNC module to block irc client from receiving channel URL notices
%description -n znc-channelurl
ZNC module to block irc client from receiving channel URL notices

%package -n znc-excessflood
Summary: ZNC module to detect excess floods
%description -n znc-excessflood
ZNC module to detect excess floods

%package -n znc-freenodeinfo
Summary: ZNC module to block irc client from receiving [freenode-info] spam
%description -n znc-freenodeinfo
ZNC module to block irc client from receiving [freenode-info] spam

%package -n znc-glined
Summary: ZNC module to detect /glines
%description -n znc-glined
ZNC module to detect /glines

%package -n znc-monitor
Summary: EXTREMELY CRUDE ZNC module to support MONITOR.
%description -n znc-monitor
EXTREMELY CRUDE ZNC module to support MONITOR.

%package -n znc-klined
Summary: ZNC module to detect /klines
%description -n znc-klined
ZNC module to detect /klines

%package -n znc-notice
Summary: ZNC module to convert NOTICE into PRIVMSG for a client
%description -n znc-notice
ZNC module to convert NOTICE into PRIVMSG for a client

%package -n znc-sendq
Summary: ZNC module to detect sendq quit messages
%description -n znc-sendq
ZNC module to detect sendq quit messages

%package -n znc-sigyn
Summary: ZNC module to detect sigyn activity
%description -n znc-sigyn
ZNC module to detect when sigyn issues a /kill in any channels we are with.

%package -n znc-zlined
Summary: ZNC module to detect /zlines
%description -n znc-zlined
ZNC module to detect /zlines

%prep
%setup -qn %{_name}-%{hash}

%build
for x in modules/*.cpp ; do
  znc-buildmod $x
done

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/znc
for x in *.so ; do
  cp $x $RPM_BUILD_ROOT%{_libdir}/znc
done

%files
%defattr(-,root,root,-)

%files -n znc-autojoin
%{_libdir}/znc/autojoin.so

%files -n znc-block_botserv
%{_libdir}/znc/block_botserv.so

%files -n znc-block_chanserv
%{_libdir}/znc/block_chanserv.so

%files -n znc-block_hostserv
%{_libdir}/znc/block_hostserv.so

%files -n znc-block_join
%{_libdir}/znc/block_join.so

%files -n znc-block_join_0
%{_libdir}/znc/block_join_0.so

%files -n znc-block_memoserv
%{_libdir}/znc/block_memoserv.so

%files -n znc-block_nickserv
%{_libdir}/znc/block_nickserv.so

%files -n znc-block_notice
%{_libdir}/znc/block_notice.so

%files -n znc-block_operserv
%{_libdir}/znc/block_operserv.so

%files -n znc-block_services
%{_libdir}/znc/block_services.so

%files -n znc-block_who
%{_libdir}/znc/block_who.so

%files -n znc-channelurl
%{_libdir}/znc/channelurl.so

%files -n znc-excessflood
%{_libdir}/znc/excessflood.so

%files -n znc-freenodeinfo
%{_libdir}/znc/freenodeinfo.so

%files -n znc-glined
%{_libdir}/znc/glined.so

%files -n znc-klined
%{_libdir}/znc/klined.so

%files -n znc-monitor
%{_libdir}/znc/monitor.so

%files -n znc-notice
%{_libdir}/znc/notice.so

%files -n znc-sendq
%{_libdir}/znc/sendq.so

%files -n znc-sigyn
%{_libdir}/znc/sigyn.so

%files -n znc-zlined
%{_libdir}/znc/zlined.so

%changelog
* Sun Feb  7 2016 RJ Bergeron <rbergero@gmail.com>
- initial packaging.
