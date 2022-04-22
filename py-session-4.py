#import numpy as np

class animalSpecs:

	def __init__(self,ani):
		self.arms = ani[0]
		self.legs = ani[1]
		self.eyes = ani[2]
		self.tail = ani[3]
		self.fur = ani[4]

	def animal(self):
		print(f"Length of Arms (inches) = {self.arms}")
		print(f"Lenght of Legs (inches) = {self.legs}")
		print(f"Number of Eyes = {self.eyes}")
		print(f"Has a tail? = {self.tail}")
		print(f"Furry? = {self.fur}")


def main():

	raccoon = [12.0,12.0,2,True,True]

	raccoonClass = animalSpecs(raccoon)
	raccoonClass.animal()

if __name__=="__main__":
	main()
