import mysql.connector
from mistune.plugins.formatting import insert
from ply.yacc import resultlimit

select_query = "select * from employees"

print("Starting.....")
try:
    #Connecting python code to the database
    con = mysql.connector.connect(host="localhost",
                              user="root",
                              port="3306",
                              password="Root@123",
                              database="company_database",
                              use_pure=True)
    curs= con.cursor()
    curs.execute(select_query)
    #for rows in curs:
       # print(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5])
    #print("Connection Succesful")
    result = curs.fetchmany(5)
    print("Connected to database")
    print(result)
    con.close() # closing connection
except:
    print("Connection Error")
print("Finished..")