import sqlite3

con = sqlite3.connect('student.db')
cursor = con.cursor()

sqlite_query_select = '''SELECT* FROM stud_marks'''

cursor.execute(sqlite_query_select)

records = cursor.fetchall()
print(records)

for row in records:
    print('id:',row[0])
    print('name:',row[1])
    print('marks:',row[2])

con.close()