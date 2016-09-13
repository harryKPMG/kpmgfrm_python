import  sqlite3

con=sqlite3.connect('a.sqlite')
cursor = con.cursor()
sql='''
 CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
)
'''
sql2='select * from COMPANY'

sql3='''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (3, 'Paul1', 32, 'California', 20000.00 )
'''
sql4='''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (2, 'Paul1', 32, 'California', 20000.00 )
# '''
# cursor.execute(sql3)
# cursor.execute(sql4)
# con.commit()
#

cursor.execute(sql2)
data = cursor.fetchall()
for d in data:
    print d

# data = cursor.next()
# cursor.fetchmany()
# print data
cursor.close()