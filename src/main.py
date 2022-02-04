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
time.sleep(0.50)
utils.cls()
c1=con.cursor()

#FUNCTION FOR SIGN IN
def sn():
    print("1. User Login ")
    print("2. Employee login ")
    print("3. Exit\n")
    choice=int(input("Enter your choice (serial no.): "))
    if choice==1:
        global code
        c1.execute("select user_id from user")
        dat=c1.fetchall()
        code=int(input("Enter your user ID: "))
        hi=list(dat)
        for i in range(0, len(hi)):
            if hi[i]==(code,):
                print("User ID found")
                c1.execute("select pwd from user where user_id = %s", (code,))
                dat10=c1.fetchall()
                code1=input("Enter your password: ")
                hj=list(dat10)
                for i in range(len(hj)):
                    if hj[i]==(code1,):
                        print("Account Accessed!")
                        time.sleep(0.420)
                        print("Taking you to the products section... ")
                        time.sleep(0.70)
                        utils.cls()
                        buy()
                    
                    else:
                        continue
                print("Error: incorrect password")    
                print("Please try again")
                time.sleep(0.7)
                utils.cls()
                main()
            
            else:
                continue
        print("Error: No such user ID found")
        print("please create an account")
        time.sleep(0.70)
        utils.cls()
        create()


    elif choice==2:
        code1=int(input("Enter employee ID: "))
        c1.execute("select emp_id from employee")
        dat1=c1.fetchall()
        hi1=list(dat1)
        for i in range(len(hi1)):
            if hi1[i]==(code1,):
                print("Employee ID found")
                time.sleep(0.4)
                pwd=input("Enter your password: ")
                c1.execute("select pwd from employee")
                dat2=c1.fetchall()
                hi2=list(dat2)
                for i in range(len(hi2)):
                    if hi2[i]==(pwd,):
                        print("Employee successfully logged in!")
                        time.sleep(0.70)
                        utils.cls()
                        order()
                    
                    else:
                        continue
                print("Error: incorrect password")    
                print("Please try again")
                time.sleep(0.7)
                utils.cls()
                main()       


            else:
                continue
        print("Error: No such employee ID found")
        print("Please try again")
        time.sleep(0.7)
        utils.cls()
        main() 

    else:
        print("Taking you to the main menu... ")
        time.sleep(0.69)
        utils.cls()
        main()           
                



#FUNTION FOR CREATING USER ACCOUNT
def create():
    c1=con.cursor()
    print("1. User account")
    print("2. Employee account")
    print("3. Exit\n")
    ch2=int(input("Enter your choice (serial no.): "))
    if ch2==1:
        print("User Account Registration")
        u=int(input("Enter a user ID (should be a 5 digit number): "))
        c1.execute("select user_id from user")
        hat=c1.fetchall()
        h2=list(hat)
        for i in range(len(h2)):      
            if h2[i][0]==u:
                print("User ID already taken")
                o1=input("Do you want to make another user ID? (y/n)?")
                if o1=="y":
                    cont3()
                else:
                    ("Taking you to the main menu... ")
                    time.sleep(0.70)
                    utils.cls()
                    main()



            else:
                continue
        o=input("Enter your password: ")
        n=input("Enter your name: ")
        c=input("Enter your city: ")
        z=int(input("Enter your phone number: "))
        query="insert into user(user_id,pwd,name,city,phone_number,item_bought) values({},'{}','{}','{}',{},0)".format(u,o,n,c,z)
        c1.execute(query)
        con.commit()
        print("User successfully added")
        print("Taking you to the login page")
        time.sleep(0.70)
        utils.cls()
        sn()
#END OF USER REGISTRATION

