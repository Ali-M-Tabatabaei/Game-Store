from app import connection, cursor, fake
import random

query = '''INSERT INTO comments (likes, dislikes, content)
        VALUES(
            %s,
            %s,
            %s
        );'''

for _ in range(5000):
    likes = random.randint(0, 1000)
    dislikes = random.randint(0, 1000)
    content = fake.text()

    bind = (likes, dislikes, content)

    cursor.execute(query, bind)

connection.commit()
