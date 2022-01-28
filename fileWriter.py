"""
fileWriter.py
Creation Date: Jan. 20, 2022
Last Updated: Jan. 26, 2022
Authors: Kelly Schombert (ks), Kalyn Koyanagi (kek)
"""

from datetime import date
import os.path
import os
import csv

today = str(date.today())
dailylog = today + "_log.txt"
termlog = "W2022_log.txt"  # How does user change what the term log name will be? When import a new roster, ask user to come up with a name for the summary perforance file of that roster?

timesCalled = {}
numFlags = {}
listDates = {}


def makeDailyLog():
    """ Called by updateLogs if a log file doesn't already exist """
    dLog = open(dailylog, "w")
    dLog.write("Daily log for cold-call-assist program\n")
    dLog.write(today + "\n\n")
    dLog.close()


def updateLogs(flag: bool, name: str, email: str):
    """ Called by visual.py when ever a keystroke is pressed and a name is removed/flagged """
    if (os.path.exists(dailylog)) == False:
        makeDailyLog()

    response_code = "-\t"
    if flag:
        response_code = "X\t"
    L = [response_code, name + " ", "<", email, ">", "\n"]

    dLog = open(dailylog, "a")
    dLog.writelines(L)
    dLog.close()


def exportSumPerf(roster: list):
    """ Called by visual.py or maybe main.py when the user want to see the Performance Summary """
    # ask for name of sum perf file here? ie W2022_log.txt
    with open('timesCalled.csv', mode='r') as inp:
        reader = csv.reader(inp)
        timesCalled = {rows[0]: int(rows[1]) for rows in reader}
    with open('numFlags.csv', mode='r') as inp:
        reader = csv.reader(inp)
        numFlags = {rows[0]: int(rows[1]) for rows in reader}
    with open('listDates.csv', mode='r') as inp:
        reader = csv.reader(inp)
        listDates = {rows[0]: rows[1] for rows in reader}

    sumPerf = open(termlog, "w")
    sumPerf.write("Summary Performance log for cold-call-assist program\n")
    sumPerf.write(
        "Total times called\t" + "Number of flags\t" + "First Name\t" + "Last Name\t" + "UO ID\t" + "Email Address\t" + "Phonetic Spelling\t" + "List of Dates\t\n");
    sumPerf.write("\n")

    for student in roster:
        name = student[0] + " " + student[1]
        ID = student[2]
        email = student[3]
        calltime = timesCalled[name]
        flagnum = numFlags[name]
        dates = listDates[name]
        sumPerf.write(str(calltime) + "\t" + str(
            flagnum) + "\t" + name + "\t" + ID + "\t" + email + "\t" + name + "\t" + dates + "\n")

    sumPerf.close()


def initSumPerf(roster: list):
    """ Called by fileReader.py to start the summary performance dictionary with the new roster """
    for student in roster:
        name = student[0] + " " + student[1]
        timesCalled[name] = 0
        numFlags[name] = 0
        listDates[name] = ""
    saveCalls = csv.writer(open("timesCalled.csv", "w"))
    saveFlags = csv.writer(open("numFlags.csv", "w"))
    saveDates = csv.writer(open("listDates.csv", "w"))

    for key, val in timesCalled.items():
        saveCalls.writerow([key, val])
    for key, val in numFlags.items():
        saveFlags.writerow([key, val])
    for key, val in listDates.items():
        saveDates.writerow([key, val])

    # print(timesCalled)
    # print("\n")
    # print(numFlags)
    # print("\n")
    # print(listDates)
    # print("\n")


def updateSumPerf(flag: bool, name: str):
    """ Called by visual.py anytime that a keystroke is pressed and a name is removed/flagged """
    with open('timesCalled.csv', mode='r') as inp:
        reader = csv.reader(inp)
        timesCalled = {rows[0]: int(rows[1]) for rows in reader}
    with open('numFlags.csv', mode='r') as inp:
        reader = csv.reader(inp)
        numFlags = {rows[0]: int(rows[1]) for rows in reader}
    with open('listDates.csv', mode='r') as inp:
        reader = csv.reader(inp)
        listDates = {rows[0]: rows[1] for rows in reader}

    # print(timesCalled)
    # print(numFlags)
    # print(listDates)
    # print(today)

    if flag:
        numFlags[name] += 1
    timesCalled[name] += 1
    listDates[name] += today + " "

    # print(timesCalled)
    # print(numFlags)
    # print(listDates)

    saveCalls = csv.writer(open("timesCalled.csv", "w"))
    saveFlags = csv.writer(open("numFlags.csv", "w"))
    saveDates = csv.writer(open("listDates.csv", "w"))

    for key, val in timesCalled.items():
        saveCalls.writerow([key, val])
    for key, val in numFlags.items():
        saveFlags.writerow([key, val])
    for key, val in listDates.items():
        saveDates.writerow([key, val])


""" Testing Purposes """
# if __name__ == "__main__":
#    initSumPerfDict([['Kelly M', 'Schombert', '951763983', 'kschombe@uoregon.edu'], ['Neville', 'Longbottom', '918002345', 'nlongbottom@uoregon.edu'], ['Jonathon', 'Lieder', '951628943', 'jlieder@uoregon.edu'], ['Allyson S', 'McHugh', '917490283', 'amchugh@uoregon.edu']])
#    updateSumPerf(True, "Kelly M Schombert")
#    updateSumPerf(False, "Jonathon Lieder")
#    updateSumPerf(True, "Allyson S McHugh")
#    exportSumPerf([['Kelly M', 'Schombert', '951763983', 'kschombe@uoregon.edu'], ['Neville', 'Longbottom', '918002345', 'nlongbottom@uoregon.edu'], ['Jonathon', 'Lieder', '951628943', 'jlieder@uoregon.edu'], ['Allyson S', 'McHugh', '917490283', 'amchugh@uoregon.edu']])
# updateLogs(True, "Kelly Schombert", "estaypress@uoregon.edu")
# updateLogs(False, "Neville Longbottom", "didknowbro@uoregon.edu")
# updateLogs(True, "Jonathon Lieder", "estaypress@uoregon.edu")
# updateLogs(False, "Allyson McHugh", "didknowbro@uoregon.edu")
