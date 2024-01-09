# Files Paths
DATABASE_PATH = "database.txt"
OUTPUT_PATH = "output.txt"
DEFAULT_PATH = "default.txt"

# Global Variables
PARAMETERS = ["Title", "Pages", "Per", "Date", "Status", "Author"]

WIDTHS = {
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
        f"+{BAR*WIDTHS[PARAMETERS[0]] + "-"*(WIDTHS[PARAMETERS[0]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[1]] + "-"*(WIDTHS[PARAMETERS[1]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[2]] + "-"*(WIDTHS[PARAMETERS[2]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[3]] + "-"*(WIDTHS[PARAMETERS[3]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[4]] + "-"*(WIDTHS[PARAMETERS[4]]-1)}"
        f"+{BAR*WIDTHS[PARAMETERS[5]] + "-"*(WIDTHS[PARAMETERS[5]]-1)}+"
    )

def justify(string, width):
    return string + " "*(width-len(string))


SEPARATING_LINE = generateLine()





GUIDE = dict(zip(PARAMETERS, range(len(PARAMETERS))))

# from Minor_Functions import get_books


# current_order = get_books()[0]


TITLE = GUIDE["Title"]
PAGES = GUIDE["Pages"]
PERCENT = GUIDE["Per"]
DATE = GUIDE["Date"]
STATUS = GUIDE["Status"]
AUTHOR = GUIDE["Author"]
