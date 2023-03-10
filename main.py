from typing import re

import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request, render_template, redirect, url_for, session
from typing import re
import pandas as pd
from pandas import json_normalize


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
            if username == 'admin' and password == 'admin':
                session['admin'] = True
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


@app.route('/create-user', methods=['GET'])
def create_emp():
    if 'loggedin' in session :
        if 'admin' in session:
            try:
                args = request.args
                email = args['email']
                username = args['username']
                password = args['password']
                if email and username and password and request.method == 'GET':
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    sqlQuery = "INSERT INTO accounts(email, username, password) VALUES(%s, %s, %s)"
                    bindData = (email, username, password)
                    cursor.execute(sqlQuery, bindData)
                    conn.commit()
                    response = jsonify('User added successfully!')
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
            response = jsonify('only accessible by admin!')
            response.status_code = 403
            return response
    else:
        return redirect(url_for('login'))


@app.route('/create-product', methods=['GET'])
def create_product():
    if 'loggedin' in session :
        if 'admin' in session:
            try:
                args = request.args
                brand = args['brand']
                name = args['name']
                '''buy_price = args['buy_price']
                sell_price = args['sell_price']
                product_type = args['product_type']
                game_type = args['game_type']
                provider_name = args['provider_name']
                in_stock = args['in_stock']
                sold_date = args['sold_date']'''
                branch_id = args['branch_id']
                receipt_id = args['receipt_id']
                if receipt_id and branch_id and brand and name and request.method == 'GET':
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    sqlQuery = "INSERT INTO products(name, brand, branch_id, receipt_id) VALUES(%s, %s, %s, %s)"
                    bindData = (name, brand, branch_id, receipt_id)
                    cursor.execute(sqlQuery, bindData)
                    conn.commit()
                    response = jsonify('Product added successfully!')
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
            response = jsonify('only accessible by admin!')
            response.status_code = 403
            return response
    else:
        return redirect(url_for('login'))


@app.route('/update-product', methods=['GET'])
def update_product():
    if 'loggedin' in session :
        if 'admin' in session:
            try:
                args = request.args
                brand = args['brand']
                name = args['name']
                '''buy_price = args['buy_price']
                sell_price = args['sell_price']
                product_type = args['product_type']
                game_type = args['game_type']
                provider_name = args['provider_name']
                in_stock = args['in_stock']
                sold_date = args['sold_date']'''
                branch_id = args['branch_id']
                receipt_id = args['receipt_id']
                if receipt_id and branch_id and brand and name and request.method == 'GET':
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    sqlQuery = "INSERT INTO products(name, brand, branch_id, receipt_id) VALUES(%s, %s, %s, %s)"
                    bindData = (name, brand, branch_id, receipt_id)
                    cursor.execute(sqlQuery, bindData)
                    conn.commit()
                    response = jsonify('Product added successfully!')
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
            response = jsonify('only accessible by admin!')
            response.status_code = 403
            return response
    else:
        return redirect(url_for('login'))


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


@app.route('/update-user', methods=['GET'])
def update_emp():
    if 'loggedin' in session:
        if 'admin' in session:
            try:
                args = request.args
                id = args['id']
                email = args['email']
                username = args['username']
                password = args['password']
                if id and email and username and password and request.method == 'GET':
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    sqlQuery = "update accounts set username = %s, password = %s, email = %s where id = %s"
                    bindData = (username, password, email, id)
                    cursor.execute(sqlQuery, bindData)
                    conn.commit()
                    response = jsonify('User updated successfully!')
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
            response = jsonify('only accessible by admin!')
            response.status_code = 403
            return response
    else:
        return redirect(url_for('login'))


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
    if 'loggedin' in session:
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "SELECT name FROM products;"
            cursor.execute(query)
            products = cursor.fetchall()
            response = jsonify(products)
            response.status_code = 200
            pd_object = json_normalize(products)
            temp = pd_object.to_dict('records')
            column_names = pd_object.columns.values
            return render_template('record.html', records=temp, colnames=column_names)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


