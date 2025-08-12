#How to install external libraries/packages using pip
#pip install <packageName>

#how to use after installing external package
from colorama import init

#use constructors
init()

from colorama import Fore
print(Fore.RED+"This is RED Text")
print(Fore.YELLOW+"This is YELLOW Text")