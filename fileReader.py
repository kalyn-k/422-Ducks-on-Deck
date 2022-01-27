"""
fileReader.py
Creation Date: Jan. 20, 2022
Last Updated: Jan. 26, 2022
Authors: Kalyn Koyanagi (kek)
TODO add purpose and function of file
Modifications:
Created file    kek     1/20/22
Modified file   ks      1/26/22
"""

import fileWriter

def filereader(fname):
        ''' 
        input: file - a tab deliminated file from standard input
        returns: a list of all the people in the following order
        [       [<name>, <95 number>, <email>,<>,<>]
                [<name>, <95 number>, <email>,<>,<>]
                [<name>, <95 number>, <email>,<>,<>]    ]
        ['First', 'Name', 'Last', 'Name', 'UO', 'ID', '#', 'Email', 'Address',
        'Kyle', 'M', 'Amsler', '950344746', 'Amsler@uoregon.edu',
        5 items but need list of [[Name, ID, email]]
        
         TODO
        '''
        roster_list = []

        with open(fname, 'r') as roster:
            #print(roster.read())

            file_data = roster.read().split("\n")
            #print(file_data)

            for i in range(len(file_data)):
                data = file_data[i].split("\t")
                #print(data)
                if i != 0:
                    roster_list.append(data)

            print(roster_list)
            fileWriter.initSumPerf(roster_list)


if __name__== "__main__":
    #filename = 'Fake_class_info.txt'
    filename = 'Short_Fake_class_info.txt'
    filereader(filename)
