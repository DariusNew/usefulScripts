import threading 
import paramiko
import socket
from tqdm import tqdm

class SSHTester():
    def __init__(self, targets, user_list, pass_list, num_threads: int):
        self.targets = targets
        self.users = user_list
        self.passkeys = pass_list
        self.targets_dict = {}
        self.targets_creds = {}
        self.targets_error = {}
        self.num_threads = num_threads

    def test_ssh(self, host: str):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.targets_dict[host] = False
        self.targets_error[host] = []
        for username in self.users:
            for passkey in self.passkeys:
                if not self.targets_dict[host]:
                    try:
                        ssh.connect(host, username=username, password=passkey, timeout=10)
                        self.targets_dict[host] = True
                        self.targets_creds[host] = (username, passkey)
                    except (paramiko.ssh_exception.BadHostKeyException, paramiko.ssh_exception.AuthenticationException, paramiko.ssh_exception.UnableToAuthenticate, socket.error) as e:
                        self.targets_dict[host] = False
                        self.targets_error[host].append(e)
        
    
    def run(self):
        number = 0
        threads = []
        pbar = tqdm(total = len(self.targets))
        while number < len(self.targets):
            threads.clear()
            for i in range(self.num_threads):
                if (number + i) < len(self.targets):
                    ssh_thread = threading.Thread(target=self.test_ssh, args=(self.targets[number+i],))
                    threads.append(ssh_thread)
                    pbar.update(1)
                else:
                    pass
            [t.start() for t in threads]
            [t.join() for t in threads]
            number += self.num_threads

        pbar.close()

        for target in self.targets_dict.keys():
            if self.targets_dict[target]:
                print(f"--- SSH client {target} is able to authenticate with {self.targets_creds[target][0]}:{self.targets_creds[target][1]}---")
            else:
                print(f"--- SSH client {target} is unable to authenticate ---")
                print(self.targets_error[target])