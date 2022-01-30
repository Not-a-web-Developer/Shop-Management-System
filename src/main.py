from logging import root
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
c1=con.cursor()

#FUNCTION FOR SIGN IN
def sn():
    print("1. User login ")
    print("2. Employee login")
    print("3. EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        c1.execute("select user_id from user")
        dat=c1.fetchall()
        code=int(input("ENTER YOUR USER ID:"))
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
                        main()        #DOUBT!!!


            else:
                print("NO SUCH ID FOUND")
                main()            
                



#FUNTION FOR CREATING USER ACCOUNT
def create():
    c1=con.cursor()
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
                o1=input("DO YOU WANT TO MAKE OTHER ID(Y/N)?")
                if o1=="y" or "Y":
                    cont3()
                else:
                    ("TAKING YOU TO MAIN PAGE")
                    main()



            else:
                o=input("ENTER YOUR PASSWORD:")
                n=input("ENTER YOUR NAME:")
                c=input("ENTER YOUR CITY:")
                z=int(input("ENTER YOUR PHONE NUMBER:"))
                query="insert into user(user_id,pwd,name,city,phone_number,item_bought) values({},'{}','{}','{}',{},NULL)".format(u,o,n,c,z)
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
        print("THANK YOU")
        print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
        print("==============================================================================")
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
    b1=input("0ENTER YOUR PREFERRED COMPANY:")
    for i in range(len(b)):
        if b[i]==b1:
            print("HERE IS THE LIST OF VARIOUS MOBILE PHONE AVAILABLE OF THIS COMPANY:")
            st="select product_id,phone,price from products where company='{}'".format(b1)
            c1.execute(st)     #DOUBT
            hat5=c1.fetchall()
            a=list(hat5)
            print(a)
            a1=int(input("SELECT THE PHONE YOU LIKED FOR ITS CONFIGURATION:"))
            for i in range(len(a1)):
                if a1[i][0]==a1:
                    print("THE CONFIGURATIONS ARE:")
                    c1.execute("select product_id,company,phone,price,config from products where sr_no={}".format(a1))
                    hat5=c1.fetchall()
                    a2=list(hat5)
                    z1=print("PHONE:",a2[2])
                    z2=print("PRICE:",a2[3])
                    z3=print("ITS CONFIGURATION ARE:",a2[4])
                    a4=input("DO YOU WANT TO BUY THIS PHONE(Y/N)?:")
                    if a4=="y" or "Y":
                        query2="insert into order(product_id,company,phone,price,config) values({},'{}','{}',{},'{})".format(a1,b1,z1,z2,z3)
                        c1.execute(query2)
                        con.commit()
                        print("TRANSACTION DONE SUCCESSFULLY")
                        print("CONGRATULATIONS THE PHONE IS YOURS!")
                        a6=input("DO YOU WANT TO SEE ANOTHER PHONE(Y/N):")            #NEED TO ADD PRODUCT TO USER DETAILS
                        if a6=="y" or "Y":
                            cont2()
                        else:   
                            print("THANK YOU")
                            print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                            print("==============================================================================")
                            main()

                    else:
                        a5=input("DO YOU WANT TO SEE ANOTHER PHONE(Y/N):")
                        if a5=="y" or "Y":
                            cont2()                               
                        else:
                            print("THANK YOU")
                            print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                            print("==============================================================================")
                            main()


                
                else:
                    print("NO SUCH SR_NO")
                    print("TRY AGAIN")
                    cont2()

    
        else:
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
    p1=int(input("ENTER THE PRODUCT ID:"))
    c1.execute("select product_id from order")
    t1=c1.fetchall()
    u1=list(t1)
    for i in range(len(u1)):
        if u1[i]==p1:
            c1.execute("delete from order where product_id='{}'".format(p1))
            con.commit()
            c1.execute("select product_id,qty from products where product_id={}".format(p1))
            t2=c1.fetchall()
            u2=list(t2)
            if u2[2]==0:
                print("THIS PRODUCT IS OUT OF STOCK")


            else:
                p2=u2[1]-1
                c1.execute("insert into products(qty) values({})".format(p2))      #DOUBT
                con.commit()
                    
                    




def details():
    print("1.USER ACCOUNT")
    print("2.EMPLOYEE ACCOUNT")
    print("3.EXIT")
    ch10=int(input("ENTER YOUR CHOICE:"))
    if ch10==1:
        v1=int(input("ENTER YOUR USER ID:"))
        c1.execute("select user_id from user")
        x1=c1.fetchall()
        y1=list(x1)
        for i in range(len(y1)):
            if y1[i]==v1:
                v2=input("ENTER YOUR PASSWORD:")
                c1.execute("select pwd from user")
                x2=c1.fetchall()
                y2=list(x2)
                for i in range(len(y2)):
                    if y2[i]==v2:
                        print("ACCOUNT ACCESSED!")
                        print("HERE ARE THE DETAILS OF YOUR ACCOUNT")
                        c1.execute("select user_id,pwd,name,city,phone_number,item_bought where user_id={}".format(v1))
                        x3=c1.fetchall()
                        y3=list(x3)
                        print("USER ID:",y3[0])
                        print("PASSWORD:",y3[1])
                        print("NAME",y3[2])
                        print("CITY",y3[3])
                        print("PHONE NUMBER",y3[4])
                        print("ITEM BOUGHT",y3[5])
                        v3=input("DO YOU WANT TO CHANGE ANY OF YOUR DETAILS(EXCEPT USER ID AND ITEM BOUGHT)(Y/N)?")
                        if v3=="y" or "Y":
                            z4=input("WHICH DETAIL YOU WANT TO CHANGE?")
                            if z4==2:
                                g1=input("ENTER YOUR NEW PASSWORD:")
                                query5="update user set pwd= %s where user_id= %s"
                                val=(v1,g1)
                                c1.execute(query5,val)                       #DOUBT
                                con.commit()

                                


                            





                        else:
                            print("THANK YOU")
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
        ch1=int(input("Select the option you want:"))
        if ch1==1:
            sn()
        elif ch1==2:
            create()
        elif ch1==3:
            delt()
        elif ch1==4:
            details()
        else:
            print("invalid choice mf")

main()


