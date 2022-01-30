"""
Name: fileReader.py
Purpose: To parse the input file into a mutable and usable Queue data structure.

Creation Date: Jan. 20, 2022
Last Updated: Jan.  30, 2022
Authors: Kalyn Koyanagi (kek), Ellie Kobak (ek)

filereader.py is part of the Ducks on Deck cold-calling assist software.
Called by:
    buildQueue.py - creates the queue from parsed file input

Modifications:
Created file        kek     1/20/22
Initial version     ek      1/23/22
Modified file       ks      1/26/22
Finalized file      ek      1/27/22
Updated comments    ek      1/30/22
"""

import sys                  # used sys to get user input from command line
import os                   # used os to validate existing file name and or file path from standard input
import fileWriter           # sends initialized queue in alphabetic order to summary perfomance        

#roster_list = []

def getFileName():
    '''
    Helper function for filereader that gets the file name from standard input.
    Called by filereader().
    Returns the file name.
    '''
    fname = ""  # initialized string for file name input
    # message to user with instructions on what to input and interact with the system
    welcome_message = "Please type in the file name of a csv or text file that \ncontains your class roster in a tab deliminated format.\nThis is an infinit loop until a valid file is entered.\nTo exit program press 'ctl + c\n"    
    print(welcome_message) # displays message to uder/standard output
    
    # interprets standard input
    for line in sys.stdin:
        print(f"File entered: {line.rstrip()}") # displays to user the file they entered, useful for ensuring correct file input
        print("Press 'ctr + d' to submit file") # how to exit standard input
        fname = line.rstrip() # strips input of white space and new line characters

    return fname # returns file name

def filereader():
    '''
    Purpose: Parse through tab deliminated file or text file to organize roster data.
    Called by buildQueue.py.
    input: none, but calls getFileName() for file name.
    returns: a list of all the people in the following order
    [	[<name>, <95 number>, <email>]
    	[<name>, <95 number>, <email>]
    	[<name>, <95 number>, <email>]	]
    '''
    roster_list = []    # initialized list for student information to be updated and added too
    valid = False       # initialized boolean to check if valid file path/file name
    while (valid != True): #verifies a valid file name has been entered, if not asks for file again
        fname = getFileName() # variable to keep track of file name
        valid = os.path.exists(fname) # checks if valid file name 


    print(f"the file inputted was {fname}") # allows use to know what file they entered
    
    with open(fname, 'r') as roster: # below parses the file 

        file_data = roster.read().split("\n") # splits each line into a list

        for i in range(len(file_data)): # divides the list of each student into usable form
            data = file_data[i].split("\t") # splits into the name, ID number, and email
            if i != 0:
                roster_list.append(data) 

            fileWriter.initSumPerf(roster_list) # initializes summary performance document in alphabetic order
            
    return roster_list # returns list of lists

""" Testing Purposes """
#if __name__== "__main__":
    #filereader()
    #filename = 'Fake_class_info.txt'
    #filename = 'Short_Fake_class_info.txt'
    #filereader(filename)
