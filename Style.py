from Config import *

def cell_format(string, number_of_tabs):  # Generating Cell Shape
    spaces = 8 * number_of_tabs - len(string) - 2
    return " " + string + " " * spaces


def formatting(book):  # generating line to be printed in a table shape
    cells = {}
    cells["Title"] = cell_format(book[TITLE].title(), WIDTHS["Title"])
    cells["Pages"] = cell_format(book[PAGES], WIDTHS["Pages"])
    cells["Per"] = cell_format(book[PERCENT], WIDTHS["Per"])
    cells["Date"] = cell_format(book[DATE], WIDTHS["Date"])
    cells["Status"] = cell_format(book[STATUS], WIDTHS["Status"])
    cells["Author"] = cell_format(book[AUTHOR].title(), WIDTHS["Author"])

    result = "\n|"
    for i in range(len(PARAMETERS)):
        result += cells[PARAMETERS[i]] + "|"

    return result


def clear_screen():  # Clearing Console using os library
    import os

    os.system("cls")


table_header = [SEPARATING_LINE, "|", "|", "|", SEPARATING_LINE]

for parameter in PARAMETERS:
    table_header[1] += f'{cell_format("", WIDTHS[parameter])}|'
    table_header[2] += f'{cell_format(parameter, WIDTHS[parameter])}|'
    table_header[3] += f'{cell_format("", WIDTHS[parameter])}|'


TABLE_HEADER = "\n".join(table_header)


