import time

from colorama import Fore

bridge_script_version = "Bridge Script V 1.0"
print(Fore.RED + bridge_script_version)
print(Fore.WHITE)

phone = input("Enter Phone Number if Phones to Bridge> ")
print("- Bridging 2 phones @ {}".format(phone))

time.sleep(2)

print("- Bridging 4 phones @ {}".format(phone))
