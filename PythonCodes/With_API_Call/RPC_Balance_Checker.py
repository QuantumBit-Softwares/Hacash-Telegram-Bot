import json
import requests

address_input = input("Enter your HAC address: ")

url = ("http://rpcapi.hacash.org/query?action=balances&address_list="+address_input)
result = requests.get(url)
src = result.text
data = json.loads(src)

if (data['ret'] == 0):
    print("HAC: ")
    print(data['list'][0]['hacash'])
    print("BTC: ")
    print (data['list'][0]['satoshi'])
    print("HACD: ")
    print(data['list'][0]['diamond'])
    
if (data['ret'] == 1):
    print("Query FAILED: " + (data['errmsg']))

