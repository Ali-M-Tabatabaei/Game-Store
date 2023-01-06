from app import connection, cursor, fake
import random

query = '''INSERT INTO employees (name) VALUES(%s);'''

for _ in range(450):
    name = fake.name()

    cursor.execute(query, name)

connection.commit()

read_query = '''SELECT id FROM employees'''

cursor.execute(read_query)
employees = cursor.fetchall()
random.shuffle(employees)

### fulltime employees ###

write_query = '''INSERT INTO fulltime_employees (emp_id, salary) VALUES(%s, %s);'''

fulltime_range = int(len(employees) * 1 / 3)

for i in range(fulltime_range):
    emp_id = employees[i]['id'] 
    rand = random.randint(5, 30)
    salary = rand * 1000000

    bind = (emp_id, salary)

    cursor.execute(write_query, bind)

connection.commit()


### parttime employees ###

write_query = '''INSERT INTO parttime_employees (emp_id, salary) VALUES(%s, %s);'''

for i in range(fulltime_range, len(employees)):
    emp_id = employees[i]['id'] 
    rand = random.randint(3, 15)
    salary = rand * 1000000

    bind = (emp_id, salary)

    cursor.execute(write_query, bind)

connection.commit()