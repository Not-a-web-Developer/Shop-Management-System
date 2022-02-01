from logging import root
from multiprocessing.managers import ValueProxy
import mysql.connector
import datetime
import time
import utils

print("Initialising app...")
print("Logging into the database...")
sql_usrnm = input("MySQL Username: ")
sql_pw = input("MySQL password: ")

con=mysql.connector.connect(user=sql_usrnm, password=sql_pw, host="localhost", database="Shop")
print("connection succeeded!")
time.sleep(0.42)
utils.cls()
c1=con.cursor()

#FUNCTION FOR SIGN IN
def sn():
    print("1. USER LOGIN ")
    print("2. EMPLOYEE LOGIN")
    print("3. EXIT")
    choice=int(input("ENTER YOUR CHOICE: "))
    if choice==1:
        global code
        c1.execute("select user_id from user")
        dat=c1.fetchall()
        code=int(input("ENTER YOUR USER ID: "))
        hi=list(dat)
        for i in range(0, len(hi)):
            if hi[i]==(code,):
                print("USER ID SUCCESSFULLY FOUND")
                c1.execute("select pwd from user where user_id = %s", (code,))
                dat10=c1.fetchall()
                code1=input("ENTER YOUR PASSWORD:")
                hj=list(dat10)
                for i in range(len(hj)):
                    if hj[i]==(code1,):
                        print("ACCOUNT ACCESSED")
                        print("TAKING YOU TO PRODUCTS SECTION...")
                        buy()
                    
                    else:
                        continue
                print("INCORRECT PASSWORD")
                print("TRY AGAIN")
                main()
            
            else:
                continue
        print("NO SUCH USER ID FOUND")
        print("PLS CREATE AN ACCOUNT")
        create()


    elif choice==2:
        code1=int(input("ENTER EMPLOYEE ID: "))
        c1.execute("select emp_id from employee")
        dat1=c1.fetchall()
        hi1=list(dat1)
        for i in range(len(hi1)):
            if hi1[i]==(code1,):
                print("EMPLOYEE ID SUCCESSFULLY FOUND")
                pwd=input("ENTER YOUR PASSWORD: ")
                c1.execute("select pwd from employee")
                dat2=c1.fetchall()
                hi2=list(dat2)
                for i in range(len(hi2)):
                    if hi2[i]==(pwd,):
                        print("EMPLOYEE SUCCESSFULLY LOGGED IN!")
                        order()
                    
                    else:
                        continue
                print("WRONG PASSWORD")    
                print("TRY AGAIN!!")
                main()       


            else:
                continue
        print("NO SUCH ID FOUND")
        print("TRY AGAIN")
        main() 

    else:
        print("TAKING YOU TO MAIN SECTION")
        main()           
                



#FUNTION FOR CREATING USER ACCOUNT
def create():
    c1=con.cursor()
    print("1.USER ACCOUNT")
    print("2.EMPLOYEE ACCCOUNT")
    print("3.EXIT")
    ch2=int(input("ENTER YOUR CHOICE: "))
    if ch2==1:
        print("WELCOME TO USER ACCOUNT REGISTRATION")
        u=input("ENTER A USER ID: ")
        c1.execute("select user_id from user")
        hat=c1.fetchall()
        h2=list(hat)
        print(h2)
        for i in range(len(h2)):              #PROBLEM!!!
            print(h2[i][0])
            if h2[i][0]==u:
                print("USER ID ALREADY EXITS")
                o1=input("DO YOU WANT TO MAKE OTHER ID(Y/N)?")
                if o1=="y":
                    cont3()
                else:
                    ("TAKING YOU TO MAIN PAGE")
                    main()



            else:
                continue
        o=input("ENTER YOUR PASSWORD:")
        n=input("ENTER YOUR NAME:")
        c=input("ENTER YOUR CITY:")
        z=int(input("ENTER YOUR PHONE NUMBER:"))
        query="insert into user(user_id,pwd,name,city,phone_number,item_bought) values({},'{}','{}','{}',{},0)".format(u,o,n,c,z)
        c1.execute(query)
        con.commit()
        print("USER CODE SUCCESSFULLY ADDED")
        print("TAKING YOU TO SIGN IN PAGE")
        sn()
