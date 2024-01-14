# Files Paths
DATABASE_PATH = "database.txt"
OUTPUT_PATH = "output.txt"
MARKS_PATH = "Marked Pages.txt"
RATINGS_PATH = "ratings.txt"
SORTED_PATH = "sorted.txt"
SORT_MODE_PATH = "sort mode.txt"

# Global Variables
PARAMETERS = ["No.", "Title", "Status", "Date", "Pages", "Per", "Author"]   # Note: Order of parameters is the order of columns in database

WIDTHS = {
    "No.": 1,
    "Title": 4,
    "Pages": 2,
    "Per": 1,
    "Date": 2,
    "Status": 2,
    "Author": 4
}

def generateLine():
    BAR = "-------"
    return (
        f"+{BAR*WIDTHS[PARAMETERS[0]] + "-"*(WIDTHS[PARAMETERS[0]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[1]] + "-"*(WIDTHS[PARAMETERS[1]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[2]] + "-"*(WIDTHS[PARAMETERS[2]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[3]] + "-"*(WIDTHS[PARAMETERS[3]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[4]] + "-"*(WIDTHS[PARAMETERS[4]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[5]] + "-"*(WIDTHS[PARAMETERS[5]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[6]] + "-"*(WIDTHS[PARAMETERS[6]]-1)}+"
    )


SEPARATING_LINE = generateLine()

GUIDE = dict(zip(PARAMETERS, range(len(PARAMETERS))))

ID = GUIDE["No."]
TITLE = GUIDE["Title"]
PAGES = GUIDE["Pages"]
PERCENT = GUIDE["Per"]
DATE = GUIDE["Date"]
STATUS = GUIDE["Status"]
AUTHOR = GUIDE["Author"]


SORTING_PARAMETERS = {
    "Title" : TITLE,
    "Pages" : PAGES,
    "Progress" : PERCENT,
    "Start Date" : DATE,
    "Status" : STATUS,
    "Author" : AUTHOR,
    "Added Recently" : "Added Recently"
}

SORT_TYPE = {"Ascending" : False, "A" : False, "Descending" : True, "D" : True}