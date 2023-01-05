from app import connection, cursor, fake

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

