from Minor_Functions import *

def main_menu():
    """Main Menu of the program"""

    print("-----------------------------------------------")
    print("1) Add New book")                                 # Done
    print("2) Remove book")                                  # Done
    print("3) I read some pages")                            # Done
    print("4) Get book details")                             # Done
    print("5) Show my Library")                              # Done
    print("6) Sort my library")                              # Under Dev
    print("7) Mark page")                                    # Done
    print("8) Find books by [Title, Date, Status, Author]")  # Done
    print("9) Modify book details")                          # Done
    print("10) Show my marks")                               # Done
    print("11) Show my ratings")                             # Done
    print("-----------------------------------------------")
    print("#) Settings")                                   # Under Dev
    print("0) Exit")                                         # Done
    print("00) Clear Screen")                                # Done
    print("-----------------------------------------------")


def check(choice):  # Checking User Choice
    output_file = open(OUTPUT_PATH, "w").close()  # Making Sure That output file is opened and clean
    
    if choice == "1":
        add_new_book()

    elif choice == "2":
        book_title = input("Book Title: ").title()
        remove_book(book_title)

    elif choice == "3":
        choose = choose_book()
        read(choose)
        calc_percentage(choose)

    elif choice == "4":
        title = input("Enter book Title: ").title()
        find_books_by("Title", title)

    elif choice == "5":
        show_library()

    elif choice == '6':
        Function_Parameters = {
            "Title" : TITLE,
            "Pages" : PAGES,
            "Progress" : PERCENT,
            "Start Date" : DATE,
            "Status" : STATUS,
            "Author" : AUTHOR,
            "Added Recently" : "Added Recently"
            }

        Parameter = input("sort by [Title, Pages, Progress, Start Date, Status, Author, Added Recently]: ").title()
        while Parameter not in Function_Parameters.keys():
            print("Please choose a valid choice.")
            Parameter = input("sort by [Title, Pages, Progress, Start Date, Status, Author, Added Recently]: ").title()
        
        if Parameter == "Added Recently":
            library = get_books_from(DEFAULT_PATH)
            update_database(library)
            
        
        elif Parameter in Function_Parameters.keys():
            Sort_Type = {"Ascending" : False, "A" : False, "Descending" : True, "D" : True}

            Type = input("Ascending [A] or Descending [D]? ").title()
            while Type not in Sort_Type.keys():
                print("Please choose a valid choice.")
                Type = input("Ascending [A] or Descending [D]? ").title()


            library = sort_library_by(Function_Parameters[Parameter], Sort_Type[Type])
            update_database(library)

    
    elif choice == '7':
        mark_page()

    elif choice == "8":
        parameter = input("Choose parameter[Date, Status, Author]: ").title()
        while parameter not in PARAMETERS:  # input correction
            print("Please, Enter a valid choice !")
            parameter = input("Choose parameter[Date, Status, Author]: ").title()

        value = input("Enter value: ").title()
        find_books_by(parameter, value)

    elif choice == "9":
        title = input("Enter book title: ").title()
        while not check_found(title):
            print("Book not found !")
            title = input("Enter book title: ").title()

        parameter = input(f"Enter parameter to change [Title, Author, Date, Pages]: ").title()
        while parameter.title() not in PARAMETERS:
            print("Enter a valid choice!")
            parameter = input("Enter parameter to change: ").title()
        modification = input("Enter new value: ")
        modify(title, parameter, modification)

    elif choice == "10":
        file = advanced_open(MARKS_PATH, 'r')
        output(file.read())
        file.close()
    
    elif choice == "11":
        file = advanced_open(RATINGS_PATH, 'r')
        output(file.read())
        file.close()



    elif choice == "#":  # Settings
        print("Change Database Path")
        print("Change Output Path")
        print("Change Marks Path")

    elif choice == "0":  # exiting program using exit() function
        print("Bye !")
        exit()

    elif choice == "00":
        clear_screen()
        print("-----------------------------------------------")
        print("-----------------Library App-------------------", end="")

    else:
        print("Enter a valid choice \n")


def add_new_book():
    """Adding new book to the library"""

    while True:  # Making sure that book doesn't exist
        title = input("Book title: ").title()
        if not check_found(title):
            break
        print("Book already exists !")

    Total_pages = input("Number of pages: ")
    author = input("Author name: ").title()
    start_date = get_correct_date_format("Start Date: ", "Please, Enter a valid date")
    while True:
        try:
            status = input("What is the status of the book ?[reading - wishlist - finished]: ").title()
            if status in ["Reading", "Wishlist", "Finished"]:
                break
        except:
            print("Please, Enter a valid choice !")

    read_pages = 0
    if status == "Finished":
        read_pages = Total_pages
    elif status == "Reading":
        read_pages = integer_only("Number of read pages: ", "Please, Enter the number of pages:")

    database_a = open(DATABASE_PATH, "a")
    book = {}
    book[ID] = f'{len(get_books_from(DATABASE_PATH)) + 1 + 1}'    # Adding 1 to the length of the library to get cuurent count of books and 1 to get the next ID
    book[TITLE] = title
    book[PAGES] = f"{read_pages}/{Total_pages}"
    book[DATE] = start_date
    book[STATUS] = status
    book[AUTHOR] = author
    book[PERCENT] = '0'
    book = [book[i] for i in range(len(PARAMETERS))] # Converting book from dictionary to list
    database_a.write(formatting(book))
    database_a.write("\n" + SEPARATING_LINE)
    database_a.close()

    calc_percentage(len(get_books_from(DATABASE_PATH)))


