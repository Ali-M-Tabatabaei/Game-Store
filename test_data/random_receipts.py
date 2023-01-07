from app import connection, cursor, fake
import random

query = '''INSERT INTO receipts (total_price, customer_id, date, data)
    VALUES(%s, %s, %s, %s);'''

read_query = '''SELECT id FROM customers ORDER BY RAND() LIMIT 1;'''
product_read = '''SELECT product_code, sell_price FROM products WHERE receipt_id is NULL ORDER BY RAND() LIMIT 1;'''
product_update = '''UPDATE products SET receipt_id = %s WHERE product_code = %s;'''
receipt_update = '''UPDATE receipts SET total_price = %s WHERE receipt_id = %s;'''

# easter!
customer_id = 1
_date = str(fake.date_between('-7d'))
data = 'just buying games for the kids!'
bind = (0 , customer_id, _date, data)
cursor.execute(query, bind)

connection.commit()

total_price = 0
for _ in range(5):
    cursor.execute(product_read)
    product = cursor.fetchone()
    product_code = product['product_code']
    price = product['sell_price']
    total_price += price

    bind = (1, product_code)

    cursor.execute(product_update, bind)

bind = (total_price, 1)
cursor.execute(receipt_update, bind)

connection.commit()

for i in range(2, 1000):

    cursor.execute(read_query)
    customer_id = cursor.fetchone()
    customer_id = customer_id['id']

    _date = str(fake.date_between('-60d'))

    data = fake.text(50)

    bind = (0, customer_id, _date, data)

    cursor.execute(query, bind)

    number_of_items = random.randint(1, 3)
    total_price = 0
    for _ in range(number_of_items):
        cursor.execute(product_read)
        product = cursor.fetchone()
        product_code = product['product_code']
        price = product['sell_price']
        total_price += price

        bind = (i, product_code)

        cursor.execute(product_update, bind)

    bind = (total_price, i)
    cursor.execute(receipt_update, bind)


connection.commit()

