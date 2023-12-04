###############################
# Title: Library Program
# Authors: Osama Ashraf & Muhammad Radwan
# Version: v2.5
# Description: -----
################################

from Major_Functions import *

print('-----------------------------------------------')
print('-----------------Library App-------------------')

while True:
    main_menu()
    choice = input()
    try:
        check(choice)
    except:
        print('Enter a Valid value!')
    
    print('\n-----------------------------------------------')

