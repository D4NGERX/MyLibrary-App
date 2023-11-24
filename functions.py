# database = open(r'D:\PROJECTS\Library Project\database.txt', 'r')
# output_file = open(r'D:\PROJECTS\Library Project\output.txt', 'w')
# input_file = open(r'D:\PROJECTS\Library Project\input.txt', 'r')


def check(choice):          # Osama
    output_file = open(r'D:\PROJECTS\Library Project\output.txt', 'w')
    if choice == '1':
        add_new_book()
    # elif choice == '2':
    #     remove_book()
    # elif choice == '3':
    #     read_pages()
    # elif choice == '4':
    #     get_book_details()
    elif choice == '5':
        show_library()
    # elif choice == '6':
    #     sort_library()
    # elif choice == '7':
    #     mark_page()
    elif choice == '8':
        parameter = input('Choose parameter[Title, Date, Status, Author]: ').lower()
        while parameter not in ['title', 'date', 'status', 'author']:       # input correction
            print('Please, Enter a valid choice !')
            parameter = input('Choose parameter[Title, Date, Status, Author]: ').lower()

        
        value = input('Enter value: ').lower()
        show_books_by(parameter, value)
    # elif choice == '0':
    #     Exit()
    # elif choice == '00':
    #     clear_screen()
    else:
        print('Enter a valid choice \n')

def output(string):         # Osama
    output_file = open(r'D:\PROJECTS\Library Project\output.txt', 'a')
    print(string, end='')
    output_file.write(string)
    output_file.close()

def add_new_book():         # Osama
    title = input('Book title: ')
    Total_pages = input('Number of pages: ')
    author = input('Author name: ')
    start_date = input('Start Date: ')
    status = input('What is the status of the book ?[reading - wishlist - finished]: ')

    database_a = open(r'D:\PROJECTS\Library Project\database.txt', 'a')
    database_a.write(formatting(title, Total_pages, start_date, author, status))
    database_a.write('\n+-----------------------+---------------+-------+---------------+---------------+-----------------------+')
    database_a.close()

def show_library():         # Osama
    database = open(r'D:\PROJECTS\Library Project\database.txt', 'r')
    lines = database.readlines()

    for line in lines:
        output(line)

def formatting(title, totalPages, date, author, status, pages=0, percent=0):    # Osama
    title_cell = cell_format(title, 3)
    pages_cell = cell_format(f'{pages}/{totalPages}', 2)
    percent_cell = cell_format(f'{percent}%', 1)
    date_cell = cell_format(date, 2)
    status_cell = cell_format(status, 2)
    author_cell = cell_format(author, 3)

    result = f'\n| {title_cell}| {pages_cell}| {percent_cell}| {date_cell}| {status_cell}| {author_cell}|'
    return result

def cell_format(string, number_of_tabs):    # Osama
    if len(string) < 6:
        string += '\t'*(number_of_tabs)
    elif len(string) < 14:
        string += '\t' * (number_of_tabs-1)
    elif len(string) < 21 and number_of_tabs > 2:
        string += '\t' * (number_of_tabs-2)
    else:
        string += ' '

    return string

def show_books_by(parameter, value):    # Osama
    database = open(r'D:\PROJECTS\Library Project\database.txt', 'r') # Opening input file
    lines = database.readlines()

    guide = {    # Translating parameter into number
        'title' : 0,
        'date' : 3,
        'status' : 4,
        'author' : 5
    }
    results = []       # Result books

    for line in lines:        # Search book by book
        whole_line = line

        line = line.replace('\t', '').split('|')      # Clearing line
        line = removeAll(line, '')             #

        for i in range(len(line)):
            line[i] = line[i].replace(' ', '', 1)              # Clearing each string from prefix space

        if len(line) > 1 and line[guide[parameter]].lower() == value:
            results.append(whole_line)    
     

    if results == []:             # Checking if results are found
        output('Not found')
    else:
        for result in results:
            output(result)        # output Found books
    
    database.close()

def removeAll(list, value):     # Osama  # Removes all values From list
    for e in list.copy():
        if e == value:
            list.remove(value)

    return list