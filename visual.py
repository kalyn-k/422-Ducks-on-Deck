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


def UserImport():
    pass


def UserExportDaily():
    pass


def UserExportTerm():
    pass


def LeftKeystroke():
    # Decrement current student?
    pass


def RightKeystroke():
    # Increment current student?
    pass


def UpperKeystroke():
    # Flag
    global class_roster
    # removed = class_roster.dequeue()


def LowerKeystroke():
    # Remove student from deck 
    pass


def UpdateDeck():
    pass


def DeckDisplay():
    # Initial design - Creates a Window
    display_win = Tk(className=" Ducks on Deck ")
    # Sets window size
    display_win.geometry("700x105")
    display_win.attributes("-topmost", 1)
    display_win.resizable(False, False)
    display_win.mainloop()

    # Create four names here
    # Names come from file reader?


def MenuDisplay():
    # Initial design - Creates a Window

    # Create a window for the main menu
    menu_win = Tk(className=" Ducks on Deck: Menu ")
    # Sets window size
    menu_win.geometry("220x300")
    # Prevent the menu window from being resized
    menu_win.resizable(False, False)
    menu_win.attributes("-topmost", 1)

    # Create menu buttons here
    export_daily_button = Button(menu_win, text="Export Daily Data", font=("MS Sans Serif", 20), command=UserExportDaily())
    export_daily_button.place(x=30, y=30)
    export_total_button = Button(menu_win, text="Export Total Data", font=("MS Sans Serif", 20), command=UserExportTerm())
    export_total_button.place(x=30, y=75)
    daily_flags_button = Button(menu_win, text="     Daily Flags      ", font=("MS Sans Serif", 20))
    daily_flags_button.place(x=30, y=120)
    import_button = Button(menu_win, text="   Import Roster   ", font=("MS Sans Serif", 20),command=UserImport())
    import_button.place(x=30, y=160)
    exit_button = Button(menu_win, text="            Exit           ", font=("MS Sans Serif", 20))
    exit_button.place(x=30, y=200)
    session_button = Button(menu_win, text="    New Session   ", font=("MS Sans Serif", 20))
    session_button.place(x=30, y=200)
    menu_win.mainloop()


class_roster = None
student_names = []

if __name__ == "__main__":
    DeckDisplay()
    MenuDisplay()

