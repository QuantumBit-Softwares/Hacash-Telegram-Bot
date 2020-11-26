import requests
import json

choice = input(" 1. Hacash Transfer\n 2. Hacash Diamond Transfer\n 3. Bitcoin Transfer\n")

# Hacash Transaction
if choice == "1":
    amount = input("Enter Hac Amount: ")
    to_address = input ("Enter Destination Address: ")
    main_prikey= input("Private key from Hac source: ")
    validation = input(f"Transferring {amount} HAC to {to_address}, type |confirm| to proceed. If you wish to cancel type |cancel| >>   ")
    if validation == "confirm":
        print("yes")
        url=("http://rpcapi.hacash.org/create?action=value_transfer_tx&main_prikey="+ main_prikey +"&fee=0.0001&unitmei=true&transfer_kind=hacash&amount="+amount+"&to_address="+to_address)
        result = requests.get(url)
        src = result.text
        dataRes = json.loads(src)
        if ((dataRes['ret']) == 0):
            params = (('action', 'transaction'),('hexbody', '1'),)
            data = (dataRes['body'])
            response = requests.post('http://rpcapi.hacash.org/submit', params=params, data=data)
            responseCurl = (response.text)
            dataJson = json.loads(responseCurl)
            if((dataJson['ret']) == 1):
                print("Transfer FAILED:" + (dataJson['errmsg']))
            if ((dataJson['ret']) == 0):
                print("Transaction ID:" + (dataRes['hash']))
                print("Transfer SUCCESS")
        if ((dataRes['ret']) == 1):
            print("Transaction ERROR. Please check you entries and try again.")
    if validation == "cancel":
        print("Transaction is CANCELLED")
# Hacash Diamond Transaction
# Bitcoin Transaction
