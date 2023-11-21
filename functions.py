database = open(r'D:\PROJECTS\Library Project\database.txt', 'r')
output_file = open(r'D:\PROJECTS\Library Project\output.txt', 'w')
input_file = open(r'D:\PROJECTS\Library Project\input.txt', 'r')


def check(choice):          # Osama
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
    # elif choice == '0':
    #     Exit()
    # elif choice == '00':
    #     clear_screen()
    else:
        print('Enter a valid choice \n')

def output(string):         # Osama
    print(string, end='')
    output_file.write(string)

def get_input(string):      # Osama
    output(string)
    # input_file.readline()
    return input()

def add_new_book():         # Osama
    title = get_input('Book title: ')
    Total_pages = get_input('Number of pages: ')
    author = get_input('Author name: ')
    start_date = get_input('Start Date: ')
    status = get_input('What is the status of the book ?[reading - wishlist - finished]: ')

    database_a = open(r'D:\PROJECTS\Library Project\database.txt', 'a')
    database_a.write(formatting(title, Total_pages, start_date, author, status))
    database_a.write('\n+-----------------------+---------------+-------+---------------+---------------+-----------------------+')
    database_a.close()

def show_library():         # Osama
    for line in database:
        output(line)
    output_file.close()

def formatting(title, totalPages, date, author, status, pages=0, percent=0):
    title_cell = cell_format(title, 3)
    pages_cell = cell_format(f'{pages}/{totalPages}', 2)
    percent_cell = cell_format(f'{percent}%', 1)
    date_cell = cell_format(date, 2)
    status_cell = cell_format(status, 2)
    author_cell = cell_format(author, 3)

    result = f'\n| {title_cell}| {pages_cell}| {percent_cell}| {date_cell}| {status_cell}| {author_cell}|'
    return result

def cell_format(string, number_of_tabs):
    if len(string) < 6:
        string += '\t'*(number_of_tabs)
    elif len(string) < 14:
        string += '\t' * (number_of_tabs-1)
    elif len(string) < 21 and number_of_tabs > 2:
        string += '\t' * (number_of_tabs-2)
    else:
        string += ' '

    return string
