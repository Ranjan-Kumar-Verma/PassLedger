import pyotp
import time
import qrcode as qr 
import json


json_path = '/home/verma/fabric-samples/asset-transfer-basic/chaincode-javascript/lib/data.json'

f_in = open(json_path)
k = json.load(f_in)
print('All the passwords available here for website are:')
for i in range(len(k)):
    print(f'The websites stored are: {i+1}', k[i]['Website'])
in_web = int(input("Enter the website's crossponding number, which you want to view: "))
print("You have selected: ", k[in_web-1]['Website'])
print("\n")
print("Displaying the crossponding username, password and crossponding 2FA OTP.")

print("\n")
#print(k[in_web-1]['Username'], 'This is the username.')
#print(k[in_web-1]['Password'], 'This is the password.')
totp = pyotp.TOTP(k[in_web-1]["AuthenticationKey"])
#print(totp.now(), 'is the OTP.')

print('Username: ', k[in_web-1]['Username'])
print('Password: ', k[in_web-1]['Password'])
print('OTP     : ', totp.now())




print("The URL to access the 2FA code on your authenicator application is:")
print(pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='alice@google.com', issuer_name='Secure App'))

def qr_img(data):
    img = qr.make(data)
    img.show()
    

print("\n")
inj = input("Enter Y/y to generate of QR code to add the 2FA into your authenticator application.")
if(inj == 'y' or inj == 'Y'):
    qr_img(k[in_web-1]["AuthenticationKey"])


