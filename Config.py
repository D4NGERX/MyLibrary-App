# Files Paths
DATABASE_PATH = "database.txt"
OUTPUT_PATH = "output.txt"
MARKS_PATH = "Marked Pages.txt"
RATINGS_PATH = "ratings.txt"

# Global Variables
PARAMETERS = ["", "Title", "Pages", "Per", "Date", "Status", "Author"]   # Note: Order of parameters is the order of columns in database

WIDTHS = {
    "": 1,
    "Title": 4,
    "Pages": 2,
    "Per": 1,
    "Date": 2,
    "Status": 2,
    "Author": 3
}

def generateLine():
    BAR = "-------"
    return (
        f"+{BAR*WIDTHS[PARAMETERS[1]] + "-"*(WIDTHS[PARAMETERS[1]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[2]] + "-"*(WIDTHS[PARAMETERS[2]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[3]] + "-"*(WIDTHS[PARAMETERS[3]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[4]] + "-"*(WIDTHS[PARAMETERS[4]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[5]] + "-"*(WIDTHS[PARAMETERS[5]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[6]] + "-"*(WIDTHS[PARAMETERS[6]]-1)}+"
    )


SEPARATING_LINE = generateLine()

GUIDE = dict(zip(PARAMETERS, range(len(PARAMETERS))))

TITLE = GUIDE["Title"]
PAGES = GUIDE["Pages"]
PERCENT = GUIDE["Per"]
DATE = GUIDE["Date"]
STATUS = GUIDE["Status"]
AUTHOR = GUIDE["Author"]
