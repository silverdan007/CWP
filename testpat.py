# Write a Python program using a while loop that asks the user to enter a password continuously 
# until they enter the correct password or run out of attempts. The correct password should be 
# python123, and the user should only have 3 attempts. If the user enters the correct password, 
# print "Access Granted". If the password is incorrect, print "Wrong Password" 
# along with the number of attempts left. After 3 failed attempts, print "Account Locked"

print("password try")
correct = "python123"
present_value = input("Enter password")
test = True
i = 1
while test:
    if present_value == correct:
        print("Access Granted")
        break
    elif present_value != correct:
        present_value = input("Enter password")
        i += 1
        if i == 3:
            test = False
            print("Account Locked")


