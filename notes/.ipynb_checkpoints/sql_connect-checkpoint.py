import mysql.connector
conn_obj=mysql.connector.connect(host='sql12.freesqldatabase.com',
                                 user='sql12805679',
                                 passwd='tJ3CENsy5b',
                                 database='sql12805679'
                                  )

# 1. Create the cursor object
mycursor = conn_obj.cursor()

# 2. Execute a query
mycursor.execute("SELECT VERSION()")
mycursor.execute("Create table N(nme char(10))")
mycursor.execute("desc N")
conn_object.commit()
cursor.close()
conn_object.cose()
