from app import connection, cursor, fake
import random

query = '''INSERT INTO given_comments (comment_id, customer_id, rating)
    VALUES(
        %s, %s, %s
    )'''

read_query = '''SELECT comment_id FROM comments'''
customer_read = '''SELECT id FROM customers ORDER BY RAND() LIMIT 1'''
cursor.execute(read_query)
comments = cursor.fetchall()

for comment in comments:
    comment_id = comment['comment_id']

    cursor.execute(customer_read)
    customer_id = cursor.fetchone()
    customer_id = customer_id['id']

    rating = random.randint(3, 10)

    bind = (comment_id, customer_id, rating)

    cursor.execute(query, bind)

connection.commit()