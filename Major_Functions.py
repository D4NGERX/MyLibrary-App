from Config import *
from Style import *
from Minor_Functions import *


def main_menu():  # Printing Main Menu
    print("-----------------------------------------------")
    print("1) Add New book")  # Done
    print("2) Remove book")  # Done
    print("3) I read some pages")  # Done
    print("4) Get book details")  # Done
    print("5) Show my Library")  # Done
    print("6) Sort my library")  # Under Dev
    print("7) Mark page")  # Under Dev
    print("8) Find books by [Title, Date, Status, Author]")  # Done
    print("9) Modify book details")  # Done
    print("0) Exit")  # Done
    print("00) Clear Screen")  # Done
    print("-----------------------------------------------")


def check(choice):  # Checking User Choice
    output_file = open(OUTPUT_PATH, "w")  # Making Sure That output file is opened and clean
    
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
        show_books_by("title", title)

    elif choice == "5":
        show_library()

    # elif choice == '6':
    #     sort_library()
    # elif choice == '7':
    #     mark_page()

    elif choice == "8":
        parameter = input("Choose parameter[Date, Status, Author]: ").title()
        while parameter not in PARAMETERS:  # input correction
            print("Please, Enter a valid choice !")
            parameter = input("Choose parameter[Date, Status, Author]: ").title()

        value = input("Enter value: ").title()
        show_books_by(parameter, value)

    elif choice == "9":
        title = input("Enter book title: ").title()
        while not check_found(title):
            print("Book not found !")
            title = input("Enter book title: ").title()

        parameter = input(F"Enter parameter to change {PARAMETERS}: ").title()
        while parameter.title() not in PARAMETERS:
            print("Enter a valid choice!")
            parameter = input("Enter parameter to change: ").title()
        modification = input("Enter new value: ")
        modify(title, parameter, modification)

    elif choice == "0":  # exiting program using exit() function
        print("Bye !")
        exit()

    elif choice == "00":
        clear_screen()
        print("-----------------------------------------------")
        print("-----------------Library App-------------------", end="")

    else:
        print("Enter a valid choice \n")


def add_new_book():  # Adding book to Library
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

    calc_percentage(len(get_books()))


def remove_book(book_title):  # Rmoving book by entering its title
    library = get_books()
    found = False
    for book in library:
        if book[0].title() == book_title:
            found = True
            library.remove(book)
    if found:
        update_database(library)
        print("Removed !")
    else:
        print("Not Found !")


def show_library():  # Showing th Whole Library
    update_database(get_books())
    database = open(DATABASE_PATH, "r")
    lines = database.readlines()

    for line in lines:
        output(line)


def show_books_by(parameter, value):  # Find books with parameter value
    library = get_books() 

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


def modify(title, parameter, new_value):  # Modify any value by book title
    library = get_books()
    for i in range(len(library)):
        if library[i][0].title() == title:
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


def read(choose):  # Updating count of read pages and percentage after reading some pages
    library = get_books()
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
