#!/usr/local/bin/python
import requests
import json
import os
from datetime import datetime

print ("\nsectrails.py Subdomain Scanning\n")

json_data_list = []
s = datetime.now()

def get_sub_domains(domain,filepath):

  url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"
  
  #print(url)
  querystring = {"children_only":"true"}
  headers = {
  'accept': "application/json",
  'apikey': "YOUR API KEY"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  result_json=json.loads(response.text)
  sub_domains=[i+'.'+domain for i in result_json['subdomains']]
  
  for j in sub_domains:
    print('[+] Discovered subdomain: '+j)
    json_data_list.append(j)
  return sub_domains
 
  #SAVE
  f=open(filepath,'w+')
  for i in sub_domains:
    f.write(i+'\n')
  return sub_domains


domain = input("\nMasukkan nama domain : ")
filepath = input("\nBerikan nama file untuk di simpan : ")
print('')

print("Starting scan at :",s)
print("*"*50)
print('')

get_sub_domains(domain,filepath)

#hasil json
with open("data_sectrails.json", "w") as write_file:
    json.dump(json_data_list, write_file)
# print(json.dumps(json_data_list))

print('')
print("*"*50)
print("End scan. Total time :",datetime.now()-s)
