import time
from datetime import datetime as dt

hosts_path = "hosts"
redirect = "127.0.0.1"  #localhost
block_websites = ["www.facebook.com", "facebook.com"]   #websites to be blocked

while True:
    if(dt(dt.now().year, dt.now().month, dt.now().day,18) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,23)):
        print("Work")
        with open("hosts", "r+") as file:
            content = file.read()       #read the hosts file
            for website in block_websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open("hosts", "r+") as file:
            content = file.readlines()     #this will create list with each line as an element of list
            file.seek(0)                   #this will take the pointer to the 0th position of hosts file
            for line in content:
                if not any(website in line for website in block_websites):
                    file.write(line)
                file.truncate()            #this will delete any content written below the file pointer
        print("Funnn")
    time.sleep(5)
