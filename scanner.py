import socket
import argparse

def scan_port(target, port):
	try:
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		target_ip=socket.gethostbyname(target)
		print(f"Starting scan on {target_ip}")
		result= s.connect_ex((target_ip, port))

		if result == 0:
			print (f'Port {port} is open')
			
		else:
			print(f'Port {port} is closed')
		s.close()	
		
	except socket.timeout:
		print(f"Port {port} is closed (timeout)")

	except socket.error as e:
		print(f"Error connecting to {target_ip}: {e}")
	finally:
		s.close()

def port_scanner(target, start_port, end_port):
	try:
		target_ip=socket.gethostbyname(target)

	except socket.gaierror:
		print('Unable to resolve target')
		return

	print(f"Starting scan on {target_ip}")

	for port in range(start_port, end_port +1):
		scan_port(target_ip, port)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='port scanner')
	parser.add_argument('target', type=str, help='Enter IP or Domain')
	parser.add_argument('-v', '--verbose', action='store_true', help='Verbosity')
	parser.add_argument("-p", "--port", type=int, help="Port number to scan")
	parser.add_argument("-r", "--range", nargs=2, type=int, metavar=('start_port', 'end_port'), help="Range of ports to scan (start and end ports)")
	args=parser.parse_args()

	if args.port:
		scan_port(args.target, args.port)

	elif args.range:
		port_scanner(args.target, args.range[0], args.range[1])
	else:
		print("Please provide either a port (-p) or a range (-r)")
