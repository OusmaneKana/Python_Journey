import string

def vol(rad):
	pi=3.14
	return (pi*(rad*rad))



def ran_check(num, low,high):
	if num in range(high, low):
		return true
	else:
		return false

# or
def ran_check(num, low, high):
	return num in range(high, low)


def up_low(s):
	d={"upper":0, "lower":0}
	for character in s:
		if character.isupper():
			d["upper"]+=1
		elif character.islower():
			d["lower"]+=1
		else: 
			pass
	print("The original string is ", s)
	print("The number of upper case characters are: ", d["lower"])
	print("The number of lower case characters are: ", d["upper"])

# Python function that prints the unique elements of a list and put it in another one

def uniq_list(u):
	l=[]
	for i in u:
		if i not in l:
			l.append(i)
	return l


# Python function that multiplies all the elements of a list 
def multiply(u):
	x=u[0]
	for i in u:
		x *= i
	return x

def palindrome(s):
	return s==s[::-1]

def ispangram (str1, alphabet=string.ascii_lowercase):
	alphaset = set(alphabet)
	return alphaset <= set(str1.lower())

