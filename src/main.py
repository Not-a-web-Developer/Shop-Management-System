from logging import root
import mysql.connector as c
import datetime
import time
import utils

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
        code=int(input("ENTER YOUR USER ID:"))
        c1.execute("select user_id from user")
        dat=c1.fetchall()
        hi=list(dat)
        for i in range(len(hi)):
            if hi[i]==code:
                print("USER ID SUCCESSFULLY FOUND")
                print("TAKING YOU TO PRODUCTS SECTION...")
                print("HERE IS THE LIST OF PRODUCTS...")
                buy()
            
            else:
                print("NO SUCH USER ID FOUND")
                print("PLS CREATE AN ACCOUNT")
                create()


    elif choice==2:
        code1=int(input("ENTER EMPLOYEE ID:"))
        c1.execute("select employee_id from employee")
        dat1=c1.fetchall()
        hi1=list(dat1)
        for i in range(len(hi1)):
            if hi1[i]==code1:
                print("EMPLOYEE ID SUCCESSFULLY FOUND")
                pwd=input("ENTER YOUR PASSWORD:")
                c1.execute("select pswd from employee")
                dat2=c1.fetchall()
                hi2=list(dat2)
                for i in range(len(hi2)):
                    if hi2[i]==pwd:
                        print("EMPLOYEE SUCCESSFULLY LOGGED IN!")
                        order()
                    
                    else:
                        print("TRY AGAIN")
                        sn()        #DOUBT!!!


            else:
                print("NO SUCH ID FOUND")
                sn()            
                


        
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
                print("EMPLOYEE ID ALREADY EXISTS")
                print("TAKING YOU TO SIGN IN PAGE")
                sn()




            else:
                n1=input("ENTER YOUR NAME:")
                c1=input("ENTER YOUR CITY:")
                z1=int(input("ENTER YOUR PHONE NUMBER:"))
                d=input("ENTER YOUR DESIGNATION:")
                pwd1=input("ENTER YOUR PASSWORD:")
                query1="insert into employee(emp_code,name,city,phone number,designation,pswd) values({},'{}','{}',{},'{}','{}')".format(u1,n1,c1,z1,d,pwd1)
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


#DELETE FUNCTION(FOR USER)

def delt():
    print("CHOOSE WHICH ACCOUNT YOU WANT TO DELETE:")
    print("1.USER ACCOUNT")
    print("2.EMPLOYEE ACCOUNT")
    print("3.EXIT")
    ch5=int(input("ENTER YOUR CHOICE:"))
    if ch5==1:
        f=int(input("ENTER THE USER ID TO BE DELETED:"))
        c1.execute("select user_id from user")
        hat1=c1.fetchall()
        h3=list(hat1)
        for i in range(len(h3)):
            if h3[i]==f:
                pwd1=input("ENTER YOUR PASSWORD:")
                c1.execute("select pswd from user")
                hat2=c1.fetchall()
                h4=list(hat2)
                for i in range(len(h4)):
                    if h4[i]==pwd1:
                        print("ACCOUNT ACCESSED")
                        g=int(input("ARE YOU SURE ABOUT DELETING YOUR ACCOUNT:"))
                        print("1.YES")
                        print("2.NO")
                        if g==1:
                            c1.execute("delete from user where user_id={}".format(f))
                            con.commit()
                            print("USER ID SUCCESSFULLY DELETED!")
                            print("THANK YOU FOR BEING WITH US")
                            main()

                    else:
                        print("SORRY WRONG PASSWROD")
                        print("PLS TRY AGAIN")
                        main()

            else:
                print("USER ID DOES NOT EXISTS")
                print("PLS TRY AGAIN")
                main()


#DELETE(FOR EMPLOYEE)
    if ch5==2:
        h=int(input("ENTER THE EMPLOYEE TO BE DELETED:"))
        c1.execute("select employee_id from employee")
        hat3=c1.fetchall()
        h5=list(hat3)
        for i in range(len(h5)):
            if h5[i]==h:
                pwd2=input("ENTER YOUR PASSWORD:")
                c1.execute("select pswd from employee")
                hat4=c1.fetchall()
                h6=list(hat4)
                for i in range(len(h6)):
                    if h6[i]==pwd2:
                        print("ACCOUNT ACCESSED")
                        g1=int(input("ARE YOU SURE ABOUT DELETING YOUR ACCOUNT:"))
                        print("1.YES")
                        print("2.NO")
                        if g1==1:
                            c1.execute("delete from employee where employee_id={}".format(h))
                            con.commit()
                            print("EMPLOYEE ID SUCCESSFULLY DELETED!")
                            print("THANK YOU FOR YOUR SERVICES")
                            main()

    else:
        print("TAKING YOU TO MAIN PAGE")
        main()


def buy():
    print("WELCOME TO BUYING SECTION")
    print("HERE ARE COMPANIES OF MOBILE PHONES AVAILABLE:")
    c1.execute("select company from products")
    hat4=c1.fetchall()
    b=list(hat4)
    print(b)
    b1=input("ENTER YOUR PREFERRED COMPANY:")
    for i in range(len(b)):
        if b[i]==b1:
            print("HERE IS THE LIST OF VARIOUS MOBILE PHONE AVAILABLE OF THIS COMPANY:")
            c1.execute("select phone,price from products where company=='b1'")     #DOUBT
            hat5=c1.fetchall()
            a=list(hat5)
                

    















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
        if ch1==3:
            delt()

main()


