###############################
# Title: Library Program
# Authors: Osama Ashraf & Muhammad Radwan
# Version: v2.0
# Description: -----
################################

from functions import *

print('-----------------------------------------------')
print('-----------------Library App-------------------')

while True:
    print('-----------------------------------------------')
    print('1) Add New book')       # Done
    print('2) Remove book')
    print('3) I read some pages')
    print('4) Get book details')    # Done
    print('5) Show my Library')     # Done
    print('6) Sort my library')
    print('7) Mark page')           
    print('8) Find books by [Title, Date, Status, Author]') # Done
    print('9) Modify book details') # To-Do
    print('0) Exit')                # Done
    print('00) Clear Screen')       # Done
    print('-----------------------------------------------')
    

    choice = input()
    check(choice)
    
    print('\n-----------------------------------------------')

