import scapy.all as scapy
import argparse

def network_sniffer(interface):
    try:
        scapy.sniff(iface=interface, store=False, prn=lambda x: x.show())

    except Exception as e:
        print('An error occurred: %s' % e)

def main():
    parser = argparse.ArgumentParser(description='Network Sniffer')
    parser.add_argument('interface', help='Network interface to sniff')
    args = parser.parse_args()

    network_sniffer(args.interface)

if __name__ == '__main__':
    main()
