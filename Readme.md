## Python Tools

I wrote these scripts to make it easier to do connectivity checks in the future. 

### Files required
You will first need a directory containing the various IP addresses and credentials in the following text files:
- targets.txt --> ping targets
- linux.txt --> linux servers
- windows.txt --> windows servers
- users.txt --> list of usernames
- passwords.txt --> list of passwords

### Run Code
``` bash
python main.py -d dirName

python main.py -d dirName -t 10
```
