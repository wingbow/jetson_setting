#%%
# generate database
import pymysql 
from datetime import datetime

class Connection:
# setting parameters for mysql connection
        def __init__(self,):
                self.dbcon = {
                'host' : 'localhost',
                'user' : 'peter',
                'password' : 'novasky82!',
                'charset' : 'utf8', 
                'autocommit' : 'True'
                }

        def create_schema(self, schema_nm):
                self.conn = pymysql.connect(**self.dbcon)
                self.cursor = self.conn.cursor() 
                
                sql = "CREATE DATABASE IF NOT EXISTS " + str(schema_nm)

                self.cursor.execute(sql)
                self.conn.commit() 
                self.conn.close() 
                
        def create_table(self, db_name, table_nm):
                self.conn = pymysql.connect(**self.dbcon)
                self.cursor = self.conn.cursor() 
                
                # example
                # CREATE TABLE InputTest (date date, time time, date_time datetime, time_stamp timestamp);

                sql = 'CREATE TABLE IF NOT EXISTS`' + str(db_name) +'`.`' + str(table_nm) + '''` (
                          `idx` INT NOT NULL auto_increment,
                          `time` DATETIME(6) NOT NULL,
                          `sensor_value` DOUBLE NULL,
                          PRIMARY KEY (`idx`))
                ''' 
                self.cursor.execute(sql)
                self.conn.commit() 
                self.conn.close()  

                
        def insert_data(self, data):
                time.sleep(1.5)
                self.conn = pymysql.connect(**self.dbcon)
                self.cursor = self.conn.cursor() 

                sql = "INSERT INTO jetson.data (time, sensor_value) VALUES (now(6), %s)" 
                self.cursor.execute(sql,data)

                self.conn.commit() 
                self.conn.close() 
                
        def update_data(self, db_name, *data):
                self.conn = pymysql.connect(**self.dbcon)
                self.cursor = self.conn.cursor() 


                sql = "DELETE FROM user WHERE email = %s" 
                self.cursor.execute(sql)

                self.conn.commit() 
                self.conn.close() 
                
        def update_data(self, db_name, *data):
                self.conn = pymysql.connect(**self.dbcon)
                self.cursor = self.conn.cursor() 

                sql = "DELETE FROM user WHERE email = %s" 
                self.cursor.execute(sql)

                self.conn.commit() 
                self.conn.close() 
               
        def show_db(self):
                self.conn = pymysql.connect(**self.dbcon)
                self.cursor = self.conn.cursor() 

                sql = "show databases" 
                self.cursor.execute(sql)
                db_names = self.cursor.fetchall()

                self.conn.commit() 
                self.conn.close() 
                return list(db_names)

# %% test
conn = Connection()
db_names = conn.show_db()
conn.create_schema("jetson")
conn.create_table("jetson", "data")

import time
import random

out = open('output_log.txt', 'a')
for idx in range(20):
        now = datetime.now()
        sensing_value= random.random()
        conn.insert_data(sensing_value)
        print(now, sensing_value)
        print(now, sensing_value, file=out)
        time.sleep(10)
        
out.close()

# %%