#END OF USER REGISTRATION

# FOR CREATING EMPLOYEE ACCOUNT
    elif ch2==2:
        print("WELCOME TO EMPLOYEE ACCOUNT REGISTRATION")
        u1=int(input("ENTER A EMPLOYEE ID:"))
        c1.execute("select emp_id from employee")
        hat1=c1.fetchall()
        h21=list(hat1)
        for i in range(len(h21)):
            if h21[i]==(u1,):
                print("EMPLOYEE ID ALREADY EXISTS")
                print("TAKING YOU TO SIGN IN PAGE")
                sn()

            else:
                continue
        n1=input("ENTER YOUR NAME:")
        c1=input("ENTER YOUR CITY:")
        z1=int(input("ENTER YOUR PHONE NUMBER:"))
        d=input("ENTER YOUR DESIGNATION:")
        pwd1=input("ENTER YOUR PASSWORD:")
        query1="insert into employee(emp_code,pwd,name,city,phone number,designation) values({},'{}','{}','{}',{},'{}')".format(u1,pwd1,n1,c1,z1,d)
        c1.execute(query1)
        con.commit()
        print("EMPLOYEE CODE SUCCESSFULLY ADDED")
        cont1()
#END OF EMPLOYEE REGISTRATION

    else:
        print("TAKING YOU TO MAIN PAGE")
        main()


#CALLING CONTINUE FUNCTION(FOR EMPLOYEE)
def cont1():
    print("1.CHECK ORDER")
    print("2.EXIT")
    ch4=int(input("ENTER YOUR CHOICE:"))

    if ch4==1:
        order()
    else:
        main()


def cont3():
    print("TAKING YOU TO CREATE ACCOUNT SECTION")
    create()


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
            if h3[i]==(f,):
                pwd1=input("ENTER YOUR PASSWORD:")
                c1.execute("select pwd from user")
                hat2=c1.fetchall()
                h4=list(hat2)
                for i in range(len(h4)):
                    if h4[i]==(pwd1,):
                        print("ACCOUNT ACCESSED")
                        g=input("ARE YOU SURE ABOUT DELETING YOUR ACCOUNT(Y/N): ")
                        if g=="y":
                            c1.execute("delete from user where user_id='{}'".format(f))
                            con.commit()
                            print("USER ID SUCCESSFULLY DELETED!")
                            print("THANK YOU FOR BEING WITH US")
                            main()
                        
                        else:
                            print("TAKING YOU TO MAIN PAGE")
                            main()

                    else:
                        continue
                        print("SORRY WRONG PASSWROD")
                        print("PLS TRY AGAIN")
                        main()

            else:
                continue
                print("USER ID DOES NOT EXISTS")
                print("PLS TRY AGAIN")
                main()


