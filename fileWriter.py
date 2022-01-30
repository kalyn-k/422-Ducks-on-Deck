"""
Name: fileWriter.py
Purpose: To create and update daily logs and summary performance file.
Creation Date: Jan. 20, 2022
Authors: Kelly Schombert (ks), Kalyn Koyanagi (kek)

fileWriter.py is part of the Ducks on Deck cold-calling assist software. 
Called by:
    fileReader.py - initialize summary performance dictionaries for a new roster of sutdents.
    buildQueue.py - update daily log and summary performance dictionaries.
    visual.py - write summary performance file.

Modifications:
    File created - Jan. 20, 2022 - kek
    File moved to new repository - Jan. 23, 2022 - ks
    Daily log functionality implemented - Jan. 25, 2022 - ks
    Export functions added - Jan. 26, 2022 - kek
    Export functions tested and removed, summary performance dictionaries implemented - Jan. 26, 2022 - ks
    Functions tested individually and with fileReader.py - Jan. 26, 2022 - ks
    Full functionality implemented - Jan. 27, 2022 - ks
    Code Documentation completed - Jan. 27, 2022 - ks
"""

from datetime import date   # used to create daily log file name and to record dates of individual cold calls
import os.path              # used to check if daily log file already exists for current date 
import csv                  # used to implement writing to and reading from csv files
import sys                  # used to read user input from stdin

today = str(date.today())       # str containing currect date; formatted as YYYY-MM-DD
dailylog = today + "_log.txt"   # str containing daily log file name; formatted as YYYY-MM-DD_log.txt

timesCalled = {}    # dictionary tracking how many times each student is cold called
numFlags = {}       # dictionary tracking how many times a student is flagged
listDates = {}      # dictionary storing every date a student is cold called on

def makeDailyLog():
    """
    Creates daily log file and writes heading to file.
    Called by updateLogs() if the daily log file hasn't been created yet.
    """
    dLog = open(dailylog, "w")  # daily log file object
    dLog.write("Daily log for cold-call-assist program\n")
    dLog.write(today + "\n\n")
    dLog.close()

def updateLogs(flag: bool, name: str, email: str):
    """ 
    Updates daily log txt file by appending line with relevant student data passed to function.
    Called by buildQueue.py when a keystroke is pressed and a name is removed/flagged.

    :bool flag: False if student was not flagged, True if student was flagged
    :str name: name of student cold called
    :str email: email address of student cold called
    """
    if (os.path.exists(dailylog)) == False:
        makeDailyLog()

    response_code = "-\t"                                       # response code for daily log record; default indicates no flag for a student
    if flag:
        response_code = "X\t"                                   # response code indicating a flag for a student
    L = [response_code, name + " ", "<", email, ">", "\n"]      # line written to daily log file

    dLog = open(dailylog, "a")                                  # daily log file object
    dLog.writelines(L)
    dLog.close()

