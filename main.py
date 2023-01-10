from typing import re

import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request, render_template, redirect, url_for, session
from typing import re


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)


@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))


@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/create', methods=['POST'])
def create_emp():
    try:
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']
        if _name and _email and _phone and _address and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO emp(name, email, phone, address) VALUES(%s, %s, %s, %s)"
            bindData = (_name, _email, _phone, _address)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Employee added successfully!')
            response.status_code = 200
            return response
        else:
            return show_message()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/emp')
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, phone, address FROM emp")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/emp/')
def emp_details(emp_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, phone, address FROM emp WHERE id =%s", emp_id)
        empRow = cursor.fetchone()
        response = jsonify(empRow)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['PUT'])
def update_emp():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']
        if _name and _email and _phone and _address and _id and request.method == 'PUT':
            sqlQuery = "UPDATE emp SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            bindData = (_name, _email, _phone, _address, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return show_message()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/', methods=['DELETE'])
def delete_emp(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM emp WHERE id =%s", (id,))
        conn.commit()
        response = jsonify('Employee deleted successfully!')
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/list-of-products', methods=['GET'])
def show_products():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "SELECT name FROM products;"
        cursor.execute(query)
        products = cursor.fetchall()
        response = jsonify(products)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# admin only
@app.route('/list-of-customers', methods=['GET'])
def show_customers():
    if 'loggedin' in session:
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "SELECT username FROM customers;"
            cursor.execute(query)
            customers = cursor.fetchall()
            response = jsonify(customers)
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/categories', methods=['GET'])
def show_categories():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "SELECT DISTINCT game_type FROM products;"
        cursor.execute(query)
        categories = cursor.fetchall()
        response = jsonify(categories)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/receipts', methods=['GET'])
def show_receipts():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = '''SELECT * FROM receipts;'''
        cursor.execute(query)
        # conn.commit()
        categories_row = cursor.fetchone()
        response = jsonify(categories_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/top-10-customers-weekly', methods=['GET'])
def show_top_customers_weekly():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = '''
                SELECT customer_id, username, spent FROM customers,
                    (SELECT customer_id, SUM(total_price) AS spent FROM 
                    (SELECT * FROM receipts WHERE DATEDIFF(curdate(), date) < 7) AS T
                    GROUP BY customer_id ORDER BY spent DESC LIMIT 10) AS top_customers
                WHERE customers.id = top_customers.customer_id;
                '''
        cursor.execute(query)
        # conn.commit()
        categories_row = cursor.fetchone()
        response = jsonify(categories_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/top-10-customers-monthly', methods=['GET'])
def show_top_customers_monthly():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = '''
            SELECT customer_id, username, spent FROM customers,
                (SELECT customer_id, SUM(total_price) AS spent FROM 
                (SELECT * FROM receipts WHERE DATEDIFF(curdate(), date) < 30) AS T
                GROUP BY customer_id ORDER BY spent DESC LIMIT 10) AS top_customers
            WHERE customers.id = top_customers.customer_id;
        '''
        cursor.execute(query)
        # conn.commit()
        categories_row = cursor.fetchone()
        response = jsonify(categories_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/most-sold-products-weekly', methods=['GET'])
def show_most_sold_products_weekly():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = '''
            SELECT name, SUM(sell_price) AS sold FROM
                (SELECT name, sell_price FROM receipts,
                    (SELECT * FROM products WHERE receipt_id IS NOT NULL ) AS sold_products
                WHERE (sold_products.receipt_id = receipts.receipt_id) & (DATEDIFF(CURDATE(), receipts.date) < 7)
                ) AS weekly_products
            GROUP BY name ORDER BY sold DESC;
        '''
        cursor.execute(query)
        # conn.commit()
        categories_row = cursor.fetchone()
        response = jsonify(categories_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/most-sold-products-monthly', methods=['GET'])
def show_most_sold_products_monthly():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = '''
            SELECT name, SUM(sell_price) AS sold FROM
                (SELECT name, sell_price FROM receipts,
                    (SELECT * FROM products WHERE receipt_id IS NOT NULL ) AS sold_products
                WHERE (sold_products.receipt_id = receipts.receipt_id) & (DATEDIFF(CURDATE(), receipts.date) < 30)
                ) AS monthly_products
            GROUP BY name ORDER BY sold DESC;
        '''
        cursor.execute(query)
        # conn.commit()
        categories_row = cursor.fetchone()
        response = jsonify(categories_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/special-offers', methods=['GET'])
def show_special_offers():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = '''
            SELECT products.name , products.sell_price, discounts.percentage
            FROM discounts, products
            WHERE (discounts.product_id = products.product_code) & (discounts.percentage >= 15);
        '''
        cursor.execute(query)
        # conn.commit()
        categories_row = cursor.fetchone()
        response = jsonify(categories_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/show-provider', methods=['GET'])
def show_provider():
    if 'loggedin' in session:
        try:
            _json = request.json
            product_name = _json['product']
            if product_name and request.method == 'GET':
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = '''
                    CALL showInStockBranches('xbox one');
                '''
                # bindData = (_name, _email, _phone, _address)
                cursor.execute(query, product_name)
                # conn.commit()
                provider_row = cursor.fetchone()
                response = jsonify(provider_row)
                response.status_code = 200
                return response
            else:
                return show_message()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))



@app.route('/show-cheapest-provider', methods=['GET'])
def show_cheapest_provider():
    if 'loggedin' in session:
        try:
            _json = request.json
            product_name = _json['product']
            if product_name and request.method == 'GET':
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = '''
                    CALL showChipestProvider('playstation 5');
                '''
                # bindData = (_name, _email, _phone, _address)
                cursor.execute(query, product_name)
                # conn.commit()
                provider_row = cursor.fetchone()
                response = jsonify(provider_row)
                response.status_code = 200
                return response
            else:
                return show_message()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/last-ten-orders', methods=['GET'])
def show_last_ten_orders():
    try:
        _json = request.json
        username = _json['user']
        if username and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = '''
                CALL showTenLastPurchases(1);
            '''
            # bindData = (_name, _email, _phone, _address)
            cursor.execute(query, username)
            # conn.commit()
            users_row = cursor.fetchone()
            response = jsonify(users_row)
            response.status_code = 200
            return response
        else:
            return show_message()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/comments', methods=['GET'])
def show_comments():
    try:
        _json = request.json
        product_name = _json['product']
        if product_name and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "select comment.content from products, comment, product_has_comment where(" \
                    "comment.commentid = product_has_comment.comment_commentid) & (product_has_comment.product_code = " \
                    "products.product_code) & (product.name = \"%s\");"
            # bindData = (_name, _email, _phone, _address)
            cursor.execute(query, product_name)
            # conn.commit()
            users_row = cursor.fetchone()
            response = jsonify(users_row)
            response.status_code = 200
            return response
        else:
            return show_message()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/top-comments', methods=['GET'])
def show_top_comments():
    try:
        _json = request.json
        product_name = _json['product']
        if product_name and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "select comment.content, product_has_comment.score as score from products, comment, " \
                    "product_has_comment where(comment.commentid = product_has_comment.comment_commentid) & (" \
                    "product_has_comment.product_code = products.product_code) & (product.name = \"%s\") order by desc " \
                    "score limit 3;"
            # bindData = (_name, _email, _phone, _address)
            cursor.execute(query, product_name)
            # conn.commit()
            users_row = cursor.fetchone()
            response = jsonify(users_row)
            response.status_code = 200
            return response
        else:
            return show_message()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/worst-comments', methods=['GET'])
def show_worst_comments():
    try:
        _json = request.json
        product_name = _json['product']
        if product_name and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "select comment.content, product_has_comment.score as score from products, comment, " \
                    "product_has_comment where(comment.commentid = product_has_comment.comment_commentid) & (" \
                    "product_has_comment.product_code = products.product_code) & (product.name = \"%s\") order by " \
                    "score limit 3;"
            # bindData = (_name, _email, _phone, _address)
            cursor.execute(query, product_name)
            # conn.commit()
            users_row = cursor.fetchone()
            response = jsonify(users_row)
            response.status_code = 200
            return response
        else:
            return show_message()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/total-sold', methods=['GET'])
def show_total_sold():
    if 'loggedin' in session:
        try:
            _json = request.json
            product_name = _json['product']
            if product_name and request.method == 'GET':
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = "select sum(products.sell_price) as totalAmount from products where product.name  = \"%s\" & " \
                        "product.isSold = 1 & datediff(curdate(), product.sold_date) < 30;"
                # bindData = (_name, _email, _phone, _address)
                cursor.execute(query, product_name)
                # conn.commit()
                users_row = cursor.fetchone()
                response = jsonify(users_row)
                response.status_code = 200
                return response
            else:
                return show_message()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))



@app.route('/average-income', methods=['GET'])
def show_average_income():
    if 'loggedin' in session:
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "select avg (products.sell_price) as totalAmount from products where product.isSold = 1 & datediff(" \
                    "curdate(), product.sold_date) < 30;"

            cursor.execute(query)
            # conn.commit()
            income = cursor.fetchone()
            response = jsonify(income)
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/city-customers', methods=['GET'])
def show_city_customers():
    try:
        _json = request.json
        city_name = _json['city']
        if city_name and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "select customer.name, customer.city from customer where customer.city=\"%s\";"
            # bindData = (_name, _email, _phone, _address)
            cursor.execute(query, city_name)
            # conn.commit()
            customer_row = cursor.fetchone()
            response = jsonify(customer_row)
            response.status_code = 200
            return response
        else:
            return show_message()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/providers-in-city', methods=['GET'])
def show_providers_in_city():
    try:
        _json = request.json
        city_name = _json['city']
        product_name = _json['product']
        if city_name and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "select product.provider_name from product, company where product.provider_name= company.name & " \
                    "company.city=%s & product.name=%s;"
            bind_data = (city_name, product_name)
            cursor.execute(query, bind_data)
            # conn.commit()
            customer_row = cursor.fetchone()
            response = jsonify(customer_row)
            response.status_code = 200
            return response
        else:
            return show_message()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def show_message(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    # Quick test configuration. Please use proper Flask configuration options
    # in production settings, and use a separate file or environment variables
    # to manage the secret key!
    app.secret_key = 'mySuperKey'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
