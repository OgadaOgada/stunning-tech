import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="collince",passwd="1234",database="ctech")
mycursor = mydb.cursor()

# dbquery = "use ctech"  #if you didn't specify db in connnection you can use it by this use statement

#UPDATE DATA IN A DATABASE TABLE
# updatedata = "update student set college = 'Afralti' where id = 2"
# mycursor.execute(updatedata)
# mydb.commit()

#DELETE DATA IN A DATABASE TABLE
# updatedata = "delete from student where id = 2"
# mycursor.execute(updatedata)
# mydb.commit()


# #INSERTING DATA FROM PYTHON TO DATABASE TABLE

insertdata = "insert into student (name,college) values (%s,%s)"
fname = input("What's your name: ")
college = input("What's your college: ")
datavalues = (fname,college)
# datavalues =  [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
mycursor.execute(insertdata, datavalues)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

print("\n")


#FETCH DATA FROM MYSQL DATABASE TABLE
fetchdata = "select * from student"
# fetchdata = "SELECT * FROM customers WHERE college = %s" # %s is to prevent injection
# college = ("Nairobi")
# mycursor.execute(fetchdata,college)
# fetchdata = "show databases"
# fetchdata = "show tables"
mycursor.execute(fetchdata)
result = mycursor.fetchall()
# result = mycursor.fetchone()
for i in result:
    print(i)