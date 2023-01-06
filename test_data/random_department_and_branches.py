# employee_works_for_official_branch
# employee_works_for_sales_branch
# official_branchs
# official_departments
# sales_branchs
# sales_departments

from app import connection, cursor, fake
import random

# departments
query = '''INSERT INTO official_departments (deptid) VALUES(%s);'''

read_query = '''SELECT deptid FROM departments;'''
cursor.execute(read_query)
departments = cursor.fetchall()
random.shuffle(departments)

delim = int(len(departments) * (1 / 3))

for i in range(delim):
    department = departments[i]
    deptid = department['deptid']

    cursor.execute(query, deptid)

connection.commit()

query = '''INSERT INTO sales_departments (deptid) VALUES(%s);'''

for i in range(delim, len(departments)):
    department = departments[i]
    deptid = department['deptid']

    cursor.execute(query, deptid)

connection.commit()

# branches
query = '''INSERT INTO official_branches (name, address, phonenumber, date_Of_establishment, deptid,
    manager_id) VALUES(%s, %s, %s, %s, %s, %s);'''

read_query = '''SELECT id from employees ORDER BY RAND() LIMIT 1'''


for i in range(delim):
    name = fake.company()
    address = fake.address()
    phonenumber = fake.phone_number()
    date_of_establish = str(fake.date_between('-20y'))

    department = departments[i]
    deptid = department['deptid']

    cursor.execute(read_query)
    manager_id = cursor.fetchone()['id']

    bind = (name, address, phonenumber, date_of_establish, deptid, manager_id)

    cursor.execute(query, bind)

connection.commit()

query = '''INSERT INTO sales_branches (name, address, phonenumber, date_Of_establishment, deptid,
    manager_id) VALUES(%s, %s, %s, %s, %s, %s);'''

read_query = '''SELECT id from employees ORDER BY RAND() LIMIT 1'''


for i in range(delim, len(departments)):
    name = fake.company()
    address = fake.address()
    phonenumber = fake.phone_number()
    date_of_establish = str(fake.date_between('-20y'))

    department = departments[i]
    deptid = department['deptid']

    cursor.execute(read_query)
    manager_id = cursor.fetchone()['id']

    bind = (name, address, phonenumber, date_of_establish, deptid, manager_id)

    cursor.execute(query, bind)

connection.commit()

######### relationships
read_query = '''SELECT id FROM employees;'''
cursor.execute(read_query)
employees = cursor.fetchall()

delim = int(len(employees) * (1 / 3))

read_query = '''SELECT branch_id FROM official_branches ORDER BY RAND() LIMIT 1'''

query = '''INSERT INTO employee_works_for_official_branch (employee_id, official_branch_branchid)
    VALUES(
        %s, %s
    )'''

for i in range(delim):
    employee_id = employees[i]['id']
    cursor.execute(read_query)
    branch = cursor.fetchone()
    branch_id = branch['branch_id']

    bind = (employee_id, branch_id)

    cursor.execute(query, bind)

connection.commit()


read_query = '''SELECT branch_id FROM sales_branches ORDER BY RAND() LIMIT 1'''

query = '''INSERT INTO employee_works_for_sales_branch (employee_id, sales_branch_branchid)
    VALUES(
        %s, %s
    )'''

for i in range(delim, len(employees)):
    employee_id = employees[i]['id']
    cursor.execute(read_query)
    branch = cursor.fetchone()
    branch_id = branch['branch_id']

    bind = (employee_id, branch_id)

    cursor.execute(query, bind)


connection.commit()