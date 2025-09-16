import dns.resolver
import argparse

def dns_enumerator(domain):
    try:
        # Create a DNS resolver object
        resolver = dns.resolver.Resolver()

        # Set the DNS server to use
        resolver.nameservers = ['8.8.8.8']

        # Perform a DNS query for the domain
        answers = resolver.resolve(domain, 'A')

        # Print the DNS records
        for answer in answers:
            print(answer.to_text())

    except Exception as e:
        print('An error occurred: %s' % e)

def main():
    parser = argparse.ArgumentParser(description='DNS Enumerator')
    parser.add_argument('domain', help='Domain to enumerate')
    args = parser.parse_args()

    dns_enumerator(args.domain)

if __name__ == '__main__':
    main()
