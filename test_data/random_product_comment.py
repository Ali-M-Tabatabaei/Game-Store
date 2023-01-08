from app import connection, cursor, fake
import random

query = '''INSERT INTO product_has_comment (product_code, comment_id)
    VALUES(%s, %s)'''

comments_query = '''SELECT comment_id FROM comments;'''
products_query = '''SELECT product_code FROM products ORDER BY RAND() LIMIT 100;'''

cursor.execute(comments_query)
comments = cursor.fetchall()
cursor.execute(products_query)
products = cursor.fetchall()

for comment in comments:
    comment_id = comment['comment_id']

    product = random.choice(products)
    product_code = product['product_code']

    bind = (product_code, comment_id)

    cursor.execute(query, bind)

connection.commit()