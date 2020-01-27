# This represent the use of special functionc/methods in OOP context 
# For exemple calling some generic python methods (like len() on classes)

class Book():
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author 
		self.pages = pages

# mybook  = Book("The 1000 miles", "Serigne Ousmane Kana", 1000)
# print (mybook)
# print(len(mybook))
# At this stages use the print or len methods will end in error because 
# print will just return the address location of the object and len() can't be used 
# because not defines 

#We can instead create a special method for the methods calls ...... if it makes sense....

class Book():
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author 
		self.pages = pages

	def __str__(self):
		return f"{self.title} by {self.author}"

mybook  = Book("The 1000 miles", "Serigne Ousmane Kana", 1000)
print (mybook)