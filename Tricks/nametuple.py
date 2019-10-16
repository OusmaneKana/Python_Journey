# """ Let's say that I want to create a program that calculates the slope of a line.
# I would need:
# 1- The x,y coordinates of all the line I wouls expect

# """
# from collections import namedtuple


# #Create the "kinda object" point
# Point = namedtuple('Point', 'x,y')
# #Initialize all the points I would to calulate the slope of that line 
# pnt1 = Point(input("x1= "),input("y1= "))

# pnt2 = Point(input("x2= "),input("y2= "))
# #Write the slope formula 
# slope = (pnt2.y - pnt1.y) / (pnt2.x - pnt1.x)
# #So right after that I will have to go 
# print(slope) 
# #SO them When we will haveto do ut we This is the thing I'll be f
# #DOing and we just have to come and go but dayyuuummm



""" Do the this wiht OOP
"""

xs = [1,2]
ys = [3,4]
class SlopeFnder:
	def __init__(self, xs, ys):
		self.xs = xs
		self.ys = ys

	def slope (xs,ys):

		slope = ((ys[1]-ys[0])/(xs[1]-xs[0]))
		return (slope)

	def __str__():
		print(slope())
print(SlopeFnder.slope(xs, ys))



