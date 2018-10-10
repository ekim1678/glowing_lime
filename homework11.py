class Animal:
	def __init__(self,fur,glands,diaphragm):
		self.fur = fur
		self.glands = glands
		self.diaphragm = diaphragm
class Mammal(Animal):
	def __init__(self,fur,glands,diaphragm):
		self.fur = fur
		self.glands = glands
		self.diaphragm = diaphragm
class Cat(Mammal):
	def __init__(self,fur,glands,diaphragm):	
		self.fur = fur
		self.glands = glands
		self.diaphragm = diaphragm
my_cat = Cat(True, True, True)
print(my_cat.fur,my_cat.glands,my_cat.diaphragm)