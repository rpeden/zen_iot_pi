import pyodbc

conn_str = "Driver={Pervasive ODBC Interface};server=localhost;DBQ=demodata"
db = pyodbc.connect(conn_str)
c = db.cursor()

print("Setting up database...")
c.execute("DROP TABLE IF EXISTS cpu_data")
c.execute("CREATE TABLE cpu_data (id identity, timestamp bigint, temperature real)")
c.execute("CREATE INDEX cpu_data_time on cpu_data (timestamp)")