# FOR CREATING EMPLOYEE ACCOUNT
    elif ch2==2:
        print("Employee Account Registration\n")
        u1=int(input("Enter an Employee ID: "))
        c1.execute("select emp_id from employee")
        hat1=c1.fetchall()
        h21=list(hat1)
        for i in range(len(h21)):
            if h21[i]==(u1,):
                print("Employee ID already exists")
                print("Taking you to the login page... ")
                time.sleep(0.70)
                utils.cls()
                sn()

            else:
                continue
        n1=input("Enter your name: ")
        c1=input("Enter your city: ")
        z1=int(input("Enter your phone number: "))
        d=input("ENTER YOUR DESIGNATION: ")
        pwd1=input("Enter your password: ")
        query1="insert into employee(emp_code,pwd,name,city,phone number,designation) values({},'{}','{}','{}',{},'{}')".format(u1,pwd1,n1,c1,z1,d)
        c1.execute(query1)
        con.commit()
        print("Employee ID successfully added")
        time.sleep(0.70)
        utils.cls()
        cont1()
#END OF EMPLOYEE REGISTRATION

    else:
        print("Taking you to the main menu... ")
        time.sleep(0.70)
        utils.cls()
        main()


#CALLING CONTINUE FUNCTION(FOR EMPLOYEE)
def cont1():
    print("1. Check order")
    print("2. Exit")
    ch4=int(input("Enter your choice (serial no.): "))

    if ch4==1:
        order()
    else:
        time.sleep(0.70)
        utils.cls()
        main()


def cont3():
    print("Taking you to the Account Management section... ")
    time.sleep(0.70)
    utils.cls()
    create()


#DELETE FUNCTION(FOR USER)

def delt():
    print("Choose which type of account you want to delete: \n")
    print("1. User Account")
    print("2. Employee account")
    print("3. Exit\n")
    ch5=int(input("Enter your choice (serial no.): "))
    if ch5==1:
        f=int(input("Enter the user ID to be deleted: "))
        c1.execute("select user_id from user")
        hat1=c1.fetchall()
        h3=list(hat1)
        for i in range(len(h3)):
            if h3[i]==(f,):
                pwd1=input("Enter your password: ")
                c1.execute("select pwd from user")
                hat2=c1.fetchall()
                h4=list(hat2)
                for i in range(len(h4)):
                    if h4[i]==(pwd1,):
                        time.sleep(0.4)
                        print("Account Accessed!")
                        g=input("Are you sure you want to delete your account? (y/n): ")
                        if g=="y":
                            c1.execute("delete from user where user_id='{}'".format(f))
                            con.commit()
                            print("User ID successfully deleted\n")
                            time.sleep(0.4)
                            print("Thank you for shopping at Digital Vision!")
                            time.sleep(0.70)
                            utils.cls()
                            main()
                        
                        else:
                            print("Taking you to the main menu... ")
                            time.sleep(0.70)
                            utils.cls()
                            main()

                    else:
                        continue
                print("The password is incorrect.")
                print("Please try again")
                time.sleep(0.70)
                utils.cls()
                main()

            else:
                continue
        print("Error: invalid user ID")
        print("Please try again")
        time.sleep(0.70)
        utils.cls()
        main()


#DELETE(FOR EMPLOYEE)
    if ch5==2:
        h=int(input("Enter the employee ID to be deleted: "))
        c1.execute("select emp_id from employee")
        hat3=c1.fetchall()
        h5=list(hat3)
        for i in range(len(h5)):
            if h5[i]==(h,):
                pwd2=input("Enter your password: ")
                c1.execute("select pwd from employee")
                hat4=c1.fetchall()
                h6=list(hat4)
                for i in range(len(h6)):
                    if h6[i]==(pwd2,):
                        time.sleep(0.4)
                        print("Account Accessed!")
                        g1=input("Are you sure you want to delete your account? (y/n): ")
                        if g1=="y":
                            c1.execute("delete from employee where employee_id={}".format(h))
                            con.commit()
                            print("Employee ID successfully deleted\n")
                            time.sleep(0.4)
                            print("Thank you for working at Digital Vision!")
                            time.sleep(0.70)
                            utils.cls()
                            main()
                        
                        else:
                            print("Taking you to the main menu... ")
                            time.sleep(0.70)
                            utils.cls()
                            main()

                    else:
                        continue
                print("The password is incorrect.")
                print("Please try again")
                time.sleep(0.70)
                utils.cls()
                main()

            else:
                continue
        print("Error: invalid employee ID")
        print("Please try again")
        time.sleep(0.70)
        utils.cls()
        main()

    else:
        print("Taking you to the main menu... ")
        time.sleep(0.69)
        utils.cls()
        main()


