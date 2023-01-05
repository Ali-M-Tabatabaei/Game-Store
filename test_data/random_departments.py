from app import connection, cursor, fake
from reference_lists import departments

query = '''INSERT INTO departments (dept_name)
    VALUES (
        %s
        );'''

for dep in departments:
    cursor.execute(query, dep)

connection.commit()