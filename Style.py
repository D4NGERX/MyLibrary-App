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
    title_cell = cell_format(title, title_col_width)
    pages_cell = cell_format(f'{pages}/{totalPages}', pages_col_width)
    percent_cell = cell_format(f'{percent}%', percent_col_width)
    date_cell = cell_format(date, date_col_width)
    status_cell = cell_format(status, status_col_width)
    author_cell = cell_format(author, author_col_width)

    result = f'\n| {title_cell}| {pages_cell}| {percent_cell}| {date_cell}| {status_cell}| {author_cell}|'
    return result

def clear_screen():                         # Osama     # Clearing Console using os library
    import os
    os.system('cls')


