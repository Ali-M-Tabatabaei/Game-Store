from app import connection, cursor, fake
import random
from reference_lists import cities, departments, companies, games, consoles
from datetime import date, timedelta

### random customers ###
### random employees ###
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


### random departments ###
query = '''INSERT INTO departments (dept_name)
    VALUES (
        %s
        );'''

for dep in departments:
    cursor.execute(query, dep)

connection.commit()

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

### random branches ###
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

### random companies ###
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

### random contracts ###
query = '''INSERT INTO contracts (amount)
        VALUES(
            %s
        );'''

for _ in range(500):
    amount = 1000000 * random.randint(1, 9000)
    
    bind = (amount,)

    cursor.execute(query, bind)

connection.commit()

### random customers ###
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

### random products ###
query = '''INSERT INTO products (brand, name, buy_price, sell_price, product_type,
 game_type, in_stock, provider_name)
 VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s
 )
'''

random.shuffle(games)
product_type = 'video_game'
in_stock = 'no'

# games
for _ in range(5000):
    game = random.choice(games)
    brand = game['brand']
    name = game['name']
    buy_price = random.randint(1000, 1750)
    sell_price = buy_price + random.randint(100, 500)
    buy_price *= 1000
    sell_price *= 1000
    game_type = game['gtype']
    provider_name = game['brand']

    bind = (brand, name, buy_price, sell_price, product_type, game_type, in_stock, provider_name)
    cursor.execute(query, bind)

random.shuffle(consoles)
product_type = 'game_console'

# consoles
for _ in range(500):
    console = random.choice(consoles)
    brand = console['brand']
    name = console['name']
    buy_price = console['price']
    rand = random.randint(100, 1000) * 1000
    sell_price = buy_price + rand
    game_type = '-'
    provider_name = console['brand']

    bind = (brand, name, buy_price, sell_price, product_type, game_type, in_stock, provider_name)
    cursor.execute(query, bind)

connection.commit()

### random deals ###
write_query = '''INSERT INTO deals (contract_number, company_id)
    VALUES(
        %s,
        %s
    );'''

contract_query = '''SELECT * FROM contracts ORDER BY RAND() LIMIT 1;'''
company_query = '''SELECT * FROM companies ORDER BY RAND() LIMIT 1;'''
contracts_count_query = '''select count(*) as count from contracts;'''

cursor.execute(contracts_count_query)
count = cursor.fetchone()
count = int(count['count'])

for _ in range(count):
    cursor.execute(contract_query)
    contract_number = cursor.fetchone()
    contract_number = contract_number['contract_number']

    cursor.execute(company_query)
    company_id = cursor.fetchone()
    company_id = company_id['id']

    bind = (contract_number, company_id)

    cursor.execute(write_query, bind)

connection.commit()


### random discounts ###
write_query = '''INSERT INTO discounts (product_id, start_date, 
end_date, active, percentage)
VALUES (
    %s, %s, %s, %s, %s
);'''

read_query = '''SELECT product_code FROM products ORDER BY RAND() LIMIT 500;'''

cursor.execute(read_query)
products = cursor.fetchall()


active = 'No'

for product in products:
    product_id = int(product['product_code'])
    start_date = str(fake.date_between('-7d'))
    end_date = str(fake.date_between(date.today(), date.today() + timedelta(days=7)))
    rand = random.randint(1, 10)
    percentage = rand * 5

    bind = (product_id, start_date, end_date, active, percentage)

    cursor.execute(write_query, bind)

connection.commit()

### random comments ###
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

### random receipts ###
query = '''INSERT INTO receipts (total_price, customer_id, data)
    VALUES(%s, %s, %s)'''

read_query = '''SELECT id FROM customers ORDER BY RAND() LIMIT 1'''

for _ in range(1000):
    rand = random.randint(100, 50000)
    total_price = rand * 1000

    cursor.execute(read_query)
    emp = cursor.fetchone()
    emp = emp['id']

    data = fake.text(50)

    bind = (total_price, emp, data)

    cursor.execute(query, bind)

connection.commit()

