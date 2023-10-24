import sqlite3

conn = sqlite3.connect("example.db")
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
 VALUES(2,'JOHN',25,'NAIROBI',30000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
 VALUES(3,'JANE',50,'KISUMU',60000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
 VALUES(4,'JEFF',35,'NAKURU',20000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
 VALUES(5,'JOE',40,'MACHAKOS',50000.00)");

conn.commit()
print("Records inserted successfully")
conn.close()