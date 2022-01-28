"""
visual.py

Creation Date: Jan. 20, 2022
Last Updated: Jan. 20, 2022

Authors: Kalyn Koyanagi (kek), Liza Richards
TODO add purpose and function of file
Modifications:
Created file    kek     1/20/22
"""

# Import Statements
from tkinter import *
import sys
# from buildQueue import *
# import buildQueue

# from fileReader import *
from fileWriter import *

# Index of current student in the deck, from 0 to 3
global current_student

global deck_names
deck_names = []  # TODO fix this -- need to make an initial list

current_student = 0


# initial_queue = Queue()


def UserImport():
    # call on file reader
    pass


def UserExportDaily():
    # exportDailyLog()
    pass


def UserExportTerm():
    # exportSumPerf
    pass


def LeftKeystroke(event):
    global current_student
    if current_student == 0:
        current_student = 3
    else:
        current_student -= 1


def RightKeystroke(event):
    global current_student
    if current_student == 3:
        current_student = 0
    else:
        current_student += 1


def UpperKeystroke(event):
    # Flag and remove ?
    global class_roster
    global deck_names
    UpdateDeck()
    '''
    # removed = class_roster.dequeue()
    student_name = deck_names[current_student]
    buildQueue.remove(student_name, True)
'''

def LowerKeystroke(event):
    # Remove student from deck
    global deck_names
    if current_student != 3:
        deck_names[current_student] = deck_names[current_student + 1]
    student_name = deck_names[current_student]
    queue.remove(student_name, False)
    pass


def UpdateDeck():
    global deck_names
    global class_roster
    test_names[2] = "Justin Herbert"


    # class_roster = queue
"""
    for name in range(4):
        pass
        # build queue needs a "get name" function
        # current_name = class_roster.get_name(name)
        # deck_names[name] = current_name
    """


def exit_():
    sys.exit()


def DeckDisplay():
    # Initial design - Creates a Window
    # Sets window size
    display_win = Toplevel(height=105, width=750)
    display_win.title(" Ducks on Deck ")
    # Prevent the window from being resized
    display_win.resizable(False, False)
    # Make the display window the topmost window at all times
    display_win.attributes('-topmost', 'true')

    # Create four names here
    # Names come from file reader?

    return display_win


def MenuDisplay():
    # Initial design - Creates a Window

    # Create a window for the main menu
    menu_win = Tk(className=" Ducks on Deck: Menu ")
    # Sets window size
    menu_win.geometry("250x300")
    # Set background color
    menu_win.configure(bg='black')
    # Prevent the menu window from being resized
    menu_win.resizable(False, False)

    # Create menu buttons here
    export_daily_button = Button(menu_win, text="Export Daily Data", font=("MS Sans Serif", 20),
                                 command=UserExportDaily, bg="white", width=15)
    export_daily_button.place(x=28, y=20)
    export_total_button = Button(menu_win, text="Export Performance\n Summary", font=("MS Sans Serif", 20),
                                 command=UserExportTerm, bg="white", width=15)
    export_total_button.place(x=28, y=65)
    # Import class data
    import_button = Button(menu_win, text="Import Roster", font=("MS Sans Serif", 20), command=UserImport, bg="white",
                           width=15)
    import_button.place(x=28, y=135)
    # Button to exit session
    exit_button = Button(menu_win, text="            Exit           ", font=("MS Sans Serif", 20), command=exit_,
                         bg="white", width=15)
    exit_button.place(x=28, y=190)
    # Button to create a new session
    session_button = Button(menu_win, text="    New Session   ", font=("MS Sans Serif", 20), command=DeckDisplay,
                            bg="white", width=15)
    session_button.place(x=28, y=235)
    menu_win.mainloop()


class_roster = None
student_names = []
test_names = ["Kalyn Koyanagi", "Kelly Schombert", "Ellie Kobak", "Liza Richards", "Anthoy Hornof", "Justin Bieber"]
if __name__ == "__main__":
    MenuDisplay()
