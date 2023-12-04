from Config import *

def cell_format(string, number_of_tabs):    # Osama     # Generating Cell Shape
    if len(string) < 6:
        string += '\t'*(number_of_tabs)
    elif len(string) < 14:
        string += '\t' * (number_of_tabs-1)
    elif len(string) < 22 and number_of_tabs > 2:
        string += '\t' * (number_of_tabs-2)
    elif len(string) < 39 and number_of_tabs > 3:
        string += '\t' * (number_of_tabs-3)
    else:
        string += ' '

    return string

def formatting(title, totalPages, date, author, status, pages=0, percent=0):    # Osama     # generating line to be printed in a table shape
    title_cell = cell_format(title, TITLE_COL_WIDTH)
    pages_cell = cell_format(f'{pages}/{totalPages}', PAGES_COL_WIDTH)
    percent_cell = cell_format(f'{percent}%', PERCENT_COL_WIDTH)
    date_cell = cell_format(date, DATE_COL_WIDTH)
    status_cell = cell_format(status, STATUS_COL_WIDTH)
    author_cell = cell_format(author, AUTHOR_COL_WIDTH)

    result = f'\n| {title_cell}| {pages_cell}| {percent_cell}| {date_cell}| {status_cell}| {author_cell}|'
    return result

def clear_screen():                         # Osama     # Clearing Console using os library
    import os
    os.system('cls')


