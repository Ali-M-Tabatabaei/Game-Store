import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request


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
        query = "select distinct name from products;"
        cursor.execute(query)
        # conn.commit()
        products_row = cursor.fetchone()
        response = jsonify(products_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/list-of-customers', methods=['GET'])
def show_customers():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "select distinct username from customers;"
        cursor.execute(query)
        # conn.commit()
        customers_row = cursor.fetchone()
        response = jsonify(customers_row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/categories', methods=['GET'])
def show_categories():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "select distinct game_type from products;"
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


@app.route('/receipts', methods=['GET'])
def show_receipts():
    #try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "select product_code, products.name, receipt_id, total_price, customer.id from products, customer, " \
                "receipt where (products.receipt_receiptid = receipt.receipt_id) & (receipt.customerid = customer.id) " \
                "group by customer.id;"
        cursor.execute(query)
        # conn.commit()
        categories_row = cursor.fetchone()
        response = jsonify(categories_row)
        response.status_code = 200
        return response
    #except Exception as e:
    #    print(e)
    #finally:
    #    cursor.close()
    #    conn.close()


@app.route('/top-10-customers-weekly', methods=['GET'])
def show_top_customers_weekly():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "select name, sum(total_price) as spent " \
                "from (select customer.username as name, receipt.total_price as total_price " \
                "from customer, receipt " \
                "where customer.id = receipt.customer_id  & datediff(curdate(), receipt.date) < 7 ) as s1 " \
                "group by name order by spent desc limit 10; "

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
        query = "select name, sum(total_price) as spent " \
                "from (select customer.username as name, receipt.total_price as total_price " \
                "from customer, receipt " \
                "where customer.id = receipt.customer_id  & datediff(curdate(), receipt.date) < 30 ) as s1 " \
                "group by name order by spent desc limit 10; "

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
        query = "select products.name, count(*) as count " \
                "from products, receipt " \
                "where datediff(curdate(), receipt.date) < 7 & products.isSold = 1 & products.receipt_id = " \
                "receipt.receipt_id " \
                "group by products.name " \
                "order by count desc;"

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
        query = "select products.name, count(*) as count " \
                "from products, receipt " \
                "where datediff(curdate(), receipt.date) < 30 & products.isSold = 1 & products.receipt_id = " \
                "receipt.receipt_id " \
                "group by products.name " \
                "order by count desc;"

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
        query = "select products.name , products.product_code " \
                "from discount, products " \
                "where discount.product_id = products.product_code & discount.percentage > 15;"

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
    try:
        _json = request.json
        product_name = _json['product']
        if product_name and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "select products.provider_name from product where product.name = \"%s\";"
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


@app.route('/show-cheapest-provider', methods=['GET'])
def show_cheapest_provider():
    try:
        _json = request.json
        product_name = _json['product']
        if product_name and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "select products.provider_name, product.sell_price as sell from product where product.name = " \
                    "\"%s\" order by desc sell;"
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


@app.route('/last-ten-orders', methods=['GET'])
def show_last_ten_orders():
    try:
        _json = request.json
        username = _json['user']
        if username and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "select product_code , products.name, receiptid , total_price, customer.id from products, " \
                    "customer, receipt where (products.receipt_receiptid = receipt.receiptid) & (receipt.customerid = " \
                    "customer.id) & cumtomer.username = \"%s\" group by receipt.receiptid order by receipt.date limit " \
                    "10;"
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


@app.route('/average-income', methods=['GET'])
def show_average_income():
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


@app.route('/city-customers', methods=['GET'])
def show_customers_in_city():
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
    app.run()
