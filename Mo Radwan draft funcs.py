MyLibrary = []




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





def remove                (library):
    choose = choose_book(library)
    library.remove(library[choose - 1])
 

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