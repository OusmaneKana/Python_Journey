from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt1= Point(1,2)
pt2= Point(3,4)
dot_product= ( pt2.x * pt2.x) + (pt1.y * pt2.y)
print (dot_product)