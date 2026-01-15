import requests
import argparse
import sys

if __name__ == '__main__':

	argparser = argparse.ArgumentParser()
	argparser.add_argument("-u", "--url", type=str, help="URL to get HTTP response")
	args = argparser.parse_args()

	if not args.url:
		argparser.error("missing required URL arg")
		
		
	try:
		while True:
			print()

			try:
				response = requests.get(args.url, timeout=10, )
				response.raise_for_status()
				print(f"Status code: {response.status_code}")
			
			except requests.exceptions.HTTPError as http_error:
				print(f"HTTP error: {http_error}")
			except requests.exceptions.RequestException as err:
				print(f"An error has occurred: {err}")

			print("----------------------------------------")
			print()

	except KeyboardInterrupt:
		print()
		print("Exiting")
		sys.exit(0)
	