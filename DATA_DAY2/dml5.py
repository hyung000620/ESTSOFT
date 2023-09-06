import psycopg2
import time
import csv

conn = psycopg2.connect(
    host="oreumi-test-postgresql.cyxsnajbfbeu.ap-northeast-2.rds.amazonaws.com", # oreumi.aws.
    database="oreumitestpostgresql", # 접속할 데이터베이스
    user="admin1", # 관리자 유저
    password="12345678", # 관리자 비밀번호
    )

cur = conn.cursor()
# select_query = """
#     SELECT * FROM fastfood_restaurant_us
# """
# cur.execute(select_query)


insert_quert = """
    INSERT INTO oreumi_answer (name, answer, question) VALUES(%s,%s,%s) 
"""
# rows = cur.fetchall()


cur.execute(insert_quert, ("이준형", "2014-02-01 04:52:11","3"))
conn.commit()

conn.close()