import pymysql
import getpass

tablename = "NONE"

def create_table():
	global tablename
	tablename = input("name of table: ")
	n = int(input("what are the number of fields: "))
	global field
	field = input("what are the fields: ").split()
	mycursor.execute("CREATE TABLE "+tablename+" (id INT AUTO_INCREMENT PRIMARY KEY)")
	for i in range(n):
		mycursor.execute("ALTER TABLE "+tablename+" ADD COLUMN "+field[i]+" VARCHAR(255)")

def table_list():
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

def delete_table():
	name = input("delete which table: ")
	mycursor.execute("DROP TABLE IF EXISTS "+name)

def change_table():
	global tablename
	tablename = input("Select which table: ")

	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM "+tablename+" LIMIT 0")
	n = len(mycursor.description)
	global field
	field = []
	for i in range(1,n):
		field.append(mycursor.description[i][0])
	print("Table Selected")	
	print("Table contains the following fields-")
	print(field)	

def insert_entry():
	sql = "INSERT INTO "+tablename+" ("
	for f in range(len(field)):
		if f is not len(field)-1 : sql = sql+field[f]+","
		else : sql = sql+field[f]

	sql = sql+") VALUES ("
	for f in range(len(field)):
		if f is not len(field)-1 : sql = sql+"%s"+","
		else : sql = sql+"%s"
	sql = sql+')'

	row = []
	n = int(input("Number of Entries: "))
	for x in range(n):
		ent = []
		for f in field:
			ent.append(input(f+": "))
		row.append(ent)	

	mycursor.executemany(sql, row)
	mydb.commit()
	print(mycursor.rowcount, "entries inserted.")
	print(row)

def show_entry():
	mycursor.execute("SELECT * FROM "+tablename)
	myresult = mycursor.fetchall()
	for x in myresult:
  		print(x)

def delete_entry():
	field_here = input("Which field contain the value in entries: ")
	value = input("What is the value: ")
	sql = "DELETE FROM "+tablename+" WHERE "+field_here+" LIKE '%"+value+"%'"
	mycursor.execute(sql)
	mydb.commit()
	print(mycursor.rowcount, "record(s) deleted")

def update_entry():
	field_here = input("Which field contains the value to be changed: ")
	current_value = input("Current value: ")
	new_value = input("New value: ")

	sql = "UPDATE "+tablename+" SET "+field_here+" = '"+new_value+"' WHERE "+field_here+" = '"+current_value+"'"
	mycursor.execute(sql)
	mydb.commit()
	print(mycursor.rowcount, "record(s) affected")	

try:
	pswd = getpass.getpass("Enter root password: ")

	mydb = pymysql.connect(
		host = "localhost",
		user = "root",
		passwd = pswd,
		database = "new")
except:
	print("WRONG PASSWORD!")

mycursor = mydb.cursor()
selection = 0
while selection is not 10:
	print("**************************************")
	print("OPERATIONS-")
	print("1-Create Table")
	print("2-Show list of tables available")
	print("3-Show Active Table")
	print("4-Delete a Table")
	print("5-Select Working Table")
	print("6-Insert Entries in Table")
	print("7-Show Entries")
	print("8-Delete Entries")
	print("9-Update Entries")
	print("10-exit")
	print("**************************************")
	selection = int(input("Which operation to perform: "))

	if selection is 1 : create_table()
	elif selection is 2 : table_list()
	elif selection is 3 : print(tablename)
	elif selection is 4 : delete_table()
	elif selection is 5 : change_table()
	elif selection is 6 : insert_entry()
	elif selection is 7 : show_entry()
	elif selection is 8 : delete_entry()
	elif selection is 9 : update_entry()
	elif selection is 10 : pass	

