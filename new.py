import os

print("\nWelcome to PassLedger a cutting edge Blockhain based password manager and 2FA authenticator.")

print("\nAn innovation by Ranjan Kumar Verma (CTO), Saumya Vilas Roy (CPO) and Sanyam Kaushik (CEO) ")
y = 'y'
while y == 'y' or y == 'Y':
    print("Enter 1. to show current blocks in the ledger: \nEnter 2. to add a new block: \nEnter 3. to access the saved data:")
    a = int(input("Enter your choice: "))
    if a == 1:
        os.system("python3 show.py")
        print("\n")
    elif a == 2:
        os.system("python3 enter_val.py")
        os.system("bash beforebasic.sh")
        os.system("python3 dis_play.py")
        print("\n")
    elif a == 3:
        os.system("python3 read_val.py")
        print("\n")
    y = input("\nEnter y/Y to continue using this program.")
print("End of the program exiting.")


