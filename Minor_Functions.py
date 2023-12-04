from Config import *
from Style import *

def get_books(): # Osama    # Get books details list
    books_details = []
    database = open(r'D:\PROJECTS\Library Project\database.txt', 'r') # Opening input file
    lines = database.readlines()
    for line in lines:
        line = line.replace('\t', '').split('|')      # Clearing line
        line = removeAll(line, '')                    #
        line = removeAll(line, '\n')

        for i in range(len(line)):
            line[i] = line[i].replace(' ', '', 1)              # Clearing each string from prefix space

        if len(line) > 1:
            books_details.append(line)


    database.close()
    return books_details[1:]

def output(string):         # Osama   # Printing Values in both terminal and output.txt file
    output_file = open(r'D:\PROJECTS\Library Project\output.txt', 'a')
    print(string, end='')
    output_file.write(string)
    output_file.close()

def check_found(title):
    books = get_books()

    for i in range(len(books)):
        if books[i][0].lower() == title:
            return True
    
    return False

def removeAll(list, value):     # Osama     # Removes all (value) from a list
    for e in list.copy():
        if e == value:
            list.remove(value)

    return list

def update_library(library):
    database = open(r'D:\PROJECTS\Library Project\database.txt', 'w') # Clearing Database
    database.write(table_header)                                      # Appending table Header
    database.close()
    database = open(r'D:\PROJECTS\Library Project\database.txt', 'a')
    for book in library:  # Formatting lines to be printed in terminal and output.txt file
        pages = book[1].split('/')  # Sparate pages read from total pages
        database.write(formatting(book[0], pages[1], book[3], book[5], book[4], pages[0], book[2][:-1]))  # -1 for deleting % character as it is added by default in formatting() function
        database.write('\n'+separating_line)  # Printing Separating Line

    database.close()
    