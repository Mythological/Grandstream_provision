#!/usr/bin/python3

import urllib.request
for i in range(1,248):
    try:
        try:
            contents = urllib.request.urlopen(f"http://192.168.16.{i}/cgi-bin/api-sys_operation?passcode=PASSWORD&request=REBOOT").read()
            print(i)
            print(contents)
        except:
            pass
        #print(i)
        #print(contents)
        #time.sleep(0.1)
        try:
            contents = urllib.request.urlopen(f"http://192.168.17.{i}/cgi-bin/api-sys_operation?passcode=PASSWORD&request=REBOOT").read()
            print(i)
            print(contents)
        except:
            pass
        #print(contents)
        #time.sleep(0.1)
        try:
            contents = urllib.request.urlopen(f"http://192.166.18.{i}/cgi-bin/api-sys_operation?passcode=PASSWORD&request=REBOOT").read()
            print(i)
            print(contents)
        except:
            pass
        #print(contents)
        try:
            contents = urllib.request.urlopen(f"http://192.168.20.{i}/cgi-bin/api-sys_operation?passcode=PASSWORD&request=REBOOT").read()
            print(i)
            print(contents)
        except:
            pass
    except:
        pass







#51 5 * * MON    /usr/bin/python3 /home/slevin/cgi-bin_Grandstream.py > /home/slevin/cgi-bin_Grandstream.log 2>&1
#http://192.166.18.204/cgi-bin/api-sys_operation?login=admin&password=PASSWORD&request=REBOOT
#http://192.166.16.6/cgi-bin/api-sys_operation?passcode=PASSWORD&request=REBOOT
