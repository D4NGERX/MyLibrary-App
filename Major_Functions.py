from Config import *
from Style  import *
from Minor_Functions import *

def main_menu():            # Osama   # Printing Main Menu
    print('-----------------------------------------------')
    print('1) Add New book')       # Done
    print('2) Remove book')        # Under Dev
    print('3) I read some pages')   #Done
    print('4) Get book details')    # Done
    print('5) Show my Library')     # Done
    print('6) Sort my library')     # Under Dev
    print('7) Mark page')           
    print('8) Find books by [Title, Date, Status, Author]') # Done
    print('9) Modify book details') # Done
    print('0) Exit')                # Done
    print('00) Clear Screen')       # Done
    print('-----------------------------------------------')

def check(choice):          # Osama   # Checking User Choice
    output_file = open(r'D:\PROJECTS\Library Project\output.txt', 'w') # Making Sure That output file is opened and clean
    if choice == '1':
        add_new_book()
    
    # elif choice == '2':
    #     remove_book()
    # elif choice == '3':
    #     read_pages()
    #     calc_percent()
    #     modify(title, new_percent)
    #     if percent == 100:
    #           modify(title, status, 'Finished')
    #           rate_book(title)
    
    elif choice == '4':
        title = input('Enter book Title: ').lower()
        show_books_by('title', title)
    
    elif choice == '5':
        show_library()
    
    # elif choice == '6':
    #     sort_library()
    # elif choice == '7':
    #     mark_page()
    
    elif choice == '8':
        parameter = input('Choose parameter[Date, Status, Author]: ').lower()
        while parameter not in ['date', 'status', 'author']:       # input correction
            print('Please, Enter a valid choice !')
            parameter = input('Choose parameter[Date, Status, Author]: ').lower()

        
        value = input('Enter value: ').lower()
        show_books_by(parameter, value)
    
    elif choice == '9':
        title = input('Enter book title: ').lower()
        while not check_found(title):
            print('Book not found !')
            title = input('Enter book title: ').lower()
        
        parameter = input('Enter parameter to change: ').lower()
        while parameter.lower() not in parameters:
            print('Enter a valid choice!')
            parameter = input('Enter parameter to change: ').lower()
        modification = input('Enter new value: ')
        modify(title, parameter, modification)

    elif choice == '0':         # exiting program using exit() function
        exit()
    
    elif choice == '00':
        clear_screen()
        print('-----------------------------------------------')
        print('-----------------Library App-------------------', end='')
    
    else:
        print('Enter a valid choice \n')

def add_new_book():         # Osama   # Adding book to Library
    title = input('Book title: ').capitalize()
    Total_pages = input('Number of pages: ')
    author = input('Author name: ').capitalize()
    start_date = input('Start Date: ')
    status = input('What is the status of the book ?[reading - wishlist - finished]: ').capitalize()

    database_a = open(r'D:\PROJECTS\Library Project\database.txt', 'a')
    database_a.write(formatting(title, Total_pages, start_date, author, status))
    database_a.write('\n'+separating_line)
    database_a.close()

def show_library():          # Osama   # Showing th Whole Library
    database = open(r'D:\PROJECTS\Library Project\database.txt', 'r')
    lines = database.readlines()

    for line in lines:
        output(line)

def show_books_by(parameter, value):    # Osama         # Find books with parameter value
    database = open(r'D:\PROJECTS\Library Project\database.txt', 'r') # Opening input file
    lines = database.readlines()

    
    
    results = []       # Result books

    for line in lines:        # Search book by book
        whole_line = line

        line = line.replace('\t', '').split('|')      # Clearing line
        line = removeAll(line, '')                    #

        for i in range(len(line)):
            line[i] = line[i].replace(' ', '', 1)              # Clearing each string from prefix space

        if len(line) > 1 and line[guide[parameter]].lower() == value:
            results.append(whole_line)
     
    
    if results == []:             # Checking if results are found
        output('Not found')
    else:
        output(table_header)
        for result in results:
            output('\n'+result)        # output Found books
            output(separating_line)
    
    database.close()

def modify(title, parameter, new_value):
    books = get_books()
    for i in range(len(books)):
        if books[i][0].lower() == title:
            books[i][guide[parameter]] = new_value
            break
    
    database = open(r'D:\PROJECTS\Library Project\database.txt', 'w') # Clearing Database
    database.write(table_header)                                      # Appending table Header
    database.close()
    database = open(r'D:\PROJECTS\Library Project\database.txt', 'a')
    for book in books:  # Formatting lines to be printed in terminal and output.txt file
        pages = book[1].split('/')  # Sparate pages read from total pages
        database.write(formatting(book[0], pages[1], book[3], book[5], book[4], pages[0], book[2][:-1]))  # -1 for deleting % character as it is added by default in formatting() function
        database.write('\n'+separating_line)  # Printing Separating Line
    
    output('Modification Done !\n')
    database.close()
  
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


