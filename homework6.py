patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
num = 0
def calculate_bmi(weight, height):
	return weight / (height ** 2)
for patient in patients:
	weight, height = patients[num]
	bmi = calculate_bmi(weight, height)
	print("Patient's BMI is: " + str(bmi))
	num = num + 1