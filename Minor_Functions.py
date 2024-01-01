from Config import *
from Style import *



def get_books():
    """Get books' details list from database.txt file

    Returns:
        list: list of books' details
    """
    books_details = []
    database = open(DATABASE_PATH, "r")  # Opening input file
    lines = database.readlines()
    for line in lines:
        line = [element.strip('\t \n') for element in line.split("|")]    # Clearing line
        line = removeAll(line, "")

        if len(line) > 1:
            books_details.append(line)

    database.close()
    books_details = reorder_books(books_details[1:])    # Reorder books according to global parameters & remove table header
    return books_details


def output(string):
    """Printing Values in both terminal and output.txt file

    Args:
        string (string): string to be printed
    """
    output_file = open(OUTPUT_PATH, "a")
    print(string, end="")
    output_file.write(string)
    output_file.close()


def check_found(title):
    """Check if book is in database or not

    Args:
        title (string): book title

    Returns:
        bool: True if book is in database, False otherwise
    """
    books = get_books()

    for i in range(len(books)):
        if books[i][0].title() == title:
            return True

    return False


def removeAll(list, value):
    """Remove all occurences of value from list

    Args:
        list (list): list to be modified
        value (any): value to be removed

    Returns:
        list: list after removing all occurences of value
    """
    for e in list.copy():
        if e == value:
            list.remove(value)

    return list


def update_database(library):
    """Update Database after any modification

    Args:
        library (list): list of books after any modification
    """
    database = open(DATABASE_PATH, "w")  # Clearing Database
    database.write(TABLE_HEADER)  # Appending table Header
    database.close()
    database = open(DATABASE_PATH, "a")

    for (book) in library:  # Formatting lines to be printed in terminal and output.txt file
        database.write(formatting(book))
        database.write("\n" + SEPARATING_LINE)  # Printing Separating Line

    database.close()


def integer_only(instructions, Error_Massage): 
    """Making sure that user entered an integer value

    Args:
        instructions (string): Message to enter integer
        Error_Massage (string): Meassage when invalid integer detected

    Returns:
        int: Correct integer
    """
    while True:
        try:
            variable = int(input(instructions))
            break
        except:
            print(Error_Massage)
    return variable


def calc_percentage(choose):
    """Calculate percentage of book read

    Args:
        choose (int): book index
    """
    library = get_books()
    read_pages = int(library[choose - 1][PAGES].split("/")[0])
    total_pages = int(library[choose - 1][PAGES].split("/")[1])

    library[choose - 1][PERCENT] = f"{int((read_pages / total_pages) * 100)}%"  # Update Percentage

    update_database(library)

    full_percentage(library, choose)


def full_percentage(library, choose):
    """Check if book is finished or not

    Args:
        library (list): list of books
        choose (int): book index
    """
    read_pages = int(library[choose - 1][PAGES].split("/")[0])
    total_pages = int(library[choose - 1][PAGES].split("/")[1])

    if read_pages == total_pages:  # If book is finished
        print("Congratiolatins!! You have finished the book")
        library[choose - 1][STATUS] = "Finished"
        # rating_after_finishing(library,choose)

    update_database(library)


def choose_book():  
    """Choose book from library after showing all books

    Returns:
        int: book index
    """
    library = get_books()
    books_list = []
    for book in library:  # Getting books list
        books_list.append(book[TITLE])

    for book in range(len(books_list)):
        print(f"{book + 1}. {books_list[book]}")
    while True:  # Asking user to shoose and amking sure that he entered integer value
        try:
            choose = integer_only("Choose book: ", "INVALID! Integers only")
            if 0 < choose <= len(books_list):
                break
        except:
            print("OUT OF RANGE! Choose one of the above options")
    return choose


def get_correct_date_format(instructions, Error_Massage):  # Making sure that user entered a valid date
    """Making sure that user entered a valid date

    Args:
        instructions (string): Message to enter date
        Error_Massage (string): Meassage when invalid date detected

    Returns:
        string: Correct Date
    """
    while True:
        date = input(instructions)
        chunks = date.split("/")
        if len(chunks) != 3:
            print(Error_Massage)
        else:
            DD, MM, YYYY = [
                int(chunk) for chunk in chunks
            ]  # Separating chunks of date and convert it to integer values
            if DD > 31 or MM > 12 or YYYY < 1000:
                print(Error_Massage)

            else:
                break

    return date


def reorder_books(library):
    """Reorder books according to global parameters

    Args:
        library (list): list of books

    Returns:
        list: list of books after reordering
    """
    database = open(DATABASE_PATH, "r")
    lines = database.readlines()

    # Getting old order of parameters
    old_order = lines[2].split("|")
    old_order = [element.strip('\t \n') for element in old_order]  # Getting old order of parameters
    removeAll(old_order, "")
    
    # Reorder box according to new order
    new_indicies = [old_order.index(element) for element in PARAMETERS]   # Getting new order of parameters
    ordered_library = []

    for book in library:
        ordered_library.append([book[i] for i in (new_indicies)])

    return ordered_library
