import shutil
import os
import time

paths = [
    r"C:\Users\oni\AppData\Local\Roblox\Downloads",
    r"C:\Users\oni\AppData\Local\Roblox\LocalStorage",
    r"C:\Users\oni\AppData\Local\Roblox\logs",
]

for path in paths:
    if os.path.exists(path):
        shutil.rmtree(path)
        print("remove")
        time.sleep(10)
else:
    print ("")
    time.sleep(3)