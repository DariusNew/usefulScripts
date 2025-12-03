import subprocess
import os
import threading 
from tqdm import tqdm

FNULL = open(os.devnull, 'w')

class ConnectivityTester():
	def __init__(self, targets, num_threads: int):
		self.targets = targets
		self.targets_dict = {}
		self.num_threads = num_threads

	def ping(self, host: str):
		result = subprocess.run(['ping','-n','1',host], capture_output=True,text=True)
		if result.returncode == 0:
			self.targets_dict[host] = True
		else:
			self.targets_dict[host] = False

	def run(self):
		number = 0
		threads = []
		pbar = tqdm(total = len(self.targets))
		while number < len(self.targets):
			threads.clear()
			for i in range(self.num_threads):
				if (number + i) < len(self.targets):
					ping_thread = threading.Thread(target=self.ping, args=(self.targets[number+i],))
					threads.append(ping_thread)
					pbar.update(1)
				else:
					pass
			[t.start() for t in threads]
			[t.join() for t in threads]
			number += self.num_threads

		pbar.close()
		for target in self.targets_dict.keys():
			if self.targets_dict[target]:
				print(f"--- Target {target} is reachable ---")
			else:
				print(f"--- Target {target} is unreachable ---")