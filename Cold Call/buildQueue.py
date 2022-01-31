"""
Name: buildQueue.py
Purpose: Class Queue is the data structure that keeps track of which names need to be 
sent to the Deck, how to remove names from the deck, and sends information to file writer

Creation Date: Jan. 20, 2022
Last Updated: Jan. 30, 2022
Authors: Kalyn Koyanagi (kek), Ellie Kobak (ek)

buildQueue.py is part of the Ducks on Deck cold-calling assist software.
Called by:
	DucksOnDeck.py - uses queue to display roster and uses queue class functions to remove names from deck

Modifications:
Created file    kek 1/20/22
Initial file 	ek	1/22/22
File complete	ek 	1/26/22
File updated	ek 	1/28/22
Debugging	    kek	1/29/22

"""
import random  # used to randomize queue order
import fileWriter  # sends information to be exported when a name is removed
import fileReader


class Queue:
    """
    The purpose of this class is to keep the queue in an organized list
    that follows a queue data structure.
    """

    def __init__(self):
        """
        Parameters: None

        Purpose: initializes the queue from the filereader
        self.queue is a list of lists contatining each student's information
        given by the filereader.py

        Calls filereader() from filereader.py to get student info list

        Returns: None, stores queue in class
        """
        self.queue = fileReader.filereader()  # imports data from file

    def randomize(self):
        """
        Parameters: None

        Purpose: randmomizes the order of the queue

        Called by DucksOnDeck.py before names are displayed on deck

        Returns: None, but changes queue order

        """
        random.shuffle(self.queue)

    def __iter__(self):
        """
        Helper method to make the queue iterable.
        """
        return iter(self.queue)

    def _count(self):
        """
        Helper function if wanting to know the length of the queue
        """
        return len(self.queue)

    def onDeck(self):
        """
        Parameters: None

        Purpose:
        This function returns the first four names in the queue
        which will be displayed to the user.

        Called by:
        DucksOnDeck.py to display the top four names in queue

        Returns: Tuple of 4 list items -> ([], [], [], [])
        """
        return self.queue[0][0], self.queue[1][0], self.queue[2][0], self.queue[3][0]

    def remove(self, name, flag):
        """
        Parameters:
        name -> int, the number correlation to the name that will be removed
        flag -> bool, if the student's name is flagged either True or False

        Purpose:
        This function allows the removal of any name from the queue. This
        function is called by:
        DucksOnDeck.py - removes the designated name from queue and then adds removed name to end of the queue.

        Returns: None
        """
        temp = self.queue[name]  # temp variable to keep track of name being removed

        self.queue.remove(self.queue[name])  # removes name from Deck
        self.queue.append(temp)  # adds removed name to end of queue

        student_name = self.queue[name][0] + " " + self.queue[name][1]  # get student's name to send to the file writer
        student_email = self.queue[name][3]  # get student's email to send to the file writer
        student_name = student_name.strip()  # strip the student's name of white space

        # (flag: bool, name: str, email: str)
        fileWriter.updateLogs(flag, student_name, student_email)  # update logs in fileWriter
        fileWriter.updateSumPerf(flag, student_name)  # updates summary performance in fileWriter
