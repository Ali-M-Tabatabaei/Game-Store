--Queries:
--1- show the list of all products:
SELECT name FROM products;

--2- show the list of customers
SELECT username FROM customers;

--3- show the list game types:
SELECT DISTINCT game_type FROM products;

--4- show the list of receipts
SELECT * FROM receipts;

--5- show the top 10 customers of the week:
SELECT customer_id, username, spent FROM customers,
    (SELECT customer_id, SUM(total_price) AS spent FROM 
    (SELECT * FROM receipts WHERE DATEDIFF(curdate(), date) < 7) AS T
    GROUP BY customer_id ORDER BY spent DESC LIMIT 10) AS top_customers
WHERE customers.id = top_customers.customer_id;

--5- show the top 10 customers of the month:
SELECT customer_id, username, spent FROM customers,
    (SELECT customer_id, SUM(total_price) AS spent FROM 
    (SELECT * FROM receipts WHERE DATEDIFF(curdate(), date) < 30) AS T
    GROUP BY customer_id ORDER BY spent DESC LIMIT 10) AS top_customers
WHERE customers.id = top_customers.customer_id;

--6- show the best-selling products of the week 
SELECT name, SUM(sell_price) AS sold FROM
    (SELECT name, sell_price FROM receipts,
        (SELECT * FROM products WHERE receipt_id IS NOT NULL ) AS sold_products
    WHERE (sold_products.receipt_id = receipts.receipt_id) & (DATEDIFF(CURDATE(), receipts.date) < 7)
    ) AS weekly_products
GROUP BY name ORDER BY sold DESC;

--6- show the best-selling products of the month
SELECT name, SUM(sell_price) AS sold FROM
    (SELECT name, sell_price FROM receipts,
        (SELECT * FROM products WHERE receipt_id IS NOT NULL ) AS sold_products
    WHERE (sold_products.receipt_id = receipts.receipt_id) & (DATEDIFF(CURDATE(), receipts.date) < 30)
    ) AS monthly_products
GROUP BY name ORDER BY sold DESC;

--7- show the list of special offers that have discount of over 15 percent 
SELECT products.name , products.sell_price, discounts.percentage
FROM discounts, products
WHERE (discounts.product_id = products.product_code) & (discounts.percentage >= 15);

--8- show the provider of a given product
DELIMITER //

CREATE PROCEDURE showInStockBranches(IN product_name VARCHAR(100))
BEGIN
    SELECT DISTINCT sales_branches.name as branch_name, sales_branches.city as city 
    FROM products, sales_branches
    WHERE (products.branch_id = sales_branches.branch_id) &
    (products.name = product_name);
END //

DELIMITER ;

CALL showInStockBranches('xbox one');

--9- show the list of chipest seller of a given product
DELIMITER //

CREATE PROCEDURE showChipestProvider(IN product_name VARCHAR(100))
BEGIN
    SELECT sales_branches.name as branch_name, products.sell_price
    FROM sales_branches, products
    WHERE (products.name = product_name) & (sales_branches.branch_id = products.branch_id)
    ORDER BY products.sell_price ASC LIMIT 1;
END //

DELIMITER ;

CALL showChipestProvider('playstation 5');
    

--10- show the list of products category
--      SELECT distinc game_type FROM products (TEKRARI)

--11- show the last 10 receipts of a user
DELIMITER //

CREATE PROCEDURE showTenLastPurchases(IN customer_id INT)
BEGIN
    SELECT receipts.date, receipts.total_price, receipts.receipt_id
    FROM receipts, customers
    WHERE (customers.id = customer_id) & (receipts.receipt_id = customers.id)
    ORDER BY DATE
    LIMIT 10;
END //

DELIMITER ;

CALL showTenLastPurchases(1);

--12- show the list of comments of a given product
DELIMITER //

CREATE PROCEDURE showProductComments(IN product_name VARCHAR(100))
BEGIN
SELECT comments.comment_id, comments.content, comments.likes, comments.dislikes
FROM comments, 
    (SELECT comment_id
    FROM product_has_comment, products
    WHERE (products.name = product_name) & (products.product_code = product_has_comment.product_code)) AS product_comments_ids
WHERE comments.comment_id = product_comments_ids.comment_id;
END //

DELIMITER ;

CALL showProductComments('playstation 4')

--13- show the top 3 highest rating comments of a given product
DELIMITER //

CREATE PROCEDURE showProductHighestRatingComments(IN product_name VARCHAR(100))
BEGIN
    SELECT comments.comment_id, comments.content, product_comments_ratings.rating
    FROM comments, 
        (SELECT given_comments.comment_id, given_comments.rating
        FROM given_comments, 
            (SELECT comment_id
            FROM product_has_comment, products
            WHERE (products.name = product_name) & (products.product_code = product_has_comment.product_code)
            ) AS product_comments_ids
        WHERE given_comments.comment_id = product_comments_ids.comment_id
        ) AS product_comments_ratings
    WHERE comments.comment_id = product_comments_ratings.comment_id
    ORDER BY rating DESC
    LIMIT 3;
END //

DELIMITER ;

CALL showProductHighestRatingComments('CALL OF DUTY');

--14- show the top 3 lowest rating comments of a given product
DELIMITER //

CREATE PROCEDURE showProductHighestRatingComments(IN product_name VARCHAR(100))
BEGIN
    SELECT comments.comment_id, comments.content, product_comments_ratings.rating
    FROM comments, 
        (SELECT given_comments.comment_id, given_comments.rating
        FROM given_comments, 
            (SELECT comment_id
            FROM product_has_comment, products
            WHERE (products.name = product_name) & (products.product_code = product_has_comment.product_code)
            ) AS product_comments_ids
        WHERE given_comments.comment_id = product_comments_ids.comment_id
        ) AS product_comments_ratings
    WHERE comments.comment_id = product_comments_ratings.comment_id
    ORDER BY rating ASC
    LIMIT 3;
END //

DELIMITER ;

CALL showProductHighestRatingComments('CALL OF DUTY');

--15- show the monthly sales report of a given product
DELIMITER //

CREATE PROCEDURE showProductMontlySalesReport(IN product_name VARCHAR(100))
BEGIN
    SELECT receipts.date, products.sell_price AS sold_price
    FROM products, receipts
    WHERE (products.name = product_name) & (products.receipt_id = receipts.receipt_id) &
        (DATEDIFF(CURDATE(), receipts.date) <= 30)
    ORDER BY date DESC;
END //

DELIMITER ;

CALL showProductMontlySalesReport('uncharted 4')

--16- show the store's avg daily revenue in the last month
SELECT AVG(sold) avg_sold_per_day
FROM 
    (SELECT receipts.date, SUM(sell_price) AS sold
    FROM products, receipts
    WHERE (products.receipt_id = receipts.receipt_id) & (DATEDIFF(CURDATE(), receipts.date) <= 30)
    GROUP BY receipts.date
    ) AS daily_revenue;

--17- show all customers in the given city
DELIMITER //

CREATE PROCEDURE showCityCustomers(IN city_name VARCHAR(50))
BEGIN
    SELECT * FROM customers
    WHERE city = city_name;
END //

DELIMITER ;

CALL showCityCustomers('tehran');

--18- show the sales branches in a given city
DELIMITER //

CREATE PROCEDURE showCityBranches(IN city_name VARCHAR(50))
BEGIN
    SELECT name, address, phonenumber 
    FROM sales_branches
    WHERE city = city_name;
END //

DELIMITER ;

CALL showCityBranches('arak');

      