# admin only
@app.route('/list-of-customers', methods=['GET'])
def show_customers():
    if 'loggedin' in session :
        if 'admin' in session:
            try:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = "SELECT username FROM customers;"
                cursor.execute(query)
                customers = cursor.fetchall()
                response = jsonify(customers)
                response.status_code = 200
                pd_object = json_normalize(customers)
                temp = pd_object.to_dict('records')
                column_names = pd_object.columns.values
                return render_template('record.html', records=temp, colnames=column_names)
            except Exception as e:
                print(e)
            finally:
                cursor.close()
                conn.close()
        else:
            response = jsonify('only accessible by admin!')
            response.status_code = 403
            return response
    else:
        return redirect(url_for('login'))


@app.route('/categories', methods=['GET'])
def show_categories():
    if 'loggedin' in session:
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "SELECT DISTINCT game_type FROM products;"
            cursor.execute(query)
            categories = cursor.fetchall()
            response = jsonify(categories)
            response.status_code = 200
            pd_object = json_normalize(categories)
            temp = pd_object.to_dict('records')
            column_names = pd_object.columns.values
            return render_template('record.html', records=temp, colnames=column_names)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/receipts', methods=['GET'])
def show_receipts():
    if 'loggedin' in session:
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = '''SELECT * FROM receipts;'''
            cursor.execute(query)
            # conn.commit()
            categories_row = cursor.fetchall()
            response = jsonify(categories_row)
            response.status_code = 200
            pd_object = json_normalize(categories_row)
            temp = pd_object.to_dict('records')
            column_names = pd_object.columns.values
            return render_template('record.html', records=temp, colnames=column_names)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/top-10-customers-weekly', methods=['GET'])
def show_top_customers_weekly():
    if 'loggedin' in session:
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
            categories_row = cursor.fetchall()
            response = jsonify(categories_row)
            response.status_code = 200
            pd_object = json_normalize(categories_row)
            temp = pd_object.to_dict('records')
            column_names = pd_object.columns.values
            return render_template('record.html', records=temp, colnames=column_names)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/top-10-customers-monthly', methods=['GET'])
def show_top_customers_monthly():
    if 'loggedin' in session:
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
            categories_row = cursor.fetchall()
            response = jsonify(categories_row)
            response.status_code = 200
            pd_object = json_normalize(categories_row)
            temp = pd_object.to_dict('records')
            column_names = pd_object.columns.values
            return render_template('record.html', records=temp, colnames=column_names)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/most-sold-products-weekly', methods=['GET'])
def show_most_sold_products_weekly():
    if 'loggedin' in session:
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
            categories_row = cursor.fetchall()
            response = jsonify(categories_row)
            response.status_code = 200
            pd_object = json_normalize(categories_row)
            temp = pd_object.to_dict('records')
            column_names = pd_object.columns.values
            return render_template('record.html', records=temp, colnames=column_names)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/most-sold-products-monthly', methods=['GET'])
def show_most_sold_products_monthly():
    if 'loggedin' in session:
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
            categories_row = cursor.fetchall()
            response = jsonify(categories_row)
            response.status_code = 200
            pd_object = json_normalize(categories_row)
            temp = pd_object.to_dict('records')
            column_names = pd_object.columns.values
            return render_template('record.html', records=temp, colnames=column_names)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/special-offers', methods=['GET'])
def show_special_offers():
    if 'loggedin' in session:
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
            categories_row = cursor.fetchall()
            response = jsonify(categories_row)
            response.status_code = 200
            pd_object = json_normalize(categories_row)
            temp = pd_object.to_dict('records')
            column_names = pd_object.columns.values
            return render_template('record.html', records=temp, colnames=column_names)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/show-provider', methods=['GET'])
