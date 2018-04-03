import time
from datetime import datetime as dt

# Host Files
# Windows: c:\\windows\system32\drivers\etc
# Mac & Linux: /etc/hosts

# make a copy of your hosts, as a backup
hosts_path_windows = r"C:\Windows\System32\drivers\etc\hosts"
hosts_path_unix = "/etc/hosts"
# host_dir = "hosts"
host_dir =  hosts_path_unix 

redirect = "127.0.0.1"

# list of websites to block
website_list = [
    "www.facebook.com",
    "facebook.com",
    "mail.google.com"
]

# Define working hours
from_hour = 2
to_hour = 16

# Main Program
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print("Working hours...")
        with open(host_dir, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_dir, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() 
        print("Fun Hours")
    time.sleep(1) #seconds