def exportSumPerf(roster: list):
    """
    Reads current csv file data to corresponding dictionary, asks user for summary performance file name, writes heading and student data to summary performance file.
    Called by DucksOnDeck.py when user chooses to export summary performance data

    :list roster: list of student data: first name, last name, ID number, email address
    """
    with open('timesCalled.csv', mode='r') as inp:
        reader = csv.reader(inp)                                    # csv reader object for timesCalled.csv file
        timesCalled = {rows[0]:int(rows[1]) for rows in reader}
    with open('numFlags.csv', mode='r') as inp:
        reader = csv.reader(inp)                                    # csv reader object for numFlags.csv file
        numFlags = {rows[0]:int(rows[1]) for rows in reader}
    with open('listDates.csv', mode='r') as inp:
        reader = csv.reader(inp)                                    # csv reader object for listDates.csv file
        listDates = {rows[0]:rows[1] for rows in reader}
    
    sumPerfname = ""                                                # summary performance file name; initialized to be empty 
    message = "Please type in the name you would prefer for the summary performance log\nThe file name will be formatted as [chosen_name].txt\nTo exit program, press ctl + c\n"    # instructions to user for entering summary performance file name
    print(message)
    for line in sys.stdin:
        print(f"\nFile name entered: {line.rstrip()}")
        print("Press 'ctr + d' to submit file")
        sumPerfname = line.rstrip() + ".txt"

    sumPerf = open(sumPerfname, "w")                                # summary performance file object
    sumPerf.write("Summary Performance log for cold-call-assist program\n")
    sumPerf.write("Total times called\t" + "Number of flags\t" + "First Name\t" + "Last Name\t" + "UO ID\t" + "Email Address\t" + "Phonetic Spelling\t" + "List of Dates\t\n");
    sumPerf.write("\n")
    
    for student in roster:
        name = student[0] + " " + student[1]                        # full student name; adds first and last name together
        name = name.strip()
        ID = student[2]                                             # student ID number
        email = student[3]                                          # student email address
        calltime = timesCalled[name]                                # number of times student was cold called
        flagnum = numFlags[name]                                    # number of flags student has
        dates = listDates[name]                                     # string of all dates student has been cold called on
        sumPerf.write(str(calltime) + "\t" + str(flagnum) + "\t" + name + "\t" + ID + "\t" + email + "\t" + name + "\t" + dates + "\n")

    sumPerf.close()

def initSumPerf(roster: list):
    """
    Initialized summary performancy dictionaries and corresponding csv files.
    Called by fileReader.py with the import of a new roster of students.

    :list roster: list of student data: first name, last name, ID number, email address
    """
    for student in roster:
        name = student[0] + " " + student[1]                    # full student name; adds first and last name together
        name = name.strip()

        timesCalled[name] = 0                                   # timeCalled dict value initialized to 0
        numFlags[name] = 0                                      # numFlags dict value intialized to 0
        listDates[name] = ""                                    # listDates dict value initialized to empty string
    
    saveCalls = csv.writer(open("timesCalled.csv", "w"))        # csv writer object for timesCalled.csv file
    saveFlags = csv.writer(open("numFlags.csv", "w"))           # csv writer object for numFlags.csv file
    saveDates = csv.writer(open("listDates.csv", "w"))          # csv writer object for listDates.csv file

    for key, val in timesCalled.items():
        saveCalls.writerow([key, val])
    for key, val in numFlags.items():
        saveFlags.writerow([key, val])
    for key, val in listDates.items():
        saveDates.writerow([key, val])

def updateSumPerf(flag: bool, name: str):
    """ 
    Reads current csv file data to corresponding dictionary, updates student data in dictionary, writes new data to csv files.
    Called by visual.py anytime that a keystroke is pressed and a student is cold called.

    :bool flag: False if student was not flagged, True if student was flagged
    :str name: name of student cold called
    """
    with open('timesCalled.csv', mode='r') as inp:
        reader = csv.reader(inp)                                # csv reader object for timesCalled.csv file
        timesCalled = {rows[0]:int(rows[1]) for rows in reader}
    with open('numFlags.csv', mode='r') as inp:
        reader = csv.reader(inp)                                # csv reader object for numFlags.csv file
        numFlags = {rows[0]:int(rows[1]) for rows in reader}
    with open('listDates.csv', mode='r') as inp:
        reader = csv.reader(inp)                                # csv reader object for listDates.csv file
        listDates = {rows[0]:rows[1] for rows in reader}

    if flag:
        numFlags[name] += 1
    timesCalled[name] += 1
    listDates[name] += today + " "
    
    saveCalls = csv.writer(open("timesCalled.csv", "w"))        # csv writer object for timesCalled.csv file
    saveFlags = csv.writer(open("numFlags.csv", "w"))           # csv writer object for numFlags.csv file
    saveDates = csv.writer(open("listDates.csv", "w"))          # csv writer object for listDates.csv file

    for key, val in timesCalled.items():
        saveCalls.writerow([key, val])
    for key, val in numFlags.items():
        saveFlags.writerow([key, val])
    for key, val in listDates.items():
        saveDates.writerow([key, val])