def buy():
    print("Welcome to the Buying Section!")
    print("Mobile Phone Companies we sell phones of:")
    c1.execute("select distinct company from products")
    hat4=c1.fetchall()
    b=list(hat4)
    for i in range(len(b)):
        print(b[i][0])
    b1=input("Enter your preferred company: ")
    for i in range(len(b)):
        if b[i]==(b1,):
            print("Here is the list of the models we sell from this company: ")
            st="select product_id,phone,price from products where company='{}'".format(b1)
            c1.execute(st)
            hat5=c1.fetchall()
            a=list(hat5)
            for i in range(len(a)):
                print(a[i])
                
            a1=int(input("Enter product ID of the phone you want to see details of: "))
            for i in range(len(a)):
                if a[i][0]==a1:
                    print("The details are: ")
                    c1.execute("select product_id,company,phone,price,config,qty from products where product_id=%s", (a1,))
                    hat5=c1.fetchall()
                    a2=list(hat5)
                    z1=print("Phone: ",a2[0][2])
                    z2=print("Price: ",a2[0][3])
                    z3=print("Its configuration is: ",a2[0][4])
                    z4=print("number of pieces left in stock: ",a2[0][5])
                    if a2[0][5]==0:
                        print("SORRY, the given phone is out of stock.")
                        a8=input("Do you want to see another phone? (y/n): ")
                        if a8=="y":
                            cont2()                               
                        else:
                            print(" Thanks for shopping from Digital Vision!")
                            print("==============================================================================")
                            time.sleep(0.70)
                            utils.cls()
                            main()
                    else:
                        a4=input("Do you want to buy this phone? (y/n): ")
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
                            print("Phone added to your account")
                            time.sleep(0.2)
                            print("Transaction successful")
                            time.sleep(0.4)
                            print("Congratulations, the phone is yours!")
                            time.sleep(1.2)
                            print("Please hand over the terminal to an employee immediately")
                            time.sleep(0.70)
                            utils.cls()
                            sn()

                        else:
                            a5=input("Do you want to see another phone? (y/n): ")
                            if a5=="y":
                                cont2()                               
                            else:
                                print(" Thanks for shopping from Digital Vision!")
                                print("==============================================================================")
                                time.sleep(0.70)
                                utils.cls()
                                main()


                else:
                    continue
            print("Error: Invalid product ID")
            print("Please try again")
            time.sleep(0.4)
            cont2()

        
        else:
            continue
    print("Sorry! We don't sell those phones here.")
    time.sleep(0.4)
    a7=input("Do you want to see another phone? (y/n): ")
    if a7=="y" or "Y":
        cont2()
    else:
        print(" Thanks for shopping from Digital Vision!")
        print("==============================================================================")
        time.sleep(0.70)
        utils.cls()
        main()


                
def cont2():
    print("Taking you to the Buying section... ")
    time.sleep(0.70)
    utils.cls()
    buy()



def order():
    print("Database Management Utility")
    p1=int(input("Enter the product ID to be updated: "))
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
    print("Updated the products section")
    query11="update orders set updated=%s where product_id=%s"
    record6=("yes",p1)
    c1.execute(query11,record6)
    con.commit()
    print("Updated the orders section")
    time.sleep(0.4)
    print("Updation complete! going back to the main menu... ")
    time.sleep(0.70)
    utils.cls()
    main()


    
