import time
from datetime import datetime as dt

hosts_path = "hosts"
redirect = "127.0.0.1"  #localhost
block_websites = ["www.facebook.com", "facebook.com"]   #websites to be blocked

while True:
    if(dt(dt.now().year, dt.now().month, dt.now().day,20) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,23)):
        print("Work")
        with open("hosts", "r+") as file:
            content = file.read()
            for website in block_websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Funnn")
    time.sleep(5)
