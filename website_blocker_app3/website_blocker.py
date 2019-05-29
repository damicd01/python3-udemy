import time
from datetime import datetime as dt

hosts_file='/etc/hosts'
redirect_ip='127.0.0.1'
website_list=['www.bbc.com','www.yahoo.com']

while True:
    time_now = dt.now()
    if dt(time_now.year, time_now.month, time_now.day, 8, 0, 0) < dt.now() < dt(time_now.year, time_now.month, time_now.day, 16, 0, 0):
        with open(hosts_file, "r") as myfile:
            contents=myfile.read()
            with open('/tmp/etc_hosts.tmp', 'a') as outf:
                outf.write(contents)
    else:
        with open(hosts_file, "r") as myfile:
            contents=myfile.read()
            with open('/tmp/etc_hosts.tmp', 'a') as outf:
                outf.write(contents)
                for i in website_list:
                    if i in contents:
                        pass
                    else:
                        outf.write(redirect_ip + ' ' + i + '\n')
    time.sleep(5)
