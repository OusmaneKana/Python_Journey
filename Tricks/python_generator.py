'''Python generator:
This is an example of python generator. It's very handy to write
memory efficient codes because it doesn't holdv values into memory, it just
uses them when it needs it.
To illustrate it, let's write a Fibonacci sequence generator using that concept'''

def gen_fibonacci(n):

    #Starting by the initial value that can be 0 or 1 (doesn't really matter)
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b


for number in gen_fibonacci(10):
    print(number)



# Without using this concept, we would have ended up sayign something like ......

def gen_fibonacci(b):
    a = 1
    b = 1
    output = []
    for i in range(b):
        output.append(a)
        a,b=b,a+b
    return output
#We would have had the same output but with less memory efficiency
