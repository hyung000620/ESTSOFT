import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="retaurant",
    user="postgres",
    password="1234"
)

cur = conn.cursor()

select_query = """
    SELECT * FROM fastfood_restaurant_us WHERE city = 'Detroit'
"""
update_query = """
    UPDATE fastfood_restaurant_us SET categories = %s WHERE city = %s AND categories IN ('Fast food restaurants', 'Fast Food Restaurant')
"""

cur.execute(update_query, ("Fast Food Restaurant", "Detroit"))
conn.commit()

# rows = cur.fetchmany(5)

# for row in rows:
#     print(row)

