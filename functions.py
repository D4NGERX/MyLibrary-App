# Global Variables

table_header = '''+-------------------------------+---------------+-------+---------------+---------------+-----------------------+
|				|		|	|		|		|			|
| Title				| Pages		| per	| Date		| Status	| Author		|
|				|		|	|		|		|			|
+-------------------------------+---------------+-------+---------------+---------------+-----------------------+'''
separating_line = '+-------------------------------+---------------+-------+---------------+---------------+-----------------------+'
parameters = ['title', 'pages', 'percent', 'date', 'status', 'author']
guide = {    # Translating parameter into number
    'title' : 0,
    'pages' : 1,
    'percent': 2,
    'date' : 3,
    'status' : 4,
    'author' : 5
}

def main_menu():
    print('-----------------------------------------------')
    print('1) Add New book')       # Done
    print('2) Remove book')
    print('3) I read some pages')
    print('4) Get book details')    # Done
    print('5) Show my Library')     # Done
    print('6) Sort my library')
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
    #     modify(title, percent, new_percent)
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

def output(string):         # Osama   # Printing Values in both terminal and output.txt file
    output_file = open(r'D:\PROJECTS\Library Project\output.txt', 'a')
    print(string, end='')
    output_file.write(string)
    output_file.close()

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

def show_library():         # Osama   # Showing th Whole Library
    database = open(r'D:\PROJECTS\Library Project\database.txt', 'r')
    lines = database.readlines()

    for line in lines:
        output(line)

def formatting(title, totalPages, date, author, status, pages=0, percent=0):    # Osama     # generating line to be printed in a table shape
    title_cell = cell_format(title, 4)
    pages_cell = cell_format(f'{pages}/{totalPages}', 2)
    percent_cell = cell_format(f'{percent}%', 1)
    date_cell = cell_format(date, 2)
    status_cell = cell_format(status, 2)
    author_cell = cell_format(author, 3)

    result = f'\n| {title_cell}| {pages_cell}| {percent_cell}| {date_cell}| {status_cell}| {author_cell}|'
    return result

def cell_format(string, number_of_tabs):    # Osama     # Generating Cell Shape
    if len(string) < 6:
        string += '\t'*(number_of_tabs)
    elif len(string) < 14:
        string += '\t' * (number_of_tabs-1)
    elif len(string) < 22 and number_of_tabs > 2:
        string += '\t' * (number_of_tabs-2)
    elif len(string) < 39 and number_of_tabs > 3:
        string += '\t' * (number_of_tabs-3)
    else:
        string += ' '

    return string

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

def removeAll(list, value):     # Osama  # Removes all values From list
    for e in list.copy():
        if e == value:
            list.remove(value)

    return list

def clear_screen():             # Clearing Console using os library
    import os
    os.system('cls')


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

def check_found(title):
    books = get_books()

    for i in range(len(books)):
        if books[i][0].lower() == title:
            return True
    
    return False


