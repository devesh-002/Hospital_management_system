import pymysql
import datetime
import pymysql.cursors
from function import *
con = pymysql.connect(host='localhost',user='root',password='123',db='hospital',cursorclass=pymysql.cursors.DictCursor)
if(con.open):
    print("Hi,")
else:
    print("Connection Error")
cur=con.cursor()
while(True):
    print("Which table do you want to work on:-")
    print("1 for admin")
    print("2 for users")
    print("3 for tel_no_users")
    print("4 for address_users")
    print("5 for doctor")
    print("6 for permission")
    print("7 for patient")
    print("8 for other_workers")
    print("9 for medicine")
    print("10 for treatment")
    print("11 for medicalRecord")
    print("12 to check cost for a medicine post discount")
    print("13 to check age for a user")
    print("14 to generate Report 1 which finds total medicine cost used by each patient along with patients names using JOIN technique")
    print("15 to generate the second report which generates the patient details under a specific doctor")
    print("16 to exit the user interface")
    command=int(input("Enter your preference:-"))
    print(command)
    if command==1:
        admin(con,cur)
    elif command==2:
        users(con,cur)
 
    elif command==3:
        tel_no_users(con,cur)
    elif command==4:
        address_users(con,cur)
    elif command==5:
        pass
    elif command==6:
        permission(con,cur)
    elif command==7:
        patient(con,cur)
    elif command==8:
        other_workers(con,cur)
    elif command==9:
        medicine(con,cur)
    elif command==10:
        treatment(con,cur)
    elif command==11: 
        treatment(con,cur)
    elif command==12:
        costForMedicine(con,cur)
    elif command==13:
        findAge(con,cur)
    elif command ==14: # For Report 1 generation
        report1(con,cur)
    elif command==15:
        report2(con,cur)
    elif command==16:
        print("Bye")
        exit()
