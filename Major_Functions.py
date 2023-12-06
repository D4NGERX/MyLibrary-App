from Config import *
from Style  import *
from Minor_Functions import *

def main_menu():                                   # Osama     # Printing Main Menu
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

def check(choice):                                 # Osama     # Checking User Choice
    output_file = open(OUTPUT_PATH, 'w') # Making Sure That output file is opened and clean
    if choice == '1':
        add_new_book()
    
    elif choice == '2':
        book_title = input("Book Title: ").lower()
        remove_book(book_title)
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
        while parameter.lower() not in PARAMETERS:
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

def add_new_book():                                # Osama     # Adding book to Library
    title = input('Book title: ').capitalize()
    Total_pages = input('Number of pages: ')
    author = input('Author name: ').capitalize()
    start_date = input('Start Date: ')
    status = input('What is the status of the book ?[reading - wishlist - finished]: ').capitalize()

    database_a = open(DATABASE_PATH, 'a')
    database_a.write(formatting(title, Total_pages, start_date, author, status))
    database_a.write('\n' + SEPARATING_LINE)
    database_a.close()

def remove_book(book_title):                       # Mohamed   # Rmoving book by entering its title
    library = get_books()
    found = False
    for book in library:
        if book[0].lower() == book_title:
            found = True
            library.remove(book)
    if found:
        update_database(library)
        print('Removed !')
    else:
        print('Not Found !')

def show_library():                                # Osama     # Showing th Whole Library
    database = open(DATABASE_PATH, 'r')
    lines = database.readlines()

    for line in lines:
        output(line)

def show_books_by(parameter, value):               # Osama     # Find books with parameter value
    database = open(DATABASE_PATH, 'r') # Opening input file
    lines = database.readlines()

    
    
    results = []       # Result books

    for line in lines:        # Search book by book
        whole_line = line

        line = line.replace('\t', '').split('|')      # Clearing line
        line = removeAll(line, '')                    #

        for i in range(len(line)):
            line[i] = line[i].replace(' ', '', 1)              # Clearing each string from prefix space

        if len(line) > 1 and line[GUIDE[parameter]].lower() == value:
            results.append(whole_line)
     
    
    if results == []:             # Checking if results are found
        output('Not found')
    else:
        output(TABLE_HEADER)
        for result in results:
            output('\n'+result)        # output Found books
            output(SEPARATING_LINE)
    
    database.close()

def modify(title, parameter, new_value):
    library = get_books()
    for i in range(len(library)):
        if library[i][0].lower() == title:
            library[i][GUIDE[parameter]] = new_value
            break
    
    update_database(library)
    print('Modification Done !\n')
    
  


