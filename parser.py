from pathlib import Path

class Parser():

	def __init__(self, foldername: Path):
		self.folder = foldername
	
	def test(self):
		result = True
		if not self.folder.exists():
			print ("Folder does not exist")
			result = False
		elif not self.folder.is_dir():
			print ("Folder is not a directory")
			result = False
		else:
			result = True

		return result

	def get_all_files(self):
		p = self.folder.glob('**/*')
		self.files = [x.name for x in p if x.is_file()]

		result = True
		## check files
		if 'targets.txt' not in self.files:
			result = False
		else:
			self.targets = self.read_file(self.folder.joinpath('targets.txt'))

		if result:
			if 'linux.txt' not in self.files:
				print ("linux targets not found")
			else:
				self.linux = self.read_file(self.folder.joinpath('linux.txt'))

			if 'windows.txt' not in self.files:
				print ("windows targets not found")
			else:
				self.windows = self.read_file(self.folder.joinpath('windows.txt'))

			if 'users.txt' not in self.files:
				print ("users not found")
			else:
				self.users = self.read_file(self.folder.joinpath('users.txt'))

			if 'passwords.txt' not in self.files:
				print ("passwords not found")
			else:
				self.passwords = self.read_file(self.folder.joinpath('passwords.txt'))		
		else:
			pass

		return result

	def read_file(self, filename: str):
		result = []
		with open(filename) as f:
			for line in f:
				ips = line.split(',')
				result += (ips)

		return result 

	def run(self):
		if not self.test():
			raise NameError("test failed")
		elif not self.get_all_files():
			raise NameError("targets.txt file missing in folder")
		else:
			pass
