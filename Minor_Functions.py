from Major_Functions import get_books

def output(string):         # Osama   # Printing Values in both terminal and output.txt file
    output_file = open(r'D:\PROJECTS\Library Project\output.txt', 'a')
    print(string, end='')
    output_file.write(string)
    output_file.close()

def check_found(title):
    books = get_books()

    for i in range(len(books)):
        if books[i][0].lower() == title:
            return True
    
    return False

def removeAll(list, value):     # Osama     # Removes all (value) from a list
    for e in list.copy():
        if e == value:
            list.remove(value)

    return list