def show_provider():
    if 'loggedin' in session:
        if 'admin' in session:
            try:
                product_name = request.args['product']
                if product_name and request.method == 'GET':
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    query = '''
                        CALL showInStockBranches(%s);
                    '''
                    # bindData = (_name, _email, _phone, _address)
                    cursor.execute(query, product_name)
                    # conn.commit()
                    provider_row = cursor.fetchall()
                    response = jsonify(provider_row)
                    response.status_code = 200
                    pd_object = json_normalize(provider_row)
                    temp = pd_object.to_dict('records')
                    column_names = pd_object.columns.values
                    return render_template('record.html', records=temp, colnames=column_names)
                else:
                    return show_message()
            except Exception as e:
                print(e)
            finally:
                cursor.close()
                conn.close()
        else:
            response = jsonify('only accessible by admin!')
            response.status_code = 403
            return response
    else:
        return redirect(url_for('login'))


@app.route('/show-cheapest-provider', methods=['GET'])
def show_cheapest_provider():
    if 'loggedin' in session:
        if 'admin' in session:
            try:
                # _json = request.json
                # product_name = _json['product']
                product_name = request.args['product']
                if product_name and request.method == 'GET':
                    print(product_name)
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    query = '''
                        CALL showChipestProvider(%s);
                    '''
                    # bindData = (_name, _email, _phone, _address)
                    cursor.execute(query, product_name)
                    # conn.commit()
                    provider_row = cursor.fetchall()
                    response = jsonify(provider_row)
                    response.status_code = 200
                    pd_object = json_normalize(provider_row)
                    temp = pd_object.to_dict('records')
                    column_names = pd_object.columns.values
                    return render_template('record.html', records=temp, colnames=column_names)
                else:
                    return show_message()
            except Exception as e:
                print(e)
            finally:
                cursor.close()
                conn.close()
        else:
            response = jsonify('only accessible by admin!')
            response.status_code = 403
            return response
    else:
        return redirect(url_for('login'))


@app.route('/last-ten-orders', methods=['GET'])
def show_last_ten_orders():
    if 'loggedin' in session:
        try:
            username = request.args['user']
            if username and request.method == 'GET':
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = '''
                    CALL showTenLastPurchases(%s);
                '''
                # bindData = (_name, _email, _phone, _address)
                cursor.execute(query, username)
                # conn.commit()
                users_row = cursor.fetchall()
                response = jsonify(users_row)
                response.status_code = 200
                pd_object = json_normalize(users_row)
                temp = pd_object.to_dict('records')
                column_names = pd_object.columns.values
                return render_template('record.html', records=temp, colnames=column_names)
            else:
                return show_message()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/comments', methods=['GET'])
def show_comments():
    if 'loggedin' in session:
        try:
            # _json = request.json
            # product_name = _json['product']
            product_name = request.args['product']
            if product_name and request.method == 'GET':
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = '''
                    CALL showProductComments(%s)
                '''
                # bindData = (_name, _email, _phone, _address)
                cursor.execute(query, product_name)
                # conn.commit()
                users_row = cursor.fetchall()
                response = jsonify(users_row)
                response.status_code = 200
                pd_object = json_normalize(users_row)
                temp = pd_object.to_dict('records')
                column_names = pd_object.columns.values
                return render_template('record.html', records=temp, colnames=column_names)
            else:
                return show_message()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/top-comments', methods=['GET'])
def show_top_comments():
    if 'loggedin' in session:
        try:
            # _json = request.json
            # product_name = _json['product']
            product_name = request.args['product']
            if product_name and request.method == 'GET':
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = '''
                    CALL showProductHighestRatingComments(%s);
                '''
                # bindData = (_name, _email, _phone, _address)
                cursor.execute(query, product_name)
                # conn.commit()
                users_row = cursor.fetchall()
                response = jsonify(users_row)
                response.status_code = 200
                pd_object = json_normalize(users_row)
                temp = pd_object.to_dict('records')
                column_names = pd_object.columns.values
                return render_template('record.html', records=temp, colnames=column_names)
            else:
                return show_message()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/worst-comments', methods=['GET'])
