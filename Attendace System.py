from gpiozero import Button
import mysql.connector
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
from time import sleep


reader = SimpleMFRC522()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="STUDENT"
)

mycursor = mydb.cursor()

#def createTable(mycursor, x):
    #mycursor.execute("CREATE TABLE classes(id VARCHAR(50), name VARCHAR(255), teacher VARCHAR(255))")
    
#def createTable:
    #mycursor.execute("CREATE TABLE students(id VARCHAR(50), first VARCHAR(255), last VARCHAR(255), nickname VARCHAR(255))")
    
#def createTable:
    #mycursor.execute("CREATE TABLE attendance(studentid VARCHAR(50), classid VARCHAR(255), datetime VARCHAR(255))")
    
#createTable(mycursor, x)



#def insertTestData(mycursor, classes, id, name, teacher):
    #lgp = "INSERT INTO classes(id, name, teacher) VALUES (%s, %s, %s)"
    #val = (id, name, teacher)

#def insertTestData(mycursor, students, id, firstname, lastname, nickname):
    #lgp = "INSERT INTO students(id, firstname, lastname, nickname) VALUES (%s, %s, %s, %s)"
    #val = (name, brand, price, origin)

#def insertTestData(mycursor, tableName, name, brand, price, origin):
    #lgp = "INSERT INTO (name, brand, price, origin) VALUES (%s, %s, %s, %s)"
    #val = (name, brand, price, origin)
    
#mycursor.execute(val)


print("Scan your Card")
id, name = reader.read()
print("Name"+name)
print("ID:"+id)

def insertProduct(mycursor,id,name):
    Table = input("What is table name"+"classes or students or attendance")
    mycursor.execute("SELECT Name FROM "+Table+" WHERE STUDENT = " + str(id))
    if Table == str(classes):
        name = input("Student name:")
        teacher = input("Teacher name:")
        print("Student's name" + name)
        print("Teacher's name" + teacher)
        mycursor.execute("INSERT INTO classes(id, name, teacher) VALUES('" + str(id) + "','" + name + "')")
        mydb.commit()
        print("class added")
        updatePrice(mycursor, nPrice, id)

    
    
inserProduct()   