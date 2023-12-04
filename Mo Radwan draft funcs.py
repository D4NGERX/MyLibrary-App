MyLibrary = []

def choose_book           (library):
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

def date_format           (instructions, Error_Massage):
    while True:
        try:
            date = input(instructions)
            if date[2] != "/" or date[5] != "/" or len(date) != 10:
                print(Error_Massage)
            elif date[2] == "/" and date[5] == "/" and len(date) == 10:
                break
        except:
            print(Error_Massage)
    return date

def add                   (Library):
    
    book_name  = input("Book Name: ")
    book_pages = integer_only("Number of pages: ", "Please enter the number of pages as an integer only")
    date       = date_format("Date: ", "Please enter the date in DD/MM/YYYY format only")
    status     = input("book status: ")
    author     = input("Author of the book: ")
   
    book_details = {
        "book name"  : book_name,
        "book pages" : f"0 / {book_pages}",
        "percentage" : "0%",
        "date"       : date,
        "status"     : status,
        "rating"     : "not rated",
        "author"     : author
    }
    Library.append(book_details)

def read                  (library):

    choose                            = choose_book(library)
    readpages                         = integer_only("Enter the number of pages you have read: ", "Please enter the number of pages as an integer only")
    library[choose - 1]["book pages"] = f"{readpages} / {library[choose - 1]['book pages'].split(' / ')[1]}"
    percentage(MyLibrary, choose)

def percentage            (library, choose):
     library[choose - 1]["percentage"] = f"{int((int(library[choose - 1]['book pages'].split(' / ')[0]) / int(library[choose - 1]['book pages'].split(' / ')[1])) * 100)}%"
     full_percentage(library, choose)

def full_percentage       (library, choose):
    if library[choose - 1]["book pages"].split(" / ")[0] == library[choose - 1]["book pages"].split(" / ")[1]:
        print("Congratiolatins!! You have finished the book")
        library[choose - 1]["status"] = "finished"
        rating_after_finishing(library,choose)

def rating_after_finishing(library, choose):
    while True:
            try:
                rating = integer_only("rate the book: ", "Please enter the rating as an integer from 1 to 10 only")
                if rating > 10 or rating < 0:
                    print("Please enter the rating as an integer from 1 to 10 only")
                elif rating <= 10 and rating >= 0:
                    break
            except:
                print("Please enter the rating as an integer from 1 to 10 only")
    library[choose - 1]["rating"] = f"{rating} / 10"

def remove                (library):
    choose = choose_book(library)
    library.remove(library[choose - 1])

def remove_by_search(library):
    book_name = input("Book Name: ")
    for book in library:
        if book["book name"] == book_name:
            library.remove(book)
            return library
    return library

def edit                  (library):
    choose = choose_book(library)
    print("What do you want to edit?")
    print("1. Book name")
    print("2. Book pages")
    print("3. Date")
    print("4. Status")
    print("5. Author")
    while True:
            try:
               edit = integer_only("Enter: ", "INVALID! Integers only")
               if 0 < edit <= 5 :
                   break
            except:
                print("OUT OF RANGE! Choose one of the above options") 
    
    if   edit == 1:
        library[choose - 1]["book name"]  = input("Enter the updated book name: ")
    elif edit == 2:
        library[choose - 1]["book pages"] = input("Enter the updated book pages: ")
    elif edit == 3:
        library[choose - 1]["date"]       = input("Enter the updated date: ")
    elif edit == 4:
        library[choose - 1]["status"]     = input("Enter the updated status: ")
    elif edit == 5:
        library[choose - 1]["author"]     = input("Enter the updated author: ")

def sort_book(library, key):    # Library    title
    keys_value = []
    for i in library:
        keys_value.append(i[key])     # i['title']
        keys_value = sorted(keys_value)
    sorted_values = []
    for x in keys_value:
        for y in library:
            if x == y[key]:
                sorted_values.append(y)
    library.clear()
    library.append(sorted_values)

# add   (MyLibrary)
# print (MyLibrary)
# read  (MyLibrary)
# print (MyLibrary)
# remove(MyLibrary)
# print (MyLibrary)