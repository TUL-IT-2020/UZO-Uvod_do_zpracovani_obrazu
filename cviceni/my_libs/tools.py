# By Pytel

import os

def clear():
    """ Clear console """
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    #os.system('cls' if os.name == 'nt' else 'clear')

