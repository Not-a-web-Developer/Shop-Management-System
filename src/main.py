from logging import root
import mysql.connector as c
import datetime
import time
import utils

print("Initialising app...")
print("Logging into the database...")
sql_usrnm = input("MySQL Username: ")
sql_pw = input("MySQL password: ")

con = c.connect(user=sql_usrnm, password=sql_pw, host="localhost", database="Shop")
c1 = con.cursor()

print("Successfully logged in!")
time.sleep(.69)

utils.cls()

# function for logging in
def sn():
    print("1. Employee Login ")
    print("2. User Login")
    print("3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        code=int(input("Enter your User ID: "))
        c1.execute("select user_id from user")
        dat=c1.fetchall()
        hi=list(dat)
        for i in range(len(hi)):
            if hi[i]==code:
                print("User ID successfully found! Logging in...")
                


        
# function for user account generation
def create():
    print("1. User Account")
    print("2. Employee Account")
    print("3. Exit")
    ch2=int(input("Enter your choice: "))
    if ch2==1:
        print("User Account Registration")
        u=input("Enter your User ID: ")
        c1.execute("select user_id from user")
        hat=c1.fetchall()
        h2=list(hat)
        for i in range(len(h2)):
            if h2[i]==u:
                print("USER ID already exists, please log in.")



            else:
                n=input("ENTER YOUR NAME:")
                c=input("ENTER YOUR CITY:")
                z=int(input("ENTER YOUR PHONE NUMBER:"))
                query="insert into user(user_id,name,city,phone_number,item_bought) values('{}','{}','{}',{},'NULL')".format(u,n,c,z)
                c1.execute(query)
                con.commit()
                print("USER CODE SUCCESSFULLY ADDED")
                cont()
# end of user account generation

# function for employee account generation
    elif ch2==2:
        print("Employee Account Registration")
        u1=int(input("Enter your Employee ID: "))
        c1.execute("select emp_code from employee")
        hat1=c1.fetchall()
        h21=list(hat1)
        for i in range(len(h21)):
            if h21[i]==u1:
                print("Employee ID already exists, please log in.")




            else:
                n1=input("ENTER YOUR NAME: ")
                c1=input("ENTER YOUR CITY: ")
                z1=int(input("ENTER YOUR PHONE NUMBER: "))
                d=input("ENTER YOUR DESIGNATION: ")
                query1="insert into employee(emp_code,name,city,phone number,designation) values({},'{}','{}',{},'{}')".format(u1,n1,c1,z1,d)
                c1.execute(query1)
                con.commit()
                newEmpCode = c
                print("EMPLOYEE CODE SUCCESSFULLY ADDED")

                cont1()
# end of employee account generation

# you wanna continue? (for employees)
def cont1():
    print("1. Check orders")
    print("2. Exit")
    ch4=int(input("Enter your choice: "))

    if ch4==1:
        order()
    else:
        main()

# you wanna continue? (for users)
def cont():
    print("1. Continue shopping")
    print("2. Exist")
    ch3=int(input("Enter your choice: "))
    if ch3==1:
        buy()
    else:
        print("==============================================================================")
        print("Thanks for coming to The Shop! ")
        print("==============================================================================")
        main()

def main():
    print('Welcome to The Shop! ')
    print("==============================================================================\n\n")
    print('1. Login')
    print('2. Create Account')
    print('3. delete Account')
    print('4. View Details') # tf is this supposed to do
    print('5. Exit')
    ch1=int(input("Select the option you want: "))
    if ch1==1:
        sn()
    if ch1==2:
        create()

main()