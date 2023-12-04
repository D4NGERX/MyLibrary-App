# Files Locations
database_path = r'D:\PROJECTS\Library Project\database.txt'

# Global Variables

table_header = '''+-------------------------------+---------------+-------+---------------+---------------+-----------------------+
|				|		|	|		|		|			|
| Title				| Pages		| per	| Date		| Status	| Author		|
|				|		|	|		|		|			|
+-------------------------------+---------------+-------+---------------+---------------+-----------------------+'''

separating_line = '+-------------------------------+---------------+-------+---------------+---------------+-----------------------+'

parameters = ['title', 'pages', 'percent', 'date', 'status', 'author']

guide = {    # Translating parameter into number
    'title' : 0,
    'pages' : 1,
    'percent': 2,
    'date' : 3,
    'status' : 4,
    'author' : 5
}

title_col_width = 4
pages_col_width = 2
percent_col_width = 1
date_col_width = 2
status_col_width = 2
author_col_width = 3



