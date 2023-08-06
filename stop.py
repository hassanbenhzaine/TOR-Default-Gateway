import subprocess

def main():

    # Set up iptables rules
    for table in ["nat", "filter"]:
        subprocess.call("iptables -t " + table + " -F OUTPUT", shell=True)

    subprocess.call("pkill tor", shell=True)

if __name__ == "__main__":
    main()
