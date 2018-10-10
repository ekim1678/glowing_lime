#part one of lesson 7
listthing = ["The", "Glorified", "Clawbot", "Shall", "Carry", "On", "Signed", "Team", "QWERTY", "85454A"]
user = input("Type in a word to add to my list! ")
if user in listthing:
	print("Your word already exists in my list!")
else:
	listthing.append(user)
print(listthing)
#part two of lesson 7
create = []
name = input("Enter your name: ")
name = name.capitalize()
color = input("Enter your favorite color: ")
pets = input("Enter how many pets you have: ")
create.append(name)
create.append(color)
create.append(pets)
print(create[0] + "'s favorite color is " + create[1] + ". They have " + create[2] + " pets." )
#part three of lesson 7
bankaccounts = {TWAGA:-10, QWERTY:500, Asteria:1,000, Davis Express:450, Vexation:700, Texan asian fam:500, Hunters:800, Explorers:0, Marvelous Megabots:550, OACKS: 1000000000000000000}
#to retrieve the information for the key, you have to input the key
user = input("Enter your password: ")
if user in bankaccounts:
	print(bankaccounts.get(user))
else:
	print("Your password does not match any current accounts.")
#creating a new account
key = input("Enter a password for your new account: ")
value = input("How much money are you putting in your account? ")
bankaccounts[key] = value
#deleting an account
delete = input("What is the password of the account you want to remove? ")
bankaccounts.pop(delete)