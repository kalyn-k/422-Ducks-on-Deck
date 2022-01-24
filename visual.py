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
import buildQueue
# from fileReader import *
# from fileWriter import *

# Index of current student in the deck, from 0 to 3
global current_student

global deck_names
deck_names = [] # TODO fix this -- need to make an initial list

current_student = 0


def UserImport():
    # call on file reader
    pass


def UserExportDaily():
    # call on file writer to export daily log
    pass


def UserExportTerm():
    # call on file writer to export term log
    pass


def DailyFlags():
    # Access a file of the daily flags
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
    # removed = class_roster.dequeue()
    student_name = deck_names[current_student]
    buildQueue.remove(student_name, True)


def LowerKeystroke(event):
    # Remove student from deck
    global deck_names
    if current_student != 3:
        deck_names[current_student] = deck_names[current_student + 1]
    student_name = deck_names[current_student]
    buildQueue.remove(student_name, False)
    pass


def UpdateDeck():
    global deck_names
    global class_roster

    # class_roster = queue

    for name in range(4):
        pass
        # build queue needs a "get name" function
        # current_name = class_roster.get_name(name)
        # deck_names[name] = current_name


def exit_():
    sys.exit()


#display_win = Tk(className=" Ducks on Deck ")


def DeckDisplay():
    # Initial design - Creates a Window
    # display_win = Tk(className=" Ducks on Deck ")
    # Sets window size
    display_win = Toplevel(height=105, width=750)
    #display_win.geometry("700x105")
    #display_win.attributes("-topmost", 1)
    display_win.title(" Ducks on Deck ")
    display_win.resizable(False, False)
    display_win.attributes('-topmost', 'true')
    #display_win.mainloop()

    # Create four names here
    # Names come from file reader?

    # Detects keystrokes
    display_win.bind('<Left>', LeftKeystroke)
    display_win.bind('<Right>', RightKeystroke)
    display_win.bind('<Up>', UpperKeystroke)
    display_win.bind('<Down>', LowerKeystroke)


def MenuDisplay():
    # Initial design - Creates a Window

    # Create a window for the main menu
    menu_win = Tk(className=" Ducks on Deck: Menu ")
    # Sets window size
    menu_win.geometry("220x300")
    # Prevent the menu window from being resized
    menu_win.resizable(False, False)
    #menu_win.attributes("-topmost", 2)

    # Create menu buttons here
    export_daily_button = Button(menu_win, text="Export Daily Data", font=("MS Sans Serif", 20),
                                 command=UserExportDaily)
    export_daily_button.place(x=30, y=30)
    export_total_button = Button(menu_win, text="Export Total Data", font=("MS Sans Serif", 20),
                                 command=UserExportTerm)
    export_total_button.place(x=30, y=75)
    # Daily Flags Button
    daily_flags_button = Button(menu_win, text="     Daily Flags      ", font=("MS Sans Serif", 20), command=DailyFlags)
    daily_flags_button.place(x=30, y=120)
    import_button = Button(menu_win, text="   Import Roster   ", font=("MS Sans Serif", 20), command=UserImport)
    import_button.place(x=30, y=160)
    # Button to exit session
    exit_button = Button(menu_win, text="            Exit           ", font=("MS Sans Serif", 20), command=exit_)
    exit_button.place(x=30, y=200)
    # Button to create a new session
    session_button = Button(menu_win, text="    New Session   ", font=("MS Sans Serif", 20), command=DeckDisplay)
    session_button.place(x=30, y=240)
    menu_win.mainloop()


class_roster = None
student_names = []

if __name__ == "__main__":
    MenuDisplay()
    DeckDisplay()
