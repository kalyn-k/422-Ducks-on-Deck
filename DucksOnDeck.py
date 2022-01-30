"""
Name: DucksOnDeck.py
Purpose: Control the software user interface

Creation Date: Jan. 20, 2022
Last Updated: Jan. 29, 2022

Authors: Kalyn Koyanagi (kek)
TODO add purpose and function of file
Modifications:
Created file    kek     1/20/22
"""

# Import Statements
from tkinter import *                            # used to create all user interface aspects
from buildQueue import *                         # used to build/update a queue using student data
from fileWriter import *                         # used to write to files with session data


class GraphicalUserInterface:

    def __init__(self):
        # Define user windows for later use
        self.on_deck = None
        self.menu = None

        # Student name labels that appear on the "deck"
        self.student_1 = None                    # label for student in the first slot on the "deck"
        self.student_2 = None                    # label for student in the second slot on the "deck"
        self.student_3 = None                    # label for student in the third slot on the "deck"
        self.student_4 = None                    # label for student in the forth slot on the "deck"

        # Student names
        self.first = None                        # name of student in the first slot on the "deck"
        self.second = None                       # name of student in the second slot on the "deck"
        self.third = None                        # name of student in the third slot on the "deck"
        self.forth = None                        # name of student in the forth slot on the "deck"

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
        if self.highlight_ind == 3:
            old_pos = self.highlight_ind
            self.highlight_ind = 0
            self.toggleHighlight(self.highlight_ind, old_pos)
        else:
            old_pos = self.highlight_ind
            self.highlight_ind += 1
            self.toggleHighlight(self.highlight_ind, old_pos)

    def LeftKeystroke(self, event):
        """
        Used when the user uses the left arrow keyboard
        button. Makes the student currently highlighted become
        the one to the left of it, or at the forth position (if
        the current highlight index is at the first position)

        Parameters:
            event: tkinter Event
        Returns:
            None
        """
        if self.highlight_ind == 0:
            old_pos = 0
            self.highlight_ind = 3
            self.toggleHighlight(self.highlight_ind, old_pos)
        else:
            old_pos = self.highlight_ind
            self.highlight_ind -= 1
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
        remove_ind = self.highlight_ind          # index of student who is going to be removed from the queue
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
        new = current_positions.get(self.highlight_ind)     # the label of the student that is currently highlighted
        new.configure(bg='white', fg='black')
        self.on_deck.update()

    def presView(self):
        """

        Returns:
        :None:
        """
        self.on_deck = Toplevel(height=105, width=750, bg='black')
        deck = self.on_deck
        deck.deiconify()
        deck.title("Ducks on Deck")
        deck.resizable(False, False)
        # Make the display window the topmost window at all times
        deck.attributes('-topmost', 'true')
        self.first = StringVar()
        self.second = StringVar()
        self.third = StringVar()
        self.forth = StringVar()

        names = self.ondeck()
        self.first.set(names[0][0].split()[0] + " " + names[0][1].split()[0].replace(',', ''))
        self.second.set(names[1][0].split()[0] + " " + names[1][1].split()[0].replace(',', ''))
        self.third.set(names[2][0].split()[0] + " " + names[2][1].split()[0].replace(',', ''))
        self.forth.set(names[3][0].split()[0] + " " + names[3][1].split()[0].replace(',', ''))

        self.highlight_ind = 0
        # Call highlight toggle?
        self.student_1 = Label(deck, textvariable=self.first)
        self.student_1.pack(padx=12, pady=6, side=LEFT)
        self.student_1.configure(width=15, height=2, wraplength=100, relief='flat', bg='white', fg="black",
                                 font=("TkDefaultFont", 15))

        self.student_2 = Label(deck, textvariable=self.second)
        self.student_2.pack(padx=12, pady=6, side=LEFT)
        self.student_2.configure(width=15, height=2, wraplength=100, relief='flat', bg='black', fg="white",
                                 font=("TkDefaultFont", 15))

        self.student_3 = Label(deck, textvariable=self.third)
        self.student_3.pack(padx=12, pady=6, side=LEFT)
        self.student_3.configure(width=15, height=2, wraplength=100, relief='flat', bg='black', fg="white",
                                 font=("TkDefaultFont", 15))

        self.student_4 = Label(deck, textvariable=self.forth)
        self.student_4.pack(padx=12, pady=6, side=LEFT)
        self.student_4.configure(width=15, height=2, wraplength=100, relief='flat', bg='black', fg="white",
                                 font=("TkDefaultFont", 15))

        deck.bind('<Left>', self.LeftKeystroke)
        deck.bind('<Right>', self.RightKeystroke)
        deck.bind('<Up>', self.UpperKeystroke)
        deck.bind('<Down>', self.LowerKeystroke)

        deck.update()

    def ondeck(self):
        # Maybe try and make this redundant...
        names = []
        for stu in self.currentQueue:
            names.append(stu)
        return names[0:4]

    def UserExportTerm(self):
        """
        Calls upon the exportSumPerf function from
        fileWriter.py to export a summary performance
        log using the data from the current queue.


        Returns:
            None
        """
        exportSumPerf(self.currentQueue)

    def MenuDisplay(self):
        self.menu = Tk()  # Toplevel()  # " Ducks on Deck: Menu ")
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
                       font=("TkDefaultFont", 18))  # Iniate
        header.pack(side=TOP, padx=10, pady=15)
        # Create menu buttons here
        export_total_button = Button(menu, text="Export Performance\n Summary", font=("TkDefaultFont", 20),
                                     command=self.UserExportTerm, bg="white", width=15)
        export_total_button.pack(padx=10, pady=10)
        # Button to create a new session
        session_button = Button(menu, text="    New Session   ", font=("TkDefaultFont", 20), command=self.presView,
                                bg="white", width=15)
        session_button.pack(padx=10, pady=10)
        # Button to exit session
        exit_button = Button(menu, text="            Exit           ", font=("TkDefaultFont", 20), command=self.exit_,
                             bg="white", width=15)
        exit_button.pack(padx=10, pady=10)
        menu.mainloop()

    def exit_(self):
        """
        Method to exit and end the program. Is called
        when user clicks corresponding exit
        button on the menu window.

        Returns:
        :None:
        """
        sys.exit()

    def UpdateDeck(self, current_ducks):
        """

        Returns:
        :None:
        """
        self.first.set(current_ducks[0][0].split()[0] + " " + current_ducks[0][1])
        self.second.set(current_ducks[1][0].split()[0] + " " + current_ducks[1][1])
        self.third.set(current_ducks[2][0].split()[0] + " " + current_ducks[2][1])
        self.forth.set(current_ducks[3][0].split()[0] + " " + current_ducks[3][1])
        self.on_deck.update()

        return


if __name__ == "__main__":
    screen = GraphicalUserInterface()
    screen.MenuDisplay()
