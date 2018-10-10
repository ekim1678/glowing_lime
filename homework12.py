class Robot:
	position = 0
	cube = False
	arm_position = 0
	score = 0

	def move(self, move):
		self.position += move

	def arm(self, arm_position):
		self.arm_position += arm_position

	def pick_up(self):
		if self.arm_position == 0 and self.position == 3 and self.cube == False:
			self.cube = True

	def tally(self):
		if self.cube == True and self.position == 7 and self.arm_position == 10:
			self.score += 5