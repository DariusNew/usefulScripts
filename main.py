from pathlib import Path
from parser import Parser
from connectivity import ConnectivityTester
from ssh import SSHTester
from smb import SMBTester
import argparse

if __name__ == '__main__':

	argparser = argparse.ArgumentParser()
	argparser.add_argument("-d", "--directory", type=str, help="directory for ip address, please put in double quotation marks")
	argparser.add_argument("-t", "--threads", type=int, help="number of threads", default=50)
	args = argparser.parse_args()

	if not args.directory:
		argparser.error("missing required directory arg")

	path = Path(args.directory)
	fileParser = Parser(path)
	fileParser.run()

	# test = ConnectivityTester(fileParser.targets, args.threads)
	# test.run()

	ssh = SSHTester(fileParser.linux, fileParser.users, fileParser.passwords, args.threads)
	ssh.run()

	smb = SMBTester(fileParser.windows, fileParser.users, fileParser.passwords, args.threads)
	smb.run()