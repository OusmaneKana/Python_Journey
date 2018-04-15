def my_func(*args):
    l =[even for even in args if even%2 ==0]
    return l

print(my_func(1,2,3,4,5,6,9))    
