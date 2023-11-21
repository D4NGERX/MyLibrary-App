###############################
# Title: Library Program
# Authors: Osama Ashraf & Muhammad Radwan
# Version: v1.0
# Description: -----
################################

from functions import *

print('-----------------------------------------------')
print('-----------------Library App-------------------')
print('-----------------------------------------------')
while True:
    print('1) Add New book')
    print('2) Remove book')
    print('3) I read some pages')
    print('4) Get book details')
    print('5) Show my Library')
    print('6) Sort my library')
    print('7) Mark page')
    print('0) Exit')
    print('00) Clear Screen')
    print('-----------------------------------------------')

    choice = input()
    check(choice)