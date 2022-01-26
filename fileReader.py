"""
fileReader.py

Creation Date: Jan. 20, 2022
Last Updated: Jan. 20, 2022

Authors: Kalyn Koyanagi (kek)

TODO add purpose and function of file
Modifications:
Created file    kek     1/20/22

"""
def filereader(fname):
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
	roster_list = []

	with open(fname, 'r') as roster:
	
		file_data = roster.read().split()
		extra = file_data[9:]

		for i in range(len(extra)):
			extra[i].replace(',', ' ')

		print(len(extra))
		print()
		
		#print(file_data)
		copy = file_data[9:]
		length = len(copy)
		print(length)
		j = 0
		for j in range(len(copy)):
			print("first i:       ", i)
			student_info = []
			name = copy[j] + " " + copy[j + 2]
			id_num = copy[j + 3]
			email = copy[j + 4]
	
			student_info.append(name)
			student_info.append(id_num)
			student_info.append(email)
			
			j += 3
			print("student info :   ", student_info)
			roster_list.append(student_info)
			print("second i:       ", j)
			print()
		


		'''while (i < length):

			student_info = []
			name = copy[i] + " " + copy[i + 2]
			id_num = copy[i + 3]
			email = copy[i + 4]
	
			student_info.append(name)
			student_info.append(id_num)
			student_info.append(email)
			print(i)
			i += 3
			print("student info :   ", student_info)
			roster_list.append(student_info)'''
			

		print("roster list:   ", roster_list)
		

		#for student in range(len(student_roster)):
			#student_info = []
os.chdir("/Users/elliekobak/Desktop/CIS422/422-Ducks-on-Deck/test_data")
filename = 'Fake_class_info.txt'
filereader(filename)