def details():
    print("1. User account")
    print("2. exit\n")
    ch10=int(input("Enter your choice(serial no.): "))
    if ch10==1:
        v1=int(input("Enter your user ID: "))
        c1.execute("select user_id from user")
        x1=c1.fetchall()
        y1=list(x1)
        for i in range(len(y1)):
            if y1[i]==(v1,):
                v2=input("Enter your password: ")
                c1.execute("select pwd from user")
                x2=c1.fetchall()
                y2=list(x2)
                for i in range(len(y2)):
                    if y2[i]==(v2,):
                        print("Account accessed!")
                        time.sleep(0.7)
                        utils.cls()
                        print("Here are the details of your account\n")
                        c1.execute("select user_id,pwd,name,city,phone_number,item_bought from user where user_id=%s",(v1,))
                        x3=c1.fetchall()
                        y3=list(x3)
                        print("1. User ID: ",y3[0][0])
                        print("2. Password: ",y3[0][1])
                        print("3. Name: ",y3[0][2])
                        print("4. City: ",y3[0][3])
                        print("5. Phone number: ",y3[0][4])
                        print("6. Items bought: ",y3[0][5])
                        v3=input("Do you want to change any of your details?(except user ID and items bought)(y/n)")
                        if v3=='y':
                            z4=int(input("Detail to be changed (serial no.): "))
                            if z4==2:
                                g1=input("Enter your new password: ")
                                query5="update user set pwd= %s where user_id= %s"
                                val1=(g1,v1)
                                c1.execute(query5,val1)                   
                                con.commit()
                                print("Password successfully changed!")
                                time.sleep(0.5)
                                print("Taking you to the main menu... ")
                                time.sleep(0.70)
                                utils.cls()
                                main()
                            elif z4==3:
                                g2=input("Enter your new name: ")
                                query6="update user set name= %s where user_id=%s"
                                val2=(g2,v1)
                                c1.execute(query6,val2)
                                con.commit()
                                print("Name successfully changed!")
                                time.sleep(0.5)
                                print("Taking you to the main menu... ")
                                time.sleep(0.70)
                                utils.cls()
                                main()
                            elif z4==4:
                                g3=input("Enter your new city: ")
                                query7="update user set city= %s where user_id=%s"
                                val3=(g3,v1)
                                c1.execute(query7,val3)
                                con.commit()
                                print("City successfully changed!")
                                time.sleep(0.5)
                                print("Taking you to the main menu... ")
                                time.sleep(0.70)
                                utils.cls()
                                main()
                            elif z4==5:
                                g4=input("Enter your new phone number: ")
                                query8="update user set phone_number= %s where user_id=%s"
                                val4=(g4,v1)
                                c1.execute(query8,val4)
                                con.commit()
                                print("Phone number successfully changed!")
                                time.sleep(0.5)
                                print("Taking you to the main menu... ")
                                time.sleep(0.70)
                                utils.cls()
                                main()
                            else:
                                print("Invalid Choice!")
                                time.sleep(0.5)
                                print("Taking you to the main menu... ")
                                time.sleep(0.70)
                                utils.cls()
                                main()

                        else:
                            print(" Thanks for shopping from Digital Vision!")
                            print("==============================================================================")
                            time.sleep(0.70)
                            utils.cls()
                            main()

                    else:
                        continue
                print("WRONG PASSWORD")
                print("TRY AGAIN")
                cont4()

            else:
                continue
        print("Invalid User ID")
        time.sleep(0.4)
        print("Please try again.")
        cont4()

    else:
        print("Taking you to the main menu... ")
        time.sleep(0.70)
        utils.cls()
        main()
                            

def cont4():
    print("Taking you to Details Section... ")
    time.sleep(0.70)
    utils.cls()
    details()


def main():
    print('Wlcome to Digital Vision!') 
    ch=int(input("Press 1 to continue: "))
    if ch==1:
        print("")
        print('1. Sign in')
        print('2. Create Account')
        print('3. Delete Account')
        print('4. View Account Details')
        print('5. Exit\n')
        ch1=int(input("Select your choice: "))
        if ch1==1:
            sn()
        elif ch1==2:
            create()
        elif ch1==3:
            delt()
        elif ch1==4:
            details()
        else:
            while True:
                ch21=input("Do you really want to exit the program? (y/n): ")
                if ch21=="y":
                    utils._exit(0)
                else:
                    main()
    else:
        print("INVALID ENTRY")        

main()


