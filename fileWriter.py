"""
fileWriter.py

Creation Date: Jan. 20, 2022
Last Updated: Jan. 23, 2022

Authors: Kelly Schombert (ks)

"""

from datetime import date
import os.path

today = str(date.today())
dailylog = today + "_log.txt"
termlog = "W2022_log.txt"


def exportDailyLog():
    os.startfile(dailylog)


def exportTermLog():
    os.startfile(termlog)


def makeDailyLog():
    file1 = open(dailylog, "w")
    file1.write("Daily log for cold-call-assist program\n")
    file1.write(today + "\n\n")
    file1.close()


def makeTermLog():
    file2 = open(termlog, "w")
    file2.write("Summary Performance log for cold-call-assist program\n")
    file2.close()


def updateLogs(flag: bool, name: str, email: str):
    if (os.path.exists(dailylog)) == False:
        makeDailyLog()

    response_code = "-\t"
    if flag:
        response_code = "X\t"
    L = [response_code, name + " ", "<", email, ">", "\n"]

    file1 = open(dailylog, "a")
    file1.writelines(L)
    file1.close()


if __name__ == "__main__":
    "makeDailyLog()"
    updateLogs(True, "Enemies Staypressed", "estaypress@uoregon.edu")
    updateLogs(False, "Didn't Knowbro", "didknowbro@uoregon.edu")
