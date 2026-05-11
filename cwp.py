# # assignment 1
# firstName = "Daniel"
# lastName = "Silver"
# print(type(firstName), type(lastName))
# #assignment 2
# age = 365
# print(type(age))
# #asignment 3
# greeting = "Yo "
# print(greeting + " " + firstName + " " + lastName + "your age is " + str(age))
# # i am silver. practiced a bit in python and hopefully i can keep up with life even though i dont want to anymore
# #assignment 4
# name = "Bola"
# age = 15
# print("hello! " + name + " " + str(type(age)))



# # Assignment 2
# simple calculator 
# num1 = input("enter first number")
# num2 = input("enter second number")
# op = input("what operation + for addition ...")
# try:
#     num1 = float(num1)
# except ValueError:
#     num1 = float(input("enter first number an actual number do not stress me"))
# try:
#     num2 = float(num2)
# except ValueError:
#     num2 = float(input("enter second number an actual number do not stress me"))

# if op == "+":
#     print (num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("wrong operation try again")





# Percentage calculator
# number = float(input("enter a digit"))
# percentage = float(input("what percentage would you luke calculated"))
# fractioned = (percentage/100) * number
# print(f"{percentage} of {number} is {fractioned}")




# 1. Smart Security System: Create variables for has_keycard, knows_password, 
# and is_admin. 
# Allow access only if (has_keycard AND knows_password) OR is_admin is True.

# print("smart security system duhh....")
# has_keycard = False
# knows_password = False
# is_admin = False

# print("Enter Keycard to gain access...\n")
# keycard = input("Village hidden in the leaf is called K___ha").lower()
# if keycard == "konoha":
#     has_keycard = True
# elif keycard == "admin":
#     is_admin = True
# print("verifying keycard")
# password = input("enter your password Hint: Marvel God of Thunder").lower()
# if password == "thor":
#     knows_password = True

# print("veryfing clearance \n")
# if has_keycard and knows_password:
#     print("access granted clearance level: 6")
# elif is_admin:
#     print("admin clearance")
# else:
#     print("intruder alert. alert alert\n self destruct sequence initiated")


# A user can checkout only if they have items in cart AND payment is successful. 
# If not, print appropriate messages explaining why checkout failed.

# print("welcome to the checkout verse")
# cart = input("enter what you would like to purchase")
# pay = input("enter your card to pay")
# if cart != "":
#     if len(pay) == 10:
#         print("payment succesful")
#     elif len(pay) != 10:
#         print("payment declined")
# elif cart == "":
#     print("cart is empty payment declined")


# Traffic Light Simulator: Create a variable light_color (red, yellow, green). 
# Use if/elif/else to print what action a driver should take.
# print("traffic light sim")
# light_color = "red"
# if light_color == "red":
#     print("stop now!!!")
# elif light_color == "yellow":
#     print("slow down possible light change")
# else:
#     print("Go, go, go")


# A student can take an exam only 
# if attendance is above 75% AND fees are paid. 
# Otherwise, explain the reason.

# attendance = input("what percentage score do you have on your attendance")
# fees = input("fees status cleared type y for yes").lower()
# affirm = ["y", "yes", "of course"]
# if int(attendance) > 75 and fees in affirm:
#     print("Auth successful proceed to exam")
# elif int(attendance) <= 75:
#     print("attendance short of criteria")
# else:
#     print("No school fees no exams")


# 5. Weather Decision Maker: Use is_sunny, 
# is_windy, and is_raining to decide if someone should go outside, 
# stay home, 
# or carry an umbrella. 
# Combine multiple logical conditions.

#weather decision maker
# affirm = ["y", "yes", "of course"]
# is_sunny = input("is it sunny Y/N")
# if is_sunny in affirm:
#     is_sunny = True
# else:
#     is_sunny = False

# is_windy = input("is it windy today Y/N").lower()

# is_windy = input("is it windy")
# if is_windy in affirm:
#     is_windy = True
# else:
#     is_windy = False

# is_windy = input("is it windy today Y/N")

# is_raining = input("is it raining")
# if is_raining in affirm:
#     is_raining = True
# else:
#     is_raining = False

# if is_raining and is_windy:
#     print('stay inside ooo')
# elif is_raining or is_sunny:
#     print("pick umbrella")


import random
myList = []
for x in range(6):
    myList.append(random.randint(1, 100))
print(f"your list is : {myList}")
print(len(myList))
print("\n")

for x in range(len(myList)):
    print(myList[x])
print("\n")

for x in range(len(myList)):
    if myList[x] > 10:
        print(myList[x])
print("\n")

print("modulo")
num = 0
for x in range(50):
    num = x
    if num % 4 == 0  and num % 8 != 0:
        print(num)
print("\n")

print("nest for ")
colors = ["blue", "green", "yellow"]
objects = ["car", "house", "shirt"]
skip = colors[1]

for color in colors:
    for object in objects:
        if color == skip:
            pass
        else:
            print(f"{color} {object}")


print("\n")
print("stars")
star = "*"
for i in range(5):
    for n in range(5):
        print(star, end=" ")
    print()
print()
inc = 0
for i in range(5):
    for n in range(5):
        if n == inc:
            print(star, end=" ")
        else:
            print(" ", end=" ")

    inc += 1
    print()
print()
print("sum of scores")
scores1 = [10, 20, 30]
scores2 = [5, 15, 25]

for score in scores1:
    for x in scores2:
        sum = score + x
        if sum > 30:
            print(sum)

