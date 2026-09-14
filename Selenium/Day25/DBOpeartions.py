import mysql.connector
from mistune.plugins.formatting import insert
update_query = "update employees set emp_name='Roshan' where emp_id=1"
insert_query = "insert into employees values(114,'Kim',77000,'2003-06-25',1,101)"
delete_query = "delete from employees where emp_id=113"
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
    print("Connection Succesful")
    curs.execute(delete_query)
    con.commit()
    con.close()
except:
    print("Connection Error")
print("Finished..")