"""
Name: DucksOnDeck.py
Purpose: Control the software user interface

Creation Date: Jan. 20, 2022
Last Updated: Jan. 30, 2022

Authors: Kalyn Koyanagi (kek), Liza Richards (ljr)
TODO add purpose and function of file
Modifications:
Created file                        kek     1/20/22
Added keystrokes                    kek     1/21/22
Updated keystrokes                  ljr     1/22/22
Finished menu and deck windows      kek     1/23/22
Updating deck user info complete    kek     1/25/22
Finished functionality              kek     1/28/22
Finished final modifications        kek     1/29/22
"""

# Import Statements
from tkinter import *     # used to create all user interface aspects
from buildQueue import *  # used to build/update a queue using student data
from fileWriter import *  # used to write to files with session data


class GraphicalUserInterface:
    """
    The purpose of this class is to display the user menu window and
    the student, as well as keep track of which students are on deck
    at any present moment.Receives student data from buildQueue, and writes student data using
    fileWriter.
    """

    def __init__(self):
        """
        Initializes the user display windows, the
        queue used for the deck, as well as the
        student names and indices that are used
        for the deck.

        Parameters:
            None
        Returns:
            None
        """
        # Define user windows for later use
        self.on_deck = None
        self.menu = None

        # Student name labels that appear on the "deck"
        self.student_1 = None                    # label for student in the first slot on the "deck"
        self.student_2 = None                    # label for student in the second slot on the "deck"
        self.student_3 = None                    # label for student in the third slot on the "deck"
        self.student_4 = None                    # label for student in the fourth slot on the "deck"

        # Student names
        self.first = None                        # name of student in the first slot on the "deck"
        self.second = None                       # name of student in the second slot on the "deck"
        self.third = None                        # name of student in the third slot on the "deck"
        self.fourth = None                       # name of student in the fourth slot on the "deck"

        self.highlight_ind = 0                   # Index to keep track of where the highlight currently is

        self.currentQueue = Queue()              # initiate a queue using buildQueue.py
        self.currentQueue.randomize()            # randomize the queue

    def RightKeystroke(self, event):
        """
        Used when the user uses the right arrow keyboard
        button. Makes the student currently highlighted become
        the one to the right of it, or the first position (if
        the current highlight index is at the last position)

        Parameters:
            event: tkinter Event
        Returns:
            None
        """
        # check if the student currently highlighted is at the end of the deck
        if self.highlight_ind == 3:
            old_pos = self.highlight_ind    # index of the previously highlighted student
            self.highlight_ind = 0          # new updated highlight index
            # update the deck to represent which student needs to be highlighted
            self.toggleHighlight(self.highlight_ind, old_pos)
        else:
            # student is not at the end of the deck
            old_pos = self.highlight_ind    # index of the previously highlighted student
            self.highlight_ind += 1         # new updated highlight index
            # update the deck to represent which student needs to be highlighted
            self.toggleHighlight(self.highlight_ind, old_pos)

    def LeftKeystroke(self, event):
        """
        Used when the user uses the left arrow keyboard
        button. Makes the student currently highlighted become
        the one to the left of it, or at the fourth position (if
        the current highlight index is at the first position)

        Parameters:
            event: tkinter Event
        Returns:
            None
        """
        # check if the student currently highlighted is at the beginning of the deck
        if self.highlight_ind == 0:
            old_pos = 0                     # index of the previously highlighted student
            self.highlight_ind = 3          # new updated highlight index
            # update the deck to represent which student needs to be highlighted
            self.toggleHighlight(self.highlight_ind, old_pos)
        else:
            old_pos = self.highlight_ind    # index of the previously highlighted student
            self.highlight_ind -= 1         # new updated highlight index
            # update the deck to represent which student needs to be highlighted
            self.toggleHighlight(self.highlight_ind, old_pos)

    def UpperKeystroke(self, event):
        """
        Used when the user uses the up arrow keyboard
        button. Removes the currently highlighted student from the
        queue, and flags the student in the performance summary.

        Parameters:
            event: tkinter Event
        Returns:
            None
        """
        remove_ind = self.highlight_ind          # index of student who is going to be removed from the queue

        # remove the student from the queue, flags them, and then update the deck
        self.currentQueue.remove(remove_ind, True)
        self.UpdateDeck(self.ondeck())

    def LowerKeystroke(self, event):
        """
        Used when the user uses the up arrow keyboard
        button. Removes the currently highlighted student from the
        queue. Does not flag the student in the performance summary.

        Parameters:
            event: tkinter Event
        Returns:
            None
        """
        remove_ind = self.highlight_ind  # index of student who is going to be removed from the queue
        # remove the student from the queue and then update the deck
        self.currentQueue.remove(remove_ind, False)
        self.UpdateDeck(self.ondeck())

    def toggleHighlight(self, highlight_index, old_pos):
        """
        Used to change which student name is currently
        highlighted after a left or right keystroke.

        Parameters:
            highlight_index: int -- index of which student needs to be highlighted
            old_pos: int -- index of the previously highlighted student.
        Returns:
            None
        """
        # dict. of all the students names, and their positions (index) as the keys
        current_positions = {0: self.student_1, 1: self.student_2, 2: self.student_3, 3: self.student_4}
        old = current_positions.get(old_pos)     # the label of the student that was previously highlighted
        old.configure(bg='black', fg="white")    # removes the highlight of the old label
        self.highlight_ind = highlight_index     # update which index is currently highlighted
        new = current_positions.get(self.highlight_ind)  # the label of the student that is currently highlighted
        new.configure(bg='white', fg='black')    # change the highlight color for the new name that is highlighted
        self.on_deck.update()                    # update the deck to reflect new deck

    def presView(self):
        """
        Purpose is to create the deck window, and initiate the
        names on the deck. Also monitors when the user
        does a keystroke.

        Parameters:
            None
        Returns:
            None
        """
        # Initiate the deck window, and set the dimension and background color
        self.on_deck = Toplevel(height=105, width=750, bg='black')
        deck = self.on_deck
        deck.deiconify()
        # Title the deck window
        deck.title("Ducks on Deck")
        # Prevent the deck from being resized
        deck.resizable(False, False)
        # Make the display window the topmost window at all times
        deck.attributes('-topmost', 'true')

        # initiate the student names
        self.first = StringVar()
        self.second = StringVar()
        self.third = StringVar()
        self.fourth = StringVar()

        names = self.ondeck()  # Get the names of the students
        # assign the names of the students to their respective spots on the deck
        self.first.set(names[0][0].split()[0] + " " + names[0][1].split()[0].replace(',', ''))
        self.second.set(names[1][0].split()[0] + " " + names[1][1].split()[0].replace(',', ''))
        self.third.set(names[2][0].split()[0] + " " + names[2][1].split()[0].replace(',', ''))
        self.fourth.set(names[3][0].split()[0] + " " + names[3][1].split()[0].replace(',', ''))

        self.highlight_ind = 0  # index of the first name that is highlighted on the deck

        # set the first student's position on the deck
        self.student_1 = Label(deck, textvariable=self.first)
        self.student_1.pack(padx=12, pady=6, side=LEFT)
        self.student_1.configure(width=15, height=3, wraplength=100, relief='flat', bg='white', fg="black",
                                 font=("TkDefaultFont", 15))
        # set the second student's position on the deck
        self.student_2 = Label(deck, textvariable=self.second)
        self.student_2.pack(padx=12, pady=6, side=LEFT)
        self.student_2.configure(width=15, height=3, wraplength=100, relief='flat', bg='black', fg="white",
                                 font=("TkDefaultFont", 15))
        # set the third student's position on the deck
        self.student_3 = Label(deck, textvariable=self.third)
        self.student_3.pack(padx=12, pady=6, side=LEFT)
        self.student_3.configure(width=15, height=3, wraplength=100, relief='flat', bg='black', fg="white",
                                 font=("TkDefaultFont", 15))
        # set the fourth student's position on the deck
        self.student_4 = Label(deck, textvariable=self.fourth)
        self.student_4.pack(padx=12, pady=6, side=LEFT)
        self.student_4.configure(width=15, height=3, wraplength=100, relief='flat', bg='black', fg="white",
                                 font=("TkDefaultFont", 15))

        # monitor which keystrokes that are initiated by the user, and all their respective methods
        deck.bind('<Left>', self.LeftKeystroke)
        deck.bind('<Right>', self.RightKeystroke)
        deck.bind('<Up>', self.UpperKeystroke)
        deck.bind('<Down>', self.LowerKeystroke)

        deck.update()

    def ondeck(self):
        """
        Purpose of method is to create and return a list that
        contains only the names of the four students on the
        deck.

        Parameters:
            None
        Returns:
            names: list of names of the students on the deck
        """
        names = []  # list that will be used to store the names of the students on the deck
        # iterate through the queue and add each name to the list
        for stu in self.currentQueue:
            names.append(stu)
        # return the names of the students on deck
        return names[0:4]

    def UserExportTerm(self):
        """
        Calls upon the exportSumPerf function from
        fileWriter.py to export a summary performance
        log using the data from the current queue.

        Parameter:
            None
        Returns:
            None
        """
        # call exportSumPerf from fileWriter.py to
        exportSumPerf(self.currentQueue)

    def MenuDisplay(self):
        """
        Purpose of this method is to create the user menu window,
        and it's corresponding buttons.

        Parameter:
            None
        Returns:
            None
        """
        # initiate the menu window, and set it's title
        self.menu = Tk()
        menu = self.menu
        menu.title(" Ducks on Deck: Menu ")
        # Sets window size
        menu.geometry("250x255")
        # Prevent the menu window from being resized
        menu.resizable(False, False)
        # Set menu background color
        menu.configure(bg='black')

        # Create a Header for the menu
        header = Label(menu, width=50, text="DUCKS ON DECK", bg="black", fg="yellow",
                       font=("TkDefaultFont", 18))
        header.pack(side=TOP, padx=10, pady=15)

        # Create menu buttons
        # export performance summary button
        export_total_button = Button(menu, text="Export Performance\n Summary", font=("TkDefaultFont", 20),
                                     command=self.UserExportTerm, bg="white", width=15)  # initiate the button
        export_total_button.pack(padx=10, pady=10)
        # Button to create a new session
        session_button = Button(menu, text="    New Session   ", font=("TkDefaultFont", 20), command=self.presView,
                                bg="white", width=15)  # initiate the button
        session_button.pack(padx=10, pady=10)
        # Button to exit session
        exit_button = Button(menu, text="            Exit           ", font=("TkDefaultFont", 20), command=self.exit_,
                             bg="white", width=15)  # initiate the button
        exit_button.pack(padx=10, pady=10)
        menu.mainloop()

    def exit_(self):
        """
        Method to exit and end the program. Is called
        when user clicks corresponding exit
        button on the menu window.

        Parameter:
            None
        Returns:
            None
        """
        sys.exit()  # use the exit method from the sys module

    def UpdateDeck(self, current_ducks):
        """
        Purpose of this method to update the student names on the deck.
        Is called upon when students are removed, highlighted, or
        when the deck is initially created.

        Parameter:
            None
        Returns:
            None
        """
        # update and set all the current student names on the deck
        self.first.set(current_ducks[0][0].split()[0] + " " + current_ducks[0][1])
        self.second.set(current_ducks[1][0].split()[0] + " " + current_ducks[1][1])
        self.third.set(current_ducks[2][0].split()[0] + " " + current_ducks[2][1])
        self.fourth.set(current_ducks[3][0].split()[0] + " " + current_ducks[3][1])
        # initiate the update
        self.on_deck.update()

        return


# program driver
if __name__ == "__main__":
    screen = GraphicalUserInterface()
    screen.MenuDisplay()
