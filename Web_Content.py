#Made by Copecofee


#Importing Modules

import requests
from bs4 import BeautifulSoup
from os import system as exe
import colorama

#init of the colorama

colorama.init(autoreset=True)

#Clearing the Screen

exe("clear")

#Setinng up the main function

def main():
    the_website = input(str("The website: "))

    try:
     r = requests.get(f'{the_website}').content
    except:
     r = requests.get(f'http://{the_website}').content

    soup = BeautifulSoup(r, 'html.parser')

    print(soup)

if __name__ == "__main__":
                          main()
