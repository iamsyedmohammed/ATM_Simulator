#Made by Syed Mohammed Akber Hussaini
#Can Follow me On IG @iamsyedmohammed
#It is a Simulation of Bank ATM and you are having a balance of Rupees 50000
import time
print("This is Protptype of ATM System")
balance=int(input("Enter an Amount to Deposit: \n₹"))
# Here You Can Choose The mode Of Transaction
trans=str(input("Enter The mode of Transaction\nDr, Cr:\n")).capitalize()
if trans=="Cr":
    print("You have Used Credit transaction with a limit of 30000")
elif trans=="Dr":
    print("You Have Choosen Debit")
else:
    print("Invalid Mode of Transaction")
    exit()
#You Can Enter The Amount of Money to be Withdrawn less than 50k
withdraw=int(input("Enter the amount to be Withdraw:\n₹"))
if withdraw>balance:
    time.sleep(1)
    print("You Don't Have Sufficient funds!!!!!")
    exit()
else:
    print("Enter Your Password")
#Your Password is needed for Completing the Transaction
paasw=str(input("")).lower()
if paasw=="xyz@123":
    time.sleep(1)
    print("Correct Password")
else:
    print("Invalid Password!!!")
    exit()
time.sleep(1)
print("Wait...")
time.sleep(1)
#If Your Password is Correct then Your Transaction will be succesfull
print("Your Transaction Was Successful")
balance=balance-withdraw
time.sleep(2)
#Here it will print the amount left after Transaction
print(f"\nTotal Amount left is ₹{balance}")






