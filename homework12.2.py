from homework12 import Robot
robot_1 = Robot()
print("Control your robot! There are four functions you can choose from: tally, move, arm, and pick_up.")
for x in range(0,11):
	user = input("Type in a function: ")
	if user == "arm" or user == "move":
		word = input("How much would you like to move it? ")
		if user == "move":
			robot_1.move(int(word))
		elif user == "arm":
			robot_1.arm(int(word))
	if user == "tally":
		robot_1.tally()
	if user == "pick_up":
		robot_1.pick_up()
		#print the variables
	print("This is your position: " + str(robot_1.position))
	print("You have a cube: " + str(robot_1.cube))
	print("Your arm is this high: " + str(robot_1.arm_position))
	print("You have scored this many points: " + str(robot_1.score))