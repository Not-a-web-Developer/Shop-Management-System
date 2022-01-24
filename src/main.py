from logging import root
import mysql.connector as c
import datetime

print("Initialising app...")
print("Logging into the database...")
sql_usrnm = input("MySQL Username: ")
sql_pw = input("MySQL password: ")

con=c.connect(user=sql_usrnm, password=sql_pw, host="localhost", database="EventManagementSystem")
print("connection succeeded!")
c1=con.cursor()

#FUNCTION FOR SIGN IN
def sn():
    print("1.EMPLOYEE LOGIN ")
    print("2.USER LOGIN")
    print("3.EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        code=int(input("ENTER YOUR USER CODE:"))
        c1.execute("select user_id from user")
        dat=c1.fetchall()
        hi=list(dat)
        for i in range(len(hi)):
            if hi[i]==code:
                print("USER ID SUCCESSFULLY FOUND")
                


        
#FUNTION FOR CREATING USER ACCOUNT
def create():
    print("1.USER ACCOUNT")
    print("2.EMPLOYEE ACCCOUNT")
    print("3.EXIT")
    ch2=int(input("Enter Your Choice:"))
    if ch2==1:
        print("WELCOME TO USER ACCOUNT REGISTRATION")
        u=input("ENTER A USER ID:")
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
#END OF USER REGISTRATION

# FOR CREATING EMPLOYEE ACCOUNT
    elif ch2==2:
        print("WELCOME TO EMPLOYEE ACCOUNT REGISTRATION")
        u1=int(input("ENTER A EMPLOYEE ID:"))
        c1.execute("select emp_code from employee")
        hat1=c1.fetchall()
        h21=list(hat1)
        for i in range(len(h21)):
            if h21[i]==u1:
                print("EMPLOYEE CODE ALREADY EXISTS")




            else:
                n1=input("ENTER YOUR NAME:")
                c1=input("ENTER YOUR CITY:")
                z1=int(input("ENTER YOUR PHONE NUMBER:"))
                d=input("ENTER YOUR DESIGNATION:")
                query1="insert into employee(emp_code,name,city,phone number,designation) values({},'{}','{}',{},'{}')".format(u1,n1,c1,z1,d)
                c1.execute(query1)
                con.commit()
                print("EMPLOYEE CODE SUCCESSFULLY ADDED")

                cont1()
#END OF EMPLOYEE REGISTRATION

#CALLING CONTINUE FUNCTION(FOR EMPLOYEE)
def cont1():
    print("1.CHECK ORDER")
    print("2.EXIT")
    ch4=int(input("ENTER YOUR CHOICE:"))

    if ch4==1:
        order()
    else:
        main()

#CALLING CONTINUE FUNCTION(FOR USER)
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

def main():
    print('WELECOME TO SSA Electronics Shop Management System ')
    ch=int(input("Press 1 to continue"))
    if ch==1:
        print('1.SIGN IN')
        print('2.CREATE ACCOUNT')
        print('3.DELETE ACCOUNT')
        print('4.VIEW DETAILS')
        print('5.EXIT')
        ch1=print("Select the option you want:")
        if ch1==1:
            sn()
        if ch1==2:
            create()

main()