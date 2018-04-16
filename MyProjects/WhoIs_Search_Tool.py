''' Who Is is a common command used to get information about a domain '''

from subprocess import call

def whois(n):
    return call(["whois", n])

ip = input("Enter an IP: ")
print (whois(ip))
