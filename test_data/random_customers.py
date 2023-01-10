from app import connection, cursor, fake
import random
from reference_lists import cities

query = '''INSERT INTO customers (username, password, phonenumber, city)
        VALUES(
            %s,
            %s,
            %s,
            %s
        );'''

cursor.execute(query, ('Phantom1', 'phantomAliHaha', '50340930', 'MASHHAD'))

for _ in range(2000):
    fname = fake.first_name()
    lname = fake.last_name()
    username = fname + '_' + lname
    password = fake.password(8)
    phone_number = fake.phone_number()
    city = random.choice(cities)

    bind_data = (username, password, phone_number, city)
    cursor.execute(query, bind_data)

connection.commit()