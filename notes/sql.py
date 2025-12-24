import mysql.connector
# 1. Create the cursor object
mycursor = conn_obj.cursor()
# 2. Execute a query
mycursor.execute("SELECT VERSION()")
