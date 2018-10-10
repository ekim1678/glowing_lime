def homework1():
	print("My name is Ellie and I am 14.")
	print("This is how old I am in months: " + (str(int(14*12))))
	return

def homework2():
	print("Hello! Welcome to the Programming Pizza Place. How may I help you? ")
	pizzas = int(input("How many pizzas would you like? Enter a number: "))
	pepperoni = int(input("How many pepperoni slices would you like? Enter a number: "))
	olives = int(input("How many olives would you like? Enter a number: "))
	name = input("Can I please have a name for the order? ")
	name.capitalize()
	print(name + " ordered "+ str(pizzas)+ " pizzas with " + str(pepperoni) + " pepperonis and " + str(olives) + " olives.")
	return

def homework5(x):
	if x > 0 and x < 50:
		print("Your input is between 0 and 50!")
	elif x>50 and x<100:
		print("Your input is between 50 and 100!")
	elif x==50:
		print("Your number is 50!")
#I adjusted this line so that way when you put in 50 (which is between 0 and 100) it doesn't say you didn't follow instructions. 
	else:
		print("You didn't follow the instructions!")
	return

def homework6():
	patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
	num = 0
	def calculate_bmi(weight, height):
		return weight / (height ** 2)
	for patient in patients:
		weight, height = patients[num]
		bmi = calculate_bmi(weight, height)
		print("Patient's BMI is: " + str(bmi))
		num = num + 1
	return

def homework7(x):
	#part one of lesson 7
	listthing = ["The", "Glorified", "Clawbot", "Shall", "Carry", "On", "Signed", "Team", "QWERTY", "85454A"]
	if x in listthing:
		print("Your word already exists in my list!")
	else:
		listthing.append(x)
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
	bankaccounts = {"TWAGA" : -10 , "QWERTY" : 500 , "Asteria" : 1000 , "Davis Express" : 450 , "Vexation" : 700 , "Texan asian fam" : 500 , "Hunters" : 800 , "Explorers" : 1 , "Marvelous Megabots" : 550 , "OACKS" : 100000}
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
	return

def homework8(x):
	#part one
	list1 = []
	boolean = False
	while boolean == False:
		x = input("Add something to the list: ")
		if x == "Stop" or x == "stop":
			boolean = True
		else:
			list1.append(x)
	print(list1)
	#part two
	list2 = ["anything", "in", "it"]
	tsil = []
	for i in range(1,len(list2)+1):
		tsil.append(list2[-i])
	print(tsil)
	return


homework1()
homework2()
homework5(int(input("Type in a number between 0 and 100: ")))
homework6()
homework7(input("Type in a word to add to my list! "))
homework8(input("Enter something to put into a list. When you want to stop entering things, type Stop. "))