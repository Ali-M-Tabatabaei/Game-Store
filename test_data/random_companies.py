from app import connection, cursor, fake
from reference_lists import companies

query = '''INSERT INTO companies (name, city)
        VALUES(
            %s,
            %s
        );'''

for i in range(len(companies)):
    name = companies[i]
    city = fake.city()

    bind_data = (name, city)

    cursor.execute(query, bind_data)

connection.commit()