#!/usr/bin/env python

#Run this with your team number and then Putty into the Palo Alto. Enter "set cli scripting-mode on" and then "cofigure"
#Then copy and past the output of the script. The first command increases the winow buffer size and the second command enters configure mode.

import sys


if len(sys.argv) != 2:
    print "Usage: fw_conf.py <team #>"
    sys.exit(0)

team_num = sys.argv[1]

with open("""PAConfig"""+team_num+""".txt""", "w") as command_file:
	commands="""set deviceconfig system permitted-ip 172.20.241.0/24
set deviceconfig system service disable-telnet yes
set deviceconfig system login-banner AuthorizedAccessOnlythorizedAccessOnly
set network profiles zone-protection-profile Default discard-overlapping-tcp-segment-mismatch yes discard-unknown-option yes tcp-reject-non-syn yes flood tcp-syn enable yes syn-cookies maximal-rate 500
set network profiles zone-protection-profile Default flood icmp enable yes
set network profiles zone-protection-profile Default flood udp enable yes
set network profiles zone-protection-profile Default flood other-ip enable yes
set network profiles zone-protection-profile Default flood icmpv6 enable yes
set network profiles interface-management-profile none
set network interface ethernet ethernet1/3 layer3 interface-management-profile none
set network interface ethernet ethernet1/2 layer3 interface-management-profile none
delete rulebase security rules Any-Any
delete rulebase security rules LAN2DMZ
delete rulebase security rules DMZ2LAN
delete rulebase security rules any2any
set address Private1 ip-range 10.0.0.0-10.255.255.255
set address Private2 ip-range 172.16.0.0-172.16.255.255
set address Private3 ip-range 192.168.0.0-192.168.255.255
set rulebase security rules GoogleDNS action allow from any to any source any destination 8.8.8.8
set rulebase security rules GoogleDNS application dns service application-default
set rulebase security rules DNSoutBlock action allow from User to External source any destination any profile-setting profiles spyware strict virus default vulnerability strict
	
set rulebase security rules DNSoutBlock action allow from Public to External source any destination any

set rulebase security rules DNSoutBlock application DNS service application-default
set rulebase security rules NTPandSYSLOGandDNS action allow from User to Public source any destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules NTPandSYSLOGandDNS action allow from Internal to Public source any destination any profile-setting profiles spyware strict virus default vulnerability strict

set rulebase security rules NTPandSYSLOGandDNS action allow from Public to User source any destination

set rulebase security rules NTPandSYSLOGandDNS application ntp service application-default
set rulebase security rules NTPandSYSLOGandDNS application syslog service application-default
set rulebase security rules NTPandSYSLOGandDNS application dns service application-default
set rulebase security rules NTPandSYSLOGandDNS application ssl service application-default
set rulebase security rules NTPandSYSLOGandDNS application web-browsing service application-default
set rulebase security rules CentOStoUbuntuDB action allow from any to any source 172.20.241.30 destination 172.25.209.23 profile-setting profiles spyware strict virus default vulnerability strict

set rulebase security rules CentOStoUbuntuDB from any source 172.25.209.23

set rulebase security rules CentOStoUbuntuDB application any service any
set rulebase security rules PrivateIPOutNoNo action deny from User to External source any destination Private1
set rulebase security rules PrivateIPOutNoNo action deny from Internal to External source any destination Private1

set rulebase security rules PrivateIPOutNoNo action deny from User to External source any destination Private2
set rulebase security rules PrivateIPOutNoNo action deny from Internal to External source any destination Private2

set rulebase security rules PrivateIPOutNoNo action deny from Public to External source any destination Private3
set rulebase security rules PrivateIPOutNoNo action deny from Public to External source any destination Private3

set rulebase security rules PrivateIPOutNoNo application any service any
set rulebase security rules PaloAltoOut action allow from Internal to External source 172.20.240.254 destination any
set rulebase security rules PaloAltoOut action allow from User to External source 172.20.242.254 destination any

set rulebase security rules PaloAltoOut action allow from User to Public source 172.20.242.254 destination any
set rulebase security rules PaloAltoOut action allow from Internal to Public source 172.20.240.254 destination any

set rulebase security rules PaloAltoOut application paloalto-updates service any
set rulebase security rules PaloAltoOut application dns service any
set rulebase security rules PaloAltoOut application ntp service any

set rulebase security rules Win7External application any service any
set rulebase security rules CentOSin action allow from External to Public source any destination 172.25.209.11 profile-setting profiles spyware strict virus default vulnerability strict

set rulebase security rules CentOSin application ssl service application-default
set rulebase security rules CentOSin application web-browsing service application-default
set rulebase security rules 2008DNStoUbuntuDNS action allow from User to User source 172.20.242.200 destination 172.20.242.10 profile-setting profiles spyware strict virus default vulnerability strict

set rulebase security rules 2008DNStoUbuntuDNS application dns service application-default
set rulebase security rules DEBIANtoUBUNTU action allow from Internal to User source 172.20.240.20 destination 172.20.242.10 profile-setting profiles spyware strict virus default vulnerability strict

set rulebase security rules DEBIANtoUBUNTU application mysql service application-default
set rulebase security rules DEBIANtoUBUNTU from User source 172.20.242.10 to External destination 172.25.20.23
set rulebase security rules DEBIANtoUBUNTU from Internal source 172.20.240.20 to External destination 172.25.20.20

set rulebase security rules UbuntuDNSto2008DNS action allow from User to User source 172.20.242.10 destination 172.20.242.200 profile-setting profiles spyware strict virus default vulnerability strict

set rulebase security rules UbuntuDNSto2008DNS application dns service application-default
set rulebase security rules UbuntuDNSto2008DNS application ntp service application-default
set rulebase security rules UbuntuDNSto2008DNS application active-directory service application-default
set rulebase security rules UbuntuDNSto2008DNS application ldap service application-default
set rulebase security rules UbuntuDNSto2008DNS application ms-ds-smb service application-default
set rulebase security rules UbuntuDNSto2008DNS application msrpc service application-default
set rulebase security rules UbuntuDNSto2008DNS application ms-ds-smb service application-default
set rulebase security rules UbuntuDNSto2008DNS application netbios-ss service application-default
set rulebase security rules UbuntuDNSto2008DNS application netbios-dg service application-default
set rulebase security rules CentOSDNSto2008DNS action allow from Public to User source 172.20.241.30 destination 172.20.242.200 profile-setting profiles spyware strict virus default vulnerability strict

set rulebase security rules CentOSDNSto2008DNS application dns service application-default
set rulebase security rules CentOSDNSto2008DNS application ntp service application-default
set rulebase security rules CentOSDNSto2008DNS application active-directory service application-default
set rulebase security rules CentOSDNSto2008DNS application ldap service application-default
set rulebase security rules CentOSDNSto2008DNS application ms-ds-smb service application-default
set rulebase security rules CentOSDNSto2008DNS application msrpc service application-default
set rulebase security rules CentOSDNSto2008DNS application netbios-ss service application-default
set rulebase security rules CentOSDNSto2008DNS application netbios-dg service application-default
set rulebase security rules UbuntuDNSin action allow from External to User source any destination 172.25.209.23 profile-setting profiles spyware strict virus default vulnerability strict
 
set rulebase security rules UbuntuDNSin application dns service application-default
set rulebase security rules FEDORAin action allow from External to Public source any destination 172.25.209.39 profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules FEDORAin application web-browsing service application-default
set rulebase security rules FEDORAin application smtp service application-default
set rulebase security rules FEDORAin application pop3 service application-default
set rulebase security rules FEDORAin application ssl service application-default
set rulebase security rules FEDORAin application imap service application-default
set rulebase security rules 2008DNSin action allow from External to User source any destination 172.25.209.27 profile-setting profiles spyware strict virus default vulnerability strict
	
set rulebase security rules 2008DNSin application dns service application-default
set rulebase security rules Publicout-CentOS action allow from Public to External source 172.20.241.30 destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules Publicout-CentOS application ssl service application-default
set rulebase security rules Publicout-CentOS application ftp service application-default
set rulebase security rules Publicout-CentOS application yum service application-default
set rulebase security rules Publicout-CentOS application github service application-default
set rulebase security rules Publicout-CentOS application git-base service application-default
set rulebase security rules Publicout-CentOS application ssh service application-default
set rulebase security rules Publicout-CentOS application web-browsing service application-default
set rulebase security rules Userout-Ubuntu action allow from User to External source 172.20.242.10 destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules Userout-Ubuntu application dns service application-default
set rulebase security rules Userout-Ubuntu application web-browsing service application-default
set rulebase security rules Userout-Ubuntu application ssl service application-default
set rulebase security rules Userout-Ubuntu application apt-get service application-default
set rulebase security rules SERVERout-FEDORAout action allow from Public to External source 172.20.241.40 destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules SERVERout-FEDORAout application web-browsing service application-default
set rulebase security rules SERVERout-2012WAout application ssl service application-default
set rulebase security rules SERVERout-2012WAout application git-base service application-default
set rulebase security rules SERVERout-2012WAout application ms-update service application-default
set rulebase security rules SERVERout-2012WAout application github service application-default
set rulebase security rules SERVERout-2008AD action allow from User to External source 172.20.242.200 destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules SERVERout-2008AD application ssl service application-default
set rulebase security rules SERVERout-2008AD application ms-update service application-default
set rulebase security rules SERVERout-2008AD application dns service application-default
set rulebase security rules SERVERout-2008AD application web-browsing service application-default
set rulebase security rules SERVERout-Debian action allow from Internal to External source 172.20.240.20 destination any profile-setting profiles spyware strict virus default vulnerability strict
set rulebase security rules SERVERout-Debian application pop3 service application-default
set rulebase security rules SERVERout-Debian application imap service application-default
set rulebase security rules SERVERout-Debian application dns service application-default
set rulebase security rules SERVERout-Debian application ocsp service application-default
set rulebase security rules SERVERout-Debian application smtp service application-default
set rulebase security rules SERVERout-Debian application ssh service application-default
set rulebase security rules SERVERout-Debian application github service application-default
set rulebase security rules SERVERout-Debian application git-base service application-default
set rulebase security rules SERVERout-Debian application ssl service application-default
set rulebase security rules SERVERout-Debian application subversion service application-default
set rulebase security rules SERVERout-Debian application sourceforge service application-default
set rulebase security rules SERVERout-Debian application apt-get service application-default
set rulebase security rules SERVERout-Debian application web-browsing service application-default
set rulebase security rules INTERZONELAN action allow from User to User source any destination any
set rulebase security rules INTERZONELAN application any service any
set rulebase security rules INTERZONEDMZ action allow from Public to Public source any destination any
set rulebase security rules INTERZONEDMZ application any service any
set rulebase security rules DENYALLExternal action deny from External to any source any destination any
set rulebase security rules DENYALLExternal application any service any
set rulebase security rules DENYALL action deny from any to any source any destination any
set rulebase security rules DENYALL application any service any
commit
	"""

	command_file.write(commands)
	