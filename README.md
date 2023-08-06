## Tor default gateway

The Tor project allows users to surf the Internet, chat and send instant messages anonymously through its own mechanism. It is used by a wide variety of people, companies and organizations, both for lawful activities and for other illicit purposes. Tor has been largely used by intelligence agencies, hacking groups, criminal activities and even ordinary users who care about their privacy in the digital world.

Tor default gateway is an engine, developed in Python3, that aims on making the Tor network your default network gateway. Tor default gateway can route the traffic from your machine to the Internet through Tor network, so you can surf the Internet having a more formidable stance on privacy and anonymity in cyberspace.

Currently, it only works on Debian based systems and only IPv4 is supported by Tor default gateway, but we are working on a solution that adds IPv6 support. Also, only traffic other than DNS requests destined for local and/or loopback addresses is not trafficked through Tor. All non-local UDP/ICMP traffic is also blocked by the Tor project.



# Install required dependencies
```shell
sudo apt update && install iptables tor python3
```

# Using the tool
```shell
# Start Tor default gateway
sudo python3 start.py

# Stop Tor default gateway
sudo python3 stop.py
```
