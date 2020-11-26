# Create Hacash Wallet
import json
import requests

N = input("Enter no. of wallet to be created 1 - 200: ")

url = ("http://rpcapi.hacash.org/create?action=accounts&number="+N)
result = requests.get(url)
src = result.text
data = json.loads(src)

for i in data['list']:
    print("Address: ")
    print(i['address'])
    print("Private Key: ")
    print(i['prikey'])
    print("\n")
