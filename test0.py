import subprocess

i = 0
while True:
    if i == 0:
        subprocess.Popen(["python","./test1.py"])
        subprocess.Popen(["python","./test2.py"])
        subprocess.Popen(["python","./test3.py"])
    i = 1
