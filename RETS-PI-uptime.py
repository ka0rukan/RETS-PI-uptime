#Using python 3.5.2

__author__ = 'brbuxton'
import requests, json

#please fill in user and password below

user = ''
password = ''
url = 'https://'+user+':'+password+'@192.168.144.147/webacs/api/v1/data/'

#There are two different Device Detail resources we will be using.  Devices and InventoryDetails
#https://192.168.144.147/webacs/api/v1/index?_docs#Device Details

InventoryDetail = 'InventoryDetails/'
Devices = 'Devices.json'

#First we need a list of devices by entityId which we will pass through a FOR loop
deviceurl = url+Devices
respDict = requests.get(deviceurl,verify=False)
#print(respDict.content)
respDict_json = respDict.json()
#print(respDict_json['queryResponse']['entityId'])

#We pass the entire response through the FOR loop and pull out the '$' value of the entityId.
#We then create a new request inside the loop to get the InventoryDetails for that entityId.

for entity in respDict_json['queryResponse']['entityId']:
    #print (entity['$'])
    inventoryurl = url+InventoryDetail+entity['$']+'.json'
    #print (inventoryurl)
    response = requests.get(inventoryurl,verify=False)
    response_json = response.json()
    print (response_json['queryResponse']['entity'])
    #Having successfully printed each entity, I next need to work on extracting only the 'summary' section
    #and the 'upTime' value within it.

