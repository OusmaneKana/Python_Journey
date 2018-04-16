from collections import Counter
l =[1,1,1,1,2,7,5,8,9,5,5,8]

# Helps you count the number of "items" in on obkect and stores the values in a dictionnary
print (Counter(l))

# Example of Counter method applied to a setence

S = " This is an Example of the the counter method used in in python"
words = S.split()
print (Counter(words))
