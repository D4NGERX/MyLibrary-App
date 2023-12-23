# Files Paths
DATABASE_PATH = 'database.txt'
OUTPUT_PATH = 'output.txt'

# Global Variables
TITLE_COL_WIDTH = 4
PAGES_COL_WIDTH = 2
PERCENT_COL_WIDTH = 1
DATE_COL_WIDTH = 2
STATUS_COL_WIDTH = 2
AUTHOR_COL_WIDTH = 3

def generateLine(title, pages, percent, date, status, author):
    BAR = '-------'
    return f'+{BAR*title + '-'*(title-1)}+{BAR*pages + '-'*(pages-1)}+{BAR*percent + '-'*(percent-1)}+{BAR*date + '-'*(date-1)}+{BAR*status + '-'*(status-1)}+{BAR*author + '-'*(author-1)}+'



SEPARATING_LINE = generateLine(TITLE_COL_WIDTH, PAGES_COL_WIDTH, PERCENT_COL_WIDTH, DATE_COL_WIDTH, STATUS_COL_WIDTH, AUTHOR_COL_WIDTH)


TABLE_HEADER = f'''{SEPARATING_LINE}
|{TITLE_COL_WIDTH * '\t'}|{PAGES_COL_WIDTH * '\t'}|{PERCENT_COL_WIDTH * '\t'}|{DATE_COL_WIDTH * '\t'}|{STATUS_COL_WIDTH * '\t'}|{AUTHOR_COL_WIDTH * '\t'}|
| Title{TITLE_COL_WIDTH * '\t'}| Pages{PAGES_COL_WIDTH * '\t'}| per{PERCENT_COL_WIDTH * '\t'}| Date{DATE_COL_WIDTH * '\t'}| Status{(STATUS_COL_WIDTH-1) * '\t'}| Author{(AUTHOR_COL_WIDTH-1) * '\t'}|
|{TITLE_COL_WIDTH * '\t'}|{PAGES_COL_WIDTH * '\t'}|{PERCENT_COL_WIDTH * '\t'}|{DATE_COL_WIDTH * '\t'}|{STATUS_COL_WIDTH * '\t'}|{AUTHOR_COL_WIDTH * '\t'}|
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

TITLE = GUIDE['title']
PAGES = GUIDE['pages']
PERCENT = GUIDE['percent']
DATE = GUIDE['date']
STATUS = GUIDE['status']
AUTHOR = GUIDE['author']



