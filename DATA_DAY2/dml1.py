import psycopg2
import time
import csv

connection = psycopg2.connect(
    host="localhost", # oreumi.aws.
    database="retaurant", # 접속할 데이터베이스
    user="postgres", # 관리자 유저
    password="1234", # 관리자 비밀번호
    )

cursor = connection.cursor() # 커서 생성

csv_file_path = 'Datafiniti_Fast_Food_Restaurants.csv'

insert_query = """
    INSERT INTO fastfood_restaurant_us (id, "dateAdded", "dateUpdated", address, categories, city, country, keys, latitude, longitude, name, "postalCode", province, "sourceURLs", websites) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

with open(csv_file_path, 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        row[1] = row[1].replace('T', ' ').replace('Z', '')
        row[2] = row[2].replace('T', ' ').replace('Z', '')
        row[8] = float(row[8])
        row[9] = float(row[9])
        cursor.execute(insert_query, row)
    connection.commit()

cursor.rowcount()