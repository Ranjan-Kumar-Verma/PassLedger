import json
import os

json_path = '/home/verma/fabric-samples/asset-transfer-basic/chaincode-javascript/lib/data.json'

print("Now you are entering the python script to enter the value in blockchain:\n")
ID = input("Enter the ID for the information block to be created: ")
Website = input("Enter the website name where the block has to be entered: ")
User_name = input("Enter the Username used for the given Website: ")
Password = input("Enter the password of the added node: ")
Auth_key = input("Enter the 2FA key: ")
new_block = { 'ID': ID, 'Password':Password, 'AuthenticationKey': Auth_key, 'Website':Website, 'Username': User_name}
data = new_block
with open (json_path, 'a+') as f:
    f.seek(0, os.SEEK_END)
    f.seek(f.tell() - 2, os.SEEK_SET)
    f.truncate()
    f.write(",")
    f.write(json.dumps(data))
    f.write("]")
    f.write("")
f.close()
print('The new block which will be added here is: ')
print(new_block)

