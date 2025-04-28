
#STUDENT MANAGEMENT SYSTEM IN PYTHON
import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
 user="root",\
 passwd ="",\
 database="student")
print("-----------------------------")
print("Enter Student details here: ")
print("-----------------------------")
def student():
 mycursor=mydb.cursor()
 L=[]
 s_id=input("Enter Student ID: ")
 L.append(s_id)
 s_name=input("Enter Student Name : ")
 L.append(s_name)
 s_fname=input("Enter Student Father Name: ")
 L.append(s_fname)
 s_address=input("Enter Student Address : ")
 L.append(s_address)
 s_phone=input("Enter Phone Number : ")
 L.append(s_phone)
 s_course=input("Enter Course : ")
 L.append(s_course)
 sql="insert into std values (%s,%s,%s,%s,%s,%s)"
 mycursor.execute(sql,L)
 mydb.commit()
 print("_____________________________________________________")
 print("Welcome Mr./Mrs. ",s_name,". Thanks for your joining.")
 print("_____________________________________________________")
 MenuSet()
def Viewall():
 mydb=mysql.connector.connect(host="localhost",\
 user="root",\
 passwd ="",\
 database="student")
 mycursor=mydb.cursor()
 sql="select * from std"
 mycursor.execute(sql)
 res=mycursor.fetchall()
 for x in res:
     print("_____________________________________________________")
     print("SEARCH DETAILS OF AN STUDENT ID:- ",x[0])
     print("")
     print("Student ID: ",x[0])
     print("Student Name: ",x[1])
     print("Student Father's Name: ",x[2])
     print("Student Address: ",x[3])
     print("Student Phone No.: ",x[4])
     print("Student Course:",x[5])
     print("")
     print("____________________________________________________________")
 MenuSet()
def Update():
 mydb=mysql.connector.connect(host="localhost",\
 user="root",\
 passwd ="",\
 database="student")
 mycursor=mydb.cursor()
 s=input("Enter Student ID : ")
 rl=(s,)
 sql="select * from std where s_id=%s"
 mycursor.execute(sql,rl)
 res=mycursor.fetchall()
 if(mycursor.rowcount > 0):
     for x in res:
         print("_________________________________________________________")
         print("SEARCH DETAILS OF AN Student ID:- ",x[0])
         print("")
         print("Student ID: ",x[0])
         print("Student Name: ",x[1])
         print("Student Father's Name: ",x[2])
         print("Student Address: ",x[3])
         print("Student Phone No.: ",x[4])
         print("Student Course:",x[5])
         print("")
         print("________________________________________________________")
         print("Enter Student Details For Update Against Student ID:- ",x[0])
 else:
     print("Records Not Found.....")
     MenuSet()
 L=[]
 temp=s
 s_name=str(input("Enter Student Name : "))
 L.append(s_name)
 s_fname=input("Enter Student Father Name: ")
 L.append(s_fname)
 s_address=str(input("Enter Student Address : "))
 L.append(s_address)
 s_phone=str(input("Enter Phone Number : "))
 L.append(s_phone)
 s_course=str(input("Enter Course : "))
 L.append(s_course)
 L.append(temp)
 cust=(L)
 sql="update std set s_name=%s,s_fname=%s,s_address=%s,s_phone=%s,s_course=%s where s_id=%s"
 mycursor.execute(sql,cust)
 mydb.commit()
 print("_____________________________________________________")
 print("Welcome Mr./Mrs. ",s_name,". Your Records Are Updated.")
 print("_____________________________________________________")
 MenuSet()
def Delete():
 mydb=mysql.connector.connect(host="localhost",\
 user="root",\
 passwd ="",\
 database="student")
 mycursor=mydb.cursor()
 print("ENTER STUDENT DETAILS FOR DELETE")
 print("____________________________________")
 s=input("Enter Student ID : ")
 rl=(s,)
 sql="delete from std where s_id=%s"
 mycursor.execute(sql,rl)
 mydb.commit()
 if(mycursor.rowcount > 0):
     print("Thanks..! Your Record are Deleted")
     print("_______________________________________")
 else:
     print("No Records found for Delete")
     print("_______________________________________")
 MenuSet()
def Search():
    mydb=mysql.connector.connect(host="localhost",\
 user="root",\
 passwd ="",\
 database="student")
    mycursor=mydb.cursor()
    L=[]
    id=input("ENTER ID TO SEARCH: ")
    L.append(id)
    sql="select * from std where s_id=%s"
    mycursor.execute(sql,L)
    for x in mycursor:
        print("Student ID: ",x[0])
        print("Student Name: ",x[1])
        print("Student Father's Name: ",x[2])
        print("Student Address: ",x[3])
        print("Student Phone No.: ",x[4])
        print("Student Course: ",x[5])
    print(mycursor.rowcount,"records are there")
    MenuSet()
def MenuSet():
 print("_______________________________________")
 print("-------------WELCOME BOYS--------------")
 print("_______________________________________")
 print("-------Student Management System-------")
 print("_______________________________________")
 print("1 : Add Student")
 print("2 : View All Student Details")
 print("3 : Search Student Details")
 print("4 : Update Student")
 print("5 : Delete Student")
 print("6 : Quit")
 print("_______________________________________")
 print("")
 try:
     userInput = int(input("Please Select An Above Option: "))
     if(userInput==1):
         student()
     elif (userInput==2):
         Viewall()
     elif (userInput==3):
         Search()
     elif (userInput==4):
         Update()
     elif (userInput==5):
         Delete()
     elif (userInput==6):
         quit()
     else:
         print("Incorrect choice. . . ")
         quit()
 finally:
     print("Incorrect choice...")
MenuSet()
