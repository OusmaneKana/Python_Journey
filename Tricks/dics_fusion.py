""" How to fusion two list in python"""

Dic1 ={
			'a':"1",
			'b':"2",
			'c':"3"
}


Dic2 ={
			'd':"4",
			'e':"5",
			'f':"6"
}


Dic={**Dic1, **Dic2}


print (Dic)