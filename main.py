import time
import colorama
from termcolor import colored
from colorama import Back, Fore, init

init()

print(Back.GREEN + Fore.BLACK + "IQ CALCULATOR 0.1")
print(Back.MAGENTA + Fore.WHITE + "enter your iq")
input = input("")
print(Back.BLUE + "calculating scores...")
time.sleep(3)
print(Back.YELLOW + Fore.BLACK + "You have", input + "IQ")