#DELETE(FOR EMPLOYEE)
    if ch5==2:
        h=int(input("ENTER THE EMPLOYEE TO BE DELETED:"))
        c1.execute("select emp_id from employee")
        hat3=c1.fetchall()
        h5=list(hat3)
        for i in range(len(h5)):
            if h5[i]==h:
                pwd2=input("ENTER YOUR PASSWORD:")
                c1.execute("select pwd from employee")
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
    c1.execute("select distinct company from products")
    hat4=c1.fetchall()
    b=list(hat4)
    print(b)
    b1=input("ENTER YOUR PREFERRED COMPANY:")
    for i in range(len(b)):
       
        if b[i]==(b1,):
            print("HERE IS THE LIST OF VARIOUS MOBILE PHONE AVAILABLE OF THIS COMPANY:")
            st="select product_id,phone,price from products where company='{}'".format(b1)
            c1.execute(st)
            hat5=c1.fetchall()
            a=list(hat5)
            for i in range(len(a)):
                print(a[i])
            
            a1=int(input("SELECT A PHONE TO VIEW ITS CONFIGURATION(ENTER PRODUCT ID):"))
            for i in range(len(a)):
                if a[i][0]==a1:
                    print("THE CONFIGURATIONS ARE:")
                    c1.execute("select product_id,company,phone,price,config,qty from products where product_id=%s", (a1,))
                    hat5=c1.fetchall()
                    a2=list(hat5)
                    z1=print("PHONE: ",a2[0][2])
                    z2=print("PRICE: ",a2[0][3])
                    z3=print("ITS CONFIGURATION ARE: ",a2[0][4])
                    z4=print("NO. OF PIECES AVAILABLE OF THIS PHONE: ",a2[0][5])
                    if a2[0][5]==0:
                        print("SORRY THE GIVEN PHONE IS OUT OF STOCK")
                        a8=input("DO YOU WANT TO SEE ANOTHER PHONE(Y/N):")
                        if a8=="y":
                            cont2()                               
                        else:
                            print("THANK YOU")
                            print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                            print("==============================================================================")
                            main()
                    else:
                        a4=input("DO YOU WANT TO BUY THIS PHONE(Y/N)?:")
                        if a4=="y":                    
                            query_1="insert into orders(transaction_id,product_id,company,phone,price,config,updated) values(%s, %s, %s, %s, %s, %s, %s)"
                            record=(utils.generate_unique_id(),a1, b1, a2[0][2], a2[0][3], a2[0][4],"no")
                            c1.execute(query_1,record)
                            con.commit()
                            c1.execute("select item_bought from user where user_id=%s",(code,))
                            val5=c1.fetchall()
                            lst=list(val5)
                            record1=lst[0][0]
                            record1 +=1
                            query9="update user set item_bought= %s where user_id= %s"
                            val6=(record1,code)
                            c1.execute(query9,val6)  
                            con.commit()
                            print("PHONE ADDED TO YOUR ACCOUNT")
                            print("TRANSACTION DONE SUCCESSFULLY")
                            print("CONGRATULATIONS THE PHONE IS YOURS!")
                            a6=input("DO YOU WANT TO SEE ANOTHER PHONE(Y/N):")            #NEED TO ADD PRODUCT TO USER DETAILS
                            if a6=="y":
                                cont2()
                            else:   
                                print("THANK YOU")
                                print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                                print("==============================================================================")
                                main()

                        else:
                            a5=input("DO YOU WANT TO SEE ANOTHER PHONE(Y/N):")
                            if a5=="y":
                                cont2()                               
                            else:
                                print("THANK YOU")
                                print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                                print("==============================================================================")
                                main()


                else:
                    continue
            print("NO SUCH PRODUCT ID")
            print("TRY AGAIN")
            cont2()

    
        else:
            continue
    print("SORRY THE GIVEN COMPANY IS NOT IN OUR STORE")
    a7=input("DO YOU WANT TO SEE ANOTHER PHONE(Y/N):")
    if a7=="y" or "Y":
        cont2()
    else:
        print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
        print("==============================================================================")
        main()


                
def cont2():
    print("TAKING YOU TO BUYING SECTION....")
    buy()



def order():
    print("WELCOME TO THE SECTION")
    p1=int(input("ENTER THE PRODUCT ID: "))
    c1.execute("select product_id from orders where product_id=%s and updated=%s",(p1,"no"))
    t1=c1.fetchall()
    up1=list(t1)
    record2=len(up1)
    c1.execute("select qty from products where product_id=%s",(p1,))
    record3=c1.fetchall()
    lst1=list(record3)
    record4=lst1[0][0]-record2
    query10="update products set qty=%s where product_id=%s"
    record5=(record4,p1)
    c1.execute(query10,record5)
    con.commit()
    print("UPDATED THE PRODUCTS SECTION")
    query11="update orders set updated=%s where product_id=%s"
    record6=("yes",p1)
    c1.execute(query11,record6)
    con.commit()
    print("UPDATED THE ORDERS SECTION")
    main()


    
def details():
    print("1.USER ACCOUNT")
    print("2.EXIT")
    ch10=int(input("ENTER YOUR CHOICE:"))
    if ch10==1:
        v1=int(input("ENTER YOUR USER ID:"))
        c1.execute("select user_id from user")
        x1=c1.fetchall()
        y1=list(x1)
        for i in range(len(y1)):
            if y1[i]==(v1,):
                v2=input("ENTER YOUR PASSWORD:")
                c1.execute("select pwd from user")
                x2=c1.fetchall()
                y2=list(x2)
                for i in range(len(y2)):
                    if y2[i]==(v2,):
                        print("ACCOUNT ACCESSED!")
                        print("HERE ARE THE DETAILS OF YOUR ACCOUNT")
                        c1.execute("select user_id,pwd,name,city,phone_number,item_bought from user where user_id=%s",(v1,))
                        x3=c1.fetchall()
                        y3=list(x3)
                        print("1.USER ID: ",y3[0][0])
                        print("2.PASSWORD: ",y3[0][1])
                        print("3.NAME: ",y3[0][2])
                        print("4.CITY: ",y3[0][3])
                        print("5.PHONE NUMBER: ",y3[0][4])
                        print("6.ITEM BOUGHT: ",y3[0][5])
                        v3=input("DO YOU WANT TO CHANGE ANY OF YOUR DETAILS(EXCEPT USER ID AND ITEM BOUGHT)(Y/N)?")
                        if v3=='y':
                            z4=int(input("WHICH DETAIL YOU WANT TO CHANGE?(ENTER THE SR.NO): "))
                            if z4==2:
                                g1=input("ENTER YOUR NEW PASSWORD: ")
                                query5="update user set pwd= %s where user_id= %s"
                                val1=(g1,v1)
                                c1.execute(query5,val1)                   
                                con.commit()
                                print("PASSWORD SUCCESSFULLY CHANGED!")
                                print("THANK YOU")
                                main()
                            elif z4==3:
                                g2=input("ENTER YOUR NEW NAME: ")
                                query6="update user set name= %s where user_id=%s"
                                val2=(g2,v1)
                                c1.execute(query6,val2)
                                con.commit()
                                print("NAME SUCCESSFULLY CHANGED!")
                                print("THANK YOU")
                                main()
                            elif z4==4:
                                g3=input("ENTER YOUR NEW CITY: ")
                                query7="update user set city= %s where user_id=%s"
                                val3=(g3,v1)
                                c1.execute(query7,val3)
                                con.commit()
                                print("CITY SUCCESSFULLY CHANGED!")
                                print("THANK YOU")
                                main()
                            elif z4==5:
                                g4=input("ENTER YOUR NEW CITY: ")
                                query8="update user set phone_number= %s where user_id=%s"
                                val4=(g4,v1)
                                c1.execute(query8,val4)
                                con.commit()
                                print("PHONE NO SUCCESSFULLY CHANGED!")
                                print("THANK YOU")
                                main()
                            else:
                                print("INVALID CHOICE!!!")
                                main()

                        else:
                            print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                            print("==============================================================================")
                            main()

                    else:
                        continue
                print("WRONG PASSWORD")
                print("TRY AGAIN")
                cont4()

            else:
                continue
        print("INVALID USER ID!!!")
        print("TRY AGAIN")
        cont4()

    else:
        print("TAKING YOU TO MAIN SECTION")
        main()
                            

def cont4():
    print("TAKING YOU TO VIEW DETAILS SECTION: ")
    details()


def main():
    print('WELCOME TO   ')
    ch=int(input("PRESS 1 TO CONTINUE "))
    if ch==1:
        print('1.SIGN IN')
        print('2.CREATE ACCOUNT')
        print('3.DELETE ACCOUNT')
        print('4.VIEW DETAILS')
        print('5.EXIT')
        ch1=int(input("SELECT THE OPTION YOU WANT(SR NO): "))
        if ch1==1:
            sn()
        elif ch1==2:
            create()
        elif ch1==3:
            delt()
        elif ch1==4:
            details()
        else:
            print("INVALID CHOICE!!!")

    else:
        print("INVALID ENTRY")        

main()


