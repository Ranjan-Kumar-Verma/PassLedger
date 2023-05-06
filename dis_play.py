import json

json_path = '/home/verma/fabric-samples/asset-transfer-basic/chaincode-javascript/lib/data.json'
 
f_in = open(json_path)
k = json.load(f_in)
print("Blocks present in the PassLedger are: ")
print(k)
print("\n")


