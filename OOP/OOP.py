# This is a quick program to illustrate the basics of OOP in python 

class Dog():

	def __init__(self, name, breed, age, smart):
		self.breed = breed
		self.name = name 
		self.age = age
		self.smart = smart

	def bark (self):
		print ("WOOF WOOF!! My name is {} and I am {}".format(self.name, self.age))

my_dog = Dog(name = "BoBy", breed = "Hoksy", age = 25, smart =  True)

my_dog.bark()