def remove_book(book_title):
    """Removing book from the library by title

    Args:
        book_title (string): title of the book to be removed
    """
    library = get_books_from(DATABASE_PATH)
    found = False
    for book in library:
        if book[TITLE].title() == book_title:
            found = True
            library.remove(book)
    if found:
        update_database(library)
        print("Removed !")
    else:
        print("Not Found !")


def show_library():
    """Showing all books in the library"""

    update_database(get_books_from(DATABASE_PATH))
    
    database = advanced_open(DATABASE_PATH, "r")
    
    lines = database.readlines()

    for line in lines:
        output(line)


def find_books_by(parameter, value):
    """Finding books by any parameter

    Args:
        parameter (string): parameter to search by
        value (string): value of the parameter
    """
    library = get_books_from(DATABASE_PATH)

    results = []  # Result books

    for book in library:  # Search book by book    

        if book[GUIDE[parameter]].title() == value:
            results.append(book)

    if results == []:  # Checking if results are found
        output("Not found")
    else:
        output(TABLE_HEADER)
        for result in results:
            output(formatting(result) + "\n")  # output Found books
            output(SEPARATING_LINE)


def modify(title, parameter, new_value):
    """Modifying any book details

    Args:
        title (string): title of the book to be modified
        parameter (string): parameter to be modified
        new_value (string): new value of the parameter
    """
    library = get_books_from(DATABASE_PATH)
    for i in range(len(library)):
        if library[i][TITLE].title() == title:
            if parameter == "Pages":
                library[i][GUIDE[parameter]] = f"{library[i][GUIDE[parameter]].split('/')[0]}/{new_value}"
                update_database(library)
                calc_percentage(i+1)
                break
            else:
                library[i][GUIDE[parameter]] = new_value
                break

    update_database(library)
    print("Modification Done !\n")


def read(choose):
    """Updating the number of read pages and status of the book

    Args:
        choose (int): order of the book in the library
    """
    library = get_books_from(DATABASE_PATH)
    readpages = integer_only(
        "Enter the number of pages you have read: ",
        "Please enter the number of pages as an integer only",
    )
    current_readpages = int(library[choose - 1][PAGES].split("/")[0])
    total_pages = library[choose - 1][PAGES].split("/")[1]
    library[choose - 1][PAGES] = f"{current_readpages+readpages}/{total_pages}"
    library[choose - 1][STATUS] = "Reading"
    calc_percentage(choose)

    update_database(library)


def mark_page():
    """Marking a page in a book and adding a comment"""

    database = open(MARKS_PATH, 'a')
    
    title = input("Enter Book Title:").title()
    while not check_found(title):               # Making sure that user enterd title of an existing book
        print("Book not found!")
        title = input("Enter Book Title:").title()

    
    order = get_book_order(title)

    page_to_mark = integer_only("Enter page to mark: ", "Please, Enter a valid page number!")
    while page_to_mark > int(get_books_from(DATABASE_PATH)[order][PAGES].split("/")[1]):   # Making sure that user entered valid page number
        print("Please, Enter a valid page number!")
        page_to_mark = integer_only("Enter page to mark: ", "Please, Enter a valid page number!")

    comment = input('Any comments ?\n')
    
    comment = divide_string(comment, 53)  # Dividing comment into segments to fit in the table

    database.write(f'\n|{cell_format(title, WIDTHS["Title"])}|{cell_format(f'{page_to_mark}', 2)}|{cell_format(comment[0], 7)}|')
    for i in range(1, len(comment)):
        database.write(f'\n|{cell_format("", WIDTHS["Title"])}|{cell_format("", 2)}|{cell_format(comment[i], 7)}|')
    database.write('\n+-------------------------------+---------------+-------------------------------------------------------+')

    database.close()
       

def sort_library_by(Parameter, Type):
    """Sorting the library by any parameter

    Args:
        Parameter (string): Parameter to sort by
        Type (string): Type of sorting [Ascending, Descending]

    Returns:
        list: sorted library
    """
    books = get_books_from(DATABASE_PATH)
    if Parameter == PAGES:
        sorted_books = sorted(books, key= sort_by_pages, reverse= Type)
    elif Parameter == PERCENT:
        sorted_books = sorted(books, key= sort_by_percentage, reverse= Type)
    elif Parameter == DATE:
        sorted_books = sorted(books, key= sort_by_date, reverse= Type)
    else:
        sorted_books = sorted(books, key= lambda book: book[Parameter], reverse= Type)
    return sorted_books
