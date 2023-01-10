from app import connection, cursor, fake
import random

query = '''INSERT INTO contracts (amount)
        VALUES(
            %s
        );'''

for _ in range(500):
    amount = 1000000 * random.randint(1, 9000)
    
    bind = (amount,)

    cursor.execute(query, bind)

connection.commit()
