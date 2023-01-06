from app import connection, cursor, fake
import random

query = '''INSERT INTO receipts (total_price, customer_id, data)
    VALUES(%s, %s, %s)'''

read_query = '''SELECT id FROM customers ORDER BY RAND() LIMIT 1'''

for _ in range(1000):
    rand = random.randint(100, 50000)
    total_price = rand * 1000

    cursor.execute(read_query)
    emp = cursor.fetchone()
    emp = emp['id']

    data = fake.text(50)

    bind = (total_price, emp, data)

    cursor.execute(query, bind)

connection.commit()

