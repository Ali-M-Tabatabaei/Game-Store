from app import connection, cursor, fake
import random
from datetime import date, timedelta

write_query = '''INSERT INTO discounts (product_id, start_date, 
end_date, active, percentage)
VALUES (
    %s, %s, %s, %s, %s
);'''

read_query = '''SELECT product_code FROM products ORDER BY RAND() LIMIT 500;'''

cursor.execute(read_query)
products = cursor.fetchall()


active = 'No'

for product in products:
    product_id = int(product['product_code'])
    start_date = str(fake.date_between('-7d'))
    end_date = str(fake.date_between(date.today(), date.today() + timedelta(days=7)))
    rand = random.randint(1, 10)
    percentage = rand * 5

    bind = (product_id, start_date, end_date, active, percentage)

    cursor.execute(write_query, bind)

connection.commit()
