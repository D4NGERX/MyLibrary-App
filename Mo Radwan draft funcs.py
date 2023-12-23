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