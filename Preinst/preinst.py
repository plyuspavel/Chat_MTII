import psycopg2
import time 

gate = True
while gate:
	try:
		conn = psycopg2.connect(dbname='projbase', user='admn', password='adminn', host='postgres')
		cur = conn.cursor()
	except:
		print("Not ready preinst")
		time.sleep(1)
	else:
		print("Preinstalling..")
		gate = False


cur.execute("CREATE SEQUENCE user_ids;")
conn.commit()
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY DEFAULT NEXTVAL('user_ids'), login CHAR(64), password CHAR(64));")
conn.commit()
  
  
cur.execute("CREATE SEQUENCE frined_ids;")
conn.commit()
cur.execute("CREATE TABLE friends(id INTEGER PRIMARY KEY DEFAULT NEXTVAL('user_ids'), main CHAR(64), frnd CHAR(64));")
conn.commit()
  
  
cur.execute("CREATE SEQUENCE chat_ids;")
conn.commit()
cur.execute("CREATE TABLE chat(id INTEGER PRIMARY KEY DEFAULT NEXTVAL('user_ids'),from_user CHAR(64), to_user CHAR(64), text CHAR(200), timeofmes timestamp);")
conn.commit()
