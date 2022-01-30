import mysql.connector as c

print("Initialising app...")
print("Logging into the database...")
sql_usrnm = input("MySQL Username: ")
sql_pw = input("MySQL password: ")

con=c.connect(user=sql_usrnm, password=sql_pw, host="localhost", database="testdb")
print("connection succeeded!")
c1=con.cursor()

c1.execute("select sr_no from lol")
d = c1.fetchall()
inputlol = int(input("enter a number lol: "))
lst = list(d)
for i in range(0, len(lst)):
    print("the database says ", lst[i])
    if lst[i] == (inputlol,):
        print("your inpuut exists in the database!")
    else:
        print("fuck you you don't exist in the db lol")