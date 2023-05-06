import json

json_path = '/home/verma/fabric-samples/asset-transfer-basic/chaincode-javascript/lib/data.json'
 
f_in = open(json_path)
k = json.load(f_in)
print('All the passwords available here for website are:')
for i in range(len(k)):
    print(f"The websites stored are: {i+1}.", k[i]['Website'])
