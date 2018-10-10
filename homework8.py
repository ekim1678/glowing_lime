#part one
list1 = []
boolean = False
while boolean == False:
	user = input("Enter something to put into a list: ")
	if user == "Stop" or user == "stop":
		boolean = True
	else:
		list1.append(user)
print(list1)
#part two
list2 = ["anything", "in", "it"]
tsil = []
for i in range(1,len(list2)+1):
    tsil.append(list2[-i])
print(tsil)