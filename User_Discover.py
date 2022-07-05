#Made by Copecofee

#Importing Modules

from os import *
from colorama import *
init(autoreset=True)

#Clearing the screen

system("clear")

def main():
 checking = getlogin()
 users = listdir("/home")
 print("The user of the system is: "+Fore.BLUE+f"{checking}")

 for x in users:
   print("Users found: "+Fore.RED+f"{x} ")

 #A funcao len() conta quantos items tem na lista

 print("Total Users: ", len(users))

if __name__ == "__main__":
 main()
