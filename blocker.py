import datetime
from msilib.schema import File
import time

endtime = datetime.datetime(2022, 7, 5)
redirect = "127.0.0.1"
blockList =  ["www.facebook.com", "www.instagram.com", ]
hostPath = "C:/Windows/System32/drivers/etc/hosts"

while True:
    if datetime.datetime.now() <endtime:
        print("Blocking...") 
        with open(hostPath, 'r+') as host_file:
            for block in blockList:
                content = host_file.read()
                for website in blockList:
                    if website not in content:
                        host_file.write(redirect+" "+block + "\n")
                    else:
                        pass
    else:
        print("unblocking...")
        with open(hostPath, 'r+') as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in blockList):
                    host_file.write(lines)
            host_file.truncate()
        
        time.sleep(5)
    