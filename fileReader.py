"""
fileReader.py
Creation Date: Jan. 20, 2022
Last Updated: Jan. 27, 2022
Authors: Kalyn Koyanagi (kek)
TODO add purpose and function of file
Modifications:
Created file        kek     1/20/22
Initial version     ek      1/23/22
Modified file       ks      1/26/22
Finalized file      ek      1/27/22
"""

from fileWriter import *
import fileWriter
import sys
import os
import fileinput

roster_list = []

def getFileName():
    fname = ""
    welcome_message = "Please type in the file name of a csv or text file that \ncontains your class roster.\nThis is an infinit loop until a valid file is entered.\nTo exit program press 'ctl + c\n"    
    print(welcome_message)
    for line in sys.stdin:
        print(f"File entered: {line.rstrip()}")
        print("Press 'ctr + d' to submit file")
        fname = line.rstrip()

    return fname

def filereader():
    '''
    input: file - a tab deliminated file from standard input
    returns: a list of all the people in the following order
    [	[<name>, <95 number>, <email>,<>,<>]
    	[<name>, <95 number>, <email>,<>,<>]
    	[<name>, <95 number>, <email>,<>,<>]	]
    ['First', 'Name', 'Last', 'Name', 'UO', 'ID', '#', 'Email', 'Address',
    'Kyle', 'M', 'Amsler', '950344746', 'Amsler@uoregon.edu',
    5 items but need list of [[Name, ID, email]]
    TODO
    '''
    
    #print(f'Input : {line}')
    valid = False
    while (valid != True):
        fname = getFileName()
        valid = os.path.exists(fname)


    print(f"the file inputted was {fname}")
    
    with open(fname, 'r') as roster:
        #print(roster.read())

        file_data = roster.read().split("\n")
        #print(file_data)

        for i in range(len(file_data)):
            data = file_data[i].split("\t")
            #print(data)
            if i != 0:
                roster_list.append(data)

            #print(roster_list)
            #fileWriter.initSumPerf(roster_list)
            #print("DONE WITH INITSUFPERF\n")
            #fileWriter.exportSumPerf(roster_list)
            #print("DONE WITH EXPORTING\n")

""" Testing Purposes """
#if __name__== "__main__":
    #filereader()
    #filename = 'Fake_class_info.txt'
    #filename = 'Short_Fake_class_info.txt'
    #filereader(filename)
