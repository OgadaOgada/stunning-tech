import mysql.connector

# host
# user
# password
# database
mycon = mysql.connector.connect(host="localhost",user="collince",passwd="1234",database="ctech")

mycursor = mycon.cursor()
# dbquery = "use ctech"  #if you didn't specify db in connnection you can use it by this use statement
updatedata = "update student set college = 'Afralti' where id = 2"
fetchdata = "select * from student"
mycursor.execute(fetchdata)
for i in mycursor:
    print(i)
mycursor.execute(updatedata)
print("\n\n")
mycursor.execute(fetchdata)

for i in mycursor:
    print(i)