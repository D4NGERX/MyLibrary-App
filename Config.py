# Files Locations
DATABASE_PATH = r'D:\PROJECTS\Library Project\database.txt'
OUTPUT_PATH = r'D:\PROJECTS\Library Project\output.txt'

# Global Variables
TITLE_COL_WIDTH = 4
PAGES_COL_WIDTH = 2
PERCENT_COL_WIDTH = 1
DATE_COL_WIDTH = 2
STATUS_COL_WIDTH = 2
AUTHOR_COL_WIDTH = 3

SEPARATING_LINE = '+-------------------------------+---------------+-------+---------------+---------------+-----------------------+'


TABLE_HEADER = f'''{SEPARATING_LINE}
|				|		|	|		|		|			|
| Title				| Pages		| per	| Date		| Status	| Author		|
|				|		|	|		|		|			|
{SEPARATING_LINE}'''


PARAMETERS = ['title', 'pages', 'percent', 'date', 'status', 'author']

GUIDE = {    # Translating parameter into number
    'title' : 0,
    'pages' : 1,
    'percent': 2,
    'date' : 3,
    'status' : 4,
    'author' : 5
}





