import os
import pymysql

dbcon = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : 'novasky82!',
    'db' : 'sensor_signal'    
}

def insert(self, vo):
    self.conn = pymysql.connect(host='localhost', user='root', password='novasky!', db='departments', charset='utf8')
    cur = self.conn.cursor()  
    sql = "insert into members (%s, %s, %s, %s)"
    vals = (vo.id, vo.pwd, vo.name, vo.email)
    cur.execute(sql, vals)
    self.conn.commit()
    self.conn.close()
a= '1'
b='2'
c='3'
d='4'

insert(a, b, c, d)




""" 

import mysql.connector

try:
    # (1) MYSQL 연결 
    connection = mysql.connector.connect(
        host = '127.0.0.1',
        database = 'db1',  
        user = 'root',
        password = 'password'   
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print('mysql Version : ', db_info)  

        # (2) 커서 만들기 
        cursor = connection.cursor()

        # (3) 원하는 쿼리문 등 실행 
        cursor.execute('show tables;')
        

        # (4) 커서에서 실행 결과 한줄씩 가져오기         
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()

except Error as e:
    print('Database Error: ',e) 

finally:
    # (5) 데이터베이스 커서와 커넥션을 모두 닫음 
    cursor.close()
    connection.close()
    print('MySQL Connection Close') """