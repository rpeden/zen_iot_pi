import pyodbc
import time

conn_str = "Driver={Pervasive ODBC Interface};server=localhost;DBQ=demodata"
db = pyodbc.connect(conn_str)
c = db.cursor()

five_mins_ago = int(time.time()) - 300
query = "SELECT AVG (temperature) FROM cpu_data WHERE timestamp > ?"
result = c.execute(query, (five_mins_ago,))
row = result.fetchone()

if row:
	print("Average temperature over past 5 minutes: {0}".format(row[0]))
