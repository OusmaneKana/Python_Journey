# This is an illustration of package using in Python.
#I ma basically calling creating packages ( in a relatively structired form)
# and call the in here which is supposingly my main file 

from PackageTemp import main_module
#/PackageTemp is a directory where I stored the script main_module.py 
from PackageTemp.Submodule import main_submodule
#Submodules plays the role of a subdirectory that contains another script main_submodule.py


#Calling the method/function from 
main_module.random()
main_submodule.sub_random()

