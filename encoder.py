import argparse
import base64
import hashlib
from termcolor import colored

def base64_encode(data):
	res=base64.b64encode(data.encode())
	print(res.decode())

def base64_decode(data):
	res=base64.b64decode(data.encode())
	print(res.decode())

def md5_encode(data):
	res=hashlib.md5(data.encode())
	print(res.hexdigest())

def sha256_encode(data):
	res=hashlib.sha256(data.encode())
	print(res.hexdigest())

if __name__ == '__main__':
	parser=argparse.ArgumentParser(description='Encoder by Johnson')
	parser.add_argument('data', type=str, help='String to encode or decode')
	parser.add_argument('--decode', action='store_true', help='String to decode(only for base64)')
	parser.add_argument('-e', '--encode', type=str, choices=['base64', 'md5', 'sha256'], help='encoding to perform')
	args=parser.parse_args()

	if args.decode:
		print(colored('Decoder by Johnson', 'green'))
		print(colored("Starting decoding....................", 'green'))
		base64_decode(args.data)

	elif args.encode:
		print(colored('Decoder by Johnson', 'green'))
		print(colored(f"Starting encoding using {args.encode}.........................", 'green'))
		if args.encode == 'base64':
			base64_encode(args.data)
		elif args.encode == 'md5':
			md5_encode(args.data)
		elif args.encode == 'sha256':
			sha256_encode(args.data)

	else:
		print("No encoding or decoding specified.")