def show_worst_comments():
    if 'loggedin' in session:
        try:
            # _json = request.json
            # product_name = _json['product']
            product_name = request.args['product']
            if product_name and request.method == 'GET':
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = '''
                    CALL showProductLowestRatingComments(%s);
    
                '''
                # bindData = (_name, _email, _phone, _address)
                cursor.execute(query, product_name)
                # conn.commit()
                users_row = cursor.fetchall()
                response = jsonify(users_row)
                response.status_code = 200
                pd_object = json_normalize(users_row)
                temp = pd_object.to_dict('records')
                column_names = pd_object.columns.values
                return render_template('record.html', records=temp, colnames=column_names)
            else:
                return show_message()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/total-sold', methods=['GET'])
def show_total_sold():
    if 'loggedin' in session:
        if 'admin' in session:
            try:
                product_name = request.args['product']
                if product_name and request.method == 'GET':
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    query = '''
                        CALL showProductMontlySalesReport(%s);
                    '''
                    # bindData = (_name, _email, _phone, _address)
                    cursor.execute(query, product_name)
                    # conn.commit()
                    users_row = cursor.fetchall()
                    response = jsonify(users_row)
                    response.status_code = 200
                    pd_object = json_normalize(users_row)
                    temp = pd_object.to_dict('records')
                    column_names = pd_object.columns.values
                    return render_template('record.html', records=temp, colnames=column_names)
                else:
                    return show_message()
            except Exception as e:
                print(e)
            finally:
                cursor.close()
                conn.close()
        else:
            response = jsonify('only accessible by admin!')
            response.status_code = 403
            return response
    else:
        return redirect(url_for('login'))


@app.route('/average-income', methods=['GET'])
def show_average_income():
    if 'loggedin' in session:
        if 'admin' in session:

            try:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = '''
                    SELECT AVG(sold) avg_sold_per_day
                    FROM 
                    (SELECT receipts.date, SUM(sell_price) AS sold
                    FROM products, receipts
                    WHERE (products.receipt_id = receipts.receipt_id) & (DATEDIFF(CURDATE(), receipts.date) <= 30)
                    GROUP BY receipts.date
                    ) AS daily_revenue;
                '''

                cursor.execute(query)
                # conn.commit()
                income = cursor.fetchall()
                response = jsonify(income)
                response.status_code = 200
                pd_object = json_normalize(income)
                temp = pd_object.to_dict('records')
                column_names = pd_object.columns.values
                return render_template('record.html', records=temp, colnames=column_names)
            except Exception as e:
                print(e)
            finally:
                cursor.close()
                conn.close()
        else:
            response = jsonify('only accessible by admin!')
            response.status_code = 403
            return response
    else:
        return redirect(url_for('login'))


@app.route('/city-customers', methods=['GET'])
def show_city_customers():
    if 'loggedin' in session:

        try:
            city_name = request.args['city']
            if city_name and request.method == 'GET':
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = '''
                    CALL showCityCustomers(%s);
                '''
                # bindData = (_name, _email, _phone, _address)
                cursor.execute(query, city_name)
                # conn.commit()
                customer_row = cursor.fetchall()
                response = jsonify(customer_row)
                response.status_code = 200
                pd_object = json_normalize(customer_row)
                temp = pd_object.to_dict('records')
                column_names = pd_object.columns.values
                return render_template('record.html', records=temp, colnames=column_names)
            else:
                return show_message()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


@app.route('/providers-in-city', methods=['GET'])
def show_providers_in_city():
    if 'loggedin' in session:

        try:
            city_name = request.args['city']
            if city_name and request.method == 'GET':
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                query = '''
                    CALL showCityBranches(%s);
                '''
                # bind_data = (city_name, product_name)
                cursor.execute(query, city_name)
                # conn.commit()
                customer_row = cursor.fetchall()
                response = jsonify(customer_row)
                response.status_code = 200
                pd_object = json_normalize(customer_row)
                temp = pd_object.to_dict('records')
                column_names = pd_object.columns.values
                return render_template('record.html', records=temp, colnames=column_names)
            else:
                return show_message()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return redirect(url_for('login'))


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
