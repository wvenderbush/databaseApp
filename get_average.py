#Team Red Squadron
#Lorenz "Red 2" Vargas and Winston "Luke's Friend from Tatooine" Venderbush

import sqlite3   
import csv      



f="schoolinfo.db"

db = sqlite3.connect(f)
c = db.cursor()   

#==========================================================

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"
sel = c.execute(q) 

students = {}

for record in sel:
	if record[0] in students:
		students[record[0]][0] += int(record[2]);
		students[record[0]][1] += 1;
	else:
		students[record[0]] = [record[2], 1, record[1]];

for i in students:
	average = float(students[i][0])/float(students[i][1])
	print "name: " + i + '\t id: ' + str(students[i][2]) + '\t average: ' + str(average)




	



	  