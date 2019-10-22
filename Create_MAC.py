#-*- coding: utf-8 -*-

from time import sleep
from os import remove
from os import system
from openpyxl import load_workbook
import csv
import re
from os import urandom
from random import choice
import MySQLdb

try:
    remove('Create_CFG_Grandstream/MAC.csv')
except OSError:
    print("Error remove")
    pass

try:
    remove('MACTEST.csv')
except OSError:
    print("Error remove")
    pass

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="PASSWORD",
                  db="Prod6",
                  charset="utf8"
                 )
x = conn.cursor()

def csv_writer(data, path):
    with open(path, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


sql="SELECT * FROM users;"
x.execute(sql)

for row in x:
     #print(row[7],row[1],row[8],row[1],"172.16.1.56")
     mac = row[9].encode('utf8', 'ignore')
     ext = row[2]
     secret = row[10].encode('utf8', 'ignore')
     ip3 = row[3]
     ip4 = row[4]
     #print(row)
     #d = row[1].encode('utf8', 'ignore')
     data1 = [['{},{},{},{},172.16.17.250,{}'.format(mac, ext, secret, ext, ext)]]
     path1 = "MACTEST.csv"
     csv_writer(data1,path1)

f6 = open("MACTEST.csv","r")
text_in6 = f6.read()
text_out5 = re.sub(r'"(?!")', '', text_in6)
#print(text_out)
#sleep(0.1)
f11 = open("Create_CFG_Grandstream/MAC.csv","wb")
f11.write(text_out5)
print("extension,secret,name,recording_in_external,recording_out_external,recording_in_internal,recording_out_internal,namedcallgroup,namedpickupgroup  ¯\_(ツ)_/¯")

