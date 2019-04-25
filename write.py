import time
import sys
import subprocess
import pyodbc

def get_cpu_temperature():
  output = subprocess.check_output(["cat","/sys/class/thermal/thermal_zone0/temp"])
  temp_value = float(output) / 1000
  return temp_value
	
def main():
  conn_str = "Driver={Pervasive ODBC Interface};server=localhost;DBQ=demodata"
  db = pyodbc.connect(conn_str)
  c = db.cursor()
  print(get_cpu_temperature())
  insert_command = """INSERT INTO cpu_data (timestamp, temperature) VALUES (?, ?)"""

  while True:
    current_temp = get_cpu_temperature()
    print("Saving temperature: {0}".format(current_temp))
    timestamp = int(time.time())
    c.execute(insert_command, (timestamp, current_temp))
    time.sleep(30)

    c.execute("SELECT COUNT(*) FROM cpu_data")
    row = c.fetchone()
    if row:
      print('Total temperature records:', row[0])
		
  return 0
   
if __name__ == "__main__":
  sys.exit(main())
