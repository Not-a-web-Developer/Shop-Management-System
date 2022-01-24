from logging import root
import mysql.connector as c
import datetime
import time
import utils

print("Initialising app...")
print("Logging into the database...")
sql_usrnm = input("MySQL Username: ")
sql_pw = input("MySQL password: ")

con=c.connect(user=sql_usrnm, password=sql_pw, host="localhost", database="Shop")
print("connection succeeded!")

time.sleep(.5)

utils.cls()
print(' Welcome to The Shop! ')
print
print('1. Login')
print('2. Crete Account')
print('3. Delete Account')
print('4. View Details') # what the heck is this supposed to do?
print('5. Exit')
ch1=int(input("Select the option you want:"))
if ch1==1:
    sn()
if ch1==2:
    create()




def sn():
    print("1. Employee Login ")
    print("2. User Login")
    print("3. Exit")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        code=int(input("Enter Your Employee ID:"))
        pwd=input("Enter Your Password:")
        c1.execute("select * from employee where emp_code={} and password={}".format(code,pwd))
        dat=c1.fetchall()
        hi=list(dat)
        






def create():
    print("1. User Account")
    print("2. Employee Account")
    print("3. Exit")
    ch2=int(input("Enter Your Choice:"))
    if ch2==1:
        print("User Account Registration")
        u=input("Enter Your User ID:")
        c1.execute("select user_id from user")
        hat=c1.fetchall()
        h2=list(hat)
        for i in range(len(h2)):
            if h2[i]==u:
                print("USER ID ALREADY EXITS")



            else:
                n=input("ENTER YOUR NAME:")
                c=input("ENTER YOUR CITY:")
                z=int(input("ENTER YOUR PHONE NUMBER:"))
                query="insert into user(user_id,name,city,phone_number,item_bought) values('{}','{}','{}',{},'NULL')".format(u,n,c,z)
                c1.execute(query)
                con.commit()
                print("USER CODE SUCCESSFULLY ADDED")
                cont()


    elif ch2==2:
        print("WELCOME TO EMPLOYEE ACCOUNT REGISTRATION")
        u1=int(input("ENTER A EMPLOYEE ID:"))
        c1.execute("select emp_code from employee")
        hat1=c1.fetchall()
        h21=list(hat1)
        for i in range(len(h21)):
            if h21[i]==u1:
                print("Employee ID already exists")




            else:
                n1=input("ENTER YOUR NAME:")
                c1=input("ENTER YOUR CITY:")
                z1=int(input("ENTER YOUR PHONE NUMBER:"))
                d=input("ENTER YOUR DESIGNATION:")
                query1="insert into employee(emp_code,name,city,phone number,designation) values({},'{}','{}',{},'{}')".format(u1,n1,c1,z1,d)
                c1.execute(query1)
                con.commit()
                newEmpCode = c
                print("EMPLOYEE CODE SUCCESSFULLY ADDED")
                print("1.CHECK ORDER")
                print("2.ADD ANOTHER EMPLOYEE")
                print("3.EXIT")
                ch4=int(input("ENTER YOUR CHOICE:"))

                if ch4==1:
                    order()
                elif ch4==2:
                    create()
                else:
                    break

#CALLING CONTINUE FUNCTION
def cont():
    print("1.CONTINUE SHOPPING")
    print("2.EXIT")
    ch3=int(input("ENTER YOUR CHOICE:"))
    if ch3==1:
        buy()
    else:
        print("Thank you")
        print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
        print("==============================================================================")
        main()
#END OF USER LOGIN
                  