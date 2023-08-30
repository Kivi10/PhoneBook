import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

from algorithm import *
from functional import *

while True:
    clear()
    print_instructions()
    Choose(input("Введите команду (1 2 3 4 5 или 6) "))
    input("Нажмите enter чтобы продолжить")