import psycopg2

conn = psycopg2.connect(database="oreumi", user="postgres", password="1234", host="127.0.0.1", port="5432")

cursor = conn.cursor()

insert_query = "INSERT INTO student VALUES (%s, %s, %s, %s)"

data_insert = []
with open("data.txt", "r", encoding='utf-8') as f:
    for i in f.read().split("\n"):
        a, b, c, d = i.split(', ')
        data_insert.append((a, b, c, d))
        

cursor.executemany(insert_query, data_insert)
conn.commit()
print("데이터 입력 완료!")

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
for row in rows:
    print(row)