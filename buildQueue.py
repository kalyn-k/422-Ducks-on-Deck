"""
buildQueue.py

Creation Date: Jan. 20, 2022
Last Updated: Jan. 20, 2022

Authors: Kalyn Koyanagi (kek), Ellie Kobak (ek)

TODO add purpose and function of file
Modifications:
Created file    kek     1/20/22
Initial file 	ek		1/22/22

"""
import random
import fileReader
import fileWriter


class Queue:
    '''
	The purpose of this class is to keep the queue in an organized list
	that follows a queue data structure. 
	'''

    def __init__(self):
        '''
		Parameters: None

		Purpose: initializes the queue from the filereader
		self.queue is a list of lists contatining each student's information
		given by the filereader.py

		Returns: None, stores queue in class
		'''
        self.queue = fileReader.makelist()  # import from file

    def randomize():
        '''
		Parameters: None

		Purpose: randmomizes the order of the queue

		Returns: None, but changes queue order

		'''
        random.shuffle(self.queue)

    def _count():
        '''
		Helper function if wanting to know the length of the queue
		'''
        return len(self.queue)

    def onDeck():
        '''
		Parameters: None

		Purpose: 
		Each list item contains, name, 95 number, XXX TODO
		This helper function returns the first four names in the queue
		which will be displayed to the user.

		Returns: Tuple of 4 list items -> ([], [], [], []). 
		
		'''
        return self.queue[0][0], self.queue[1][0], self.queue[2][0], self.queue[3][0]

    def remove(name, flag):
        '''
		Parameters: 
		name -> int, the number correlation to the name that will be removed
		flag -> bool, if the student's name is flagged either True or False

		Purpose:
		This function allows the removal of any name from the queue. This 
		function is called in the XXXX and then removes the designated name from
		queue and adds it to the end of the queue.

		Returns: None

		'''

        temp = self.queue[name]
        self.queue[name].remove()
        self.queue.append(temp)
        student_name = self.queue[name][2]
        student_email = self.queue[name][3]

        # (flag: bool, name: str, email: str)
        fileWriter.updateLogs(flag, student_name, student_email)
