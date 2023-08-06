import subprocess
import os

def main():
    user_name = "unknown"
    dns_port = "9061"
    transfer_port = "9051"
    network = "10.66.0.0/255.255.0.0"

    # Stop Tor
    subprocess.call("sudo pkill tor", shell=True)

    # Start Tor
    subprocess.call("tor -f " + os.path.join(os.getcwd(), "torrc"), shell=True)

    # Set up iptables rules
    for table in ["nat", "filter"]:
        target = "ACCEPT"
        if table == "nat":
            target = "RETURN"

        subprocess.call("iptables -t " + table + " -F OUTPUT", shell=True)
        subprocess.call("iptables -t " + table + " -A OUTPUT -m state --state ESTABLISHED -j " + target, shell=True)
        subprocess.call("iptables -t " + table + " -A OUTPUT -m owner --uid " + "105" + " -j " + target, shell=True)

        match_dns_port = dns_port
        if table == "nat":
            target = "REDIRECT --to-ports {}".format(dns_port)
            match_dns_port = "53"

        subprocess.call("iptables -t " + table + " -A OUTPUT -p udp --dport " + match_dns_port + " -j " + target, shell=True)
        subprocess.call("iptables -t " + table + " -A OUTPUT -p tcp --dport " + match_dns_port + " -j " + target, shell=True)

        if table == "nat":
            target = "REDIRECT --to-ports {}".format(transfer_port)

        subprocess.call("iptables -t " + table + " -A OUTPUT -d " + network + " -p tcp -j " + target, shell=True)


        if table == "nat":
            target = "RETURN"

        subprocess.call("iptables -t " + table + " -A OUTPUT -d 127.0.0.1/8    -j " + target, shell=True)
        subprocess.call("iptables -t " + table + " -A OUTPUT -d 192.168.0.0/16 -j " + target, shell=True)
        subprocess.call("iptables -t " + table + " -A OUTPUT -d 172.16.0.0/12  -j " + target, shell=True)
        subprocess.call("iptables -t " + table + " -A OUTPUT -d 10.0.0.0/8     -j " + target, shell=True)

        if table == "nat":
            target = "REDIRECT --to-ports {}".format(transfer_port)

        subprocess.call("iptables -t " + table + " -A OUTPUT -p tcp -j " + target, shell=True)


    subprocess.call("iptables -t filter -A OUTPUT -p udp -j REJECT", shell=True)
    subprocess.call("iptables -t filter -A OUTPUT -p icmp -j REJECT", shell=True)

    # Disable IPv6
    subprocess.call("sysctl -w net.ipv6.conf.all.disable_ipv6=1", shell=True)
    subprocess.call("sysctl -w net.ipv6.conf.default.disable_ipv6=1", shell=True)

if __name__ == "__main__":
    main()
