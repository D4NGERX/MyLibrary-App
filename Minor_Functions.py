from Config import *
from Style import *

def get_books(): # Osama    # Get books details list
    books_details = []
    database = open(DATABASE_PATH, 'r') # Opening input file
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
    output_file = open(OUTPUT_PATH, 'a')
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

def update_database(library):
    database = open(DATABASE_PATH, 'w') # Clearing Database
    database.write(TABLE_HEADER)                                      # Appending table Header
    database.close()
    database = open(DATABASE_PATH, 'a')
    for book in library:  # Formatting lines to be printed in terminal and output.txt file
        pages = book[1].split('/')  # Sparate pages read from total pages
        database.write(formatting(book[0], pages[1], book[3], book[5], book[4], pages[0], book[2][:-1]))  # -1 for deleting % character as it is added by default in formatting() function
        database.write('\n'+SEPARATING_LINE)  # Printing Separating Line

    database.close()

def choose_book(library):
    books_list = []
    for book in library:
        books_list.append(book["book name"])
    print("Choose the book: ")
    for book in range(len(books_list)):
        print(f"{book + 1}. {books_list[book]}")
    while True:
            try:
               choose = integer_only("Choose book: ", "INVALID! Integers only")
               if 0 < choose <= len(books_list) :
                   break
            except:
                print("OUT OF RANGE! Choose one of the above options") 
    return choose

def integer_only          (instructions, Error_Massage):
    while True:
            try:
                variable = int(input(instructions))
                break
            except:
                print(Error_Massage)
    return variable

def clac_percentage(library, choose):
     library[choose - 1]["percentage"] = f"{int((int(library[choose - 1]['book pages'].split(' / ')[0]) / int(library[choose - 1]['book pages'].split(' / ')[1])) * 100)}%"
     full_percentage(library, choose)

def full_percentage       (library, choose):
    if library[choose - 1]["book pages"].split('/')[0] == library[choose - 1]["book pages"].split('/')[1]:
        print("Congratiolatins!! You have finished the book")
        library[choose - 1]["status"] = "Finished"
        # rating_after_finishing(library,choose)
