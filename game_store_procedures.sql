

CREATE PROCEDURE showInStockBranches(IN product_name VARCHAR(100))
BEGIN
    SELECT DISTINCT sales_branches.name as branch_name, sales_branches.city as city 
    FROM products, sales_branches
    WHERE (products.branch_id = sales_branches.branch_id) &
    (products.name = product_name);
END;


CREATE PROCEDURE showChipestProvider(IN product_name VARCHAR(100))
BEGIN
    SELECT sales_branches.name as branch_name, products.sell_price
    FROM sales_branches, products
    WHERE (products.name = product_name) & (sales_branches.branch_id = products.branch_id)
    ORDER BY products.sell_price ASC LIMIT 1;
END;


CREATE PROCEDURE showTenLastPurchases(IN customer_id INT)
BEGIN
    SELECT receipts.date, receipts.total_price, receipts.receipt_id
    FROM receipts, customers
    WHERE (customers.id = customer_id) & (receipts.receipt_id = customers.id)
    ORDER BY DATE
    LIMIT 10;
END ;


CREATE PROCEDURE showProductComments(IN product_name VARCHAR(100))
BEGIN
SELECT comments.comment_id, comments.content, comments.likes, comments.dislikes
FROM comments, 
    (SELECT comment_id
    FROM product_has_comment, products
    WHERE (products.name = product_name) & (products.product_code = product_has_comment.product_code)) AS product_comments_ids
WHERE comments.comment_id = product_comments_ids.comment_id;
END;


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
END;


CREATE PROCEDURE showProductLowestRatingComments(IN product_name VARCHAR(100))
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
END;


CREATE PROCEDURE showProductMontlySalesReport(IN product_name VARCHAR(100))
BEGIN
    SELECT receipts.date, products.sell_price AS sold_price
    FROM products, receipts
    WHERE (products.name = product_name) & (products.receipt_id = receipts.receipt_id) &
        (DATEDIFF(CURDATE(), receipts.date) <= 30)
    ORDER BY date DESC;
END;


CREATE PROCEDURE showCityCustomers(IN city_name VARCHAR(50))
BEGIN
    SELECT * FROM customers
    WHERE city = city_name;
END;


CREATE PROCEDURE showCityBranches(IN city_name VARCHAR(50))
BEGIN
    SELECT name, address, phonenumber 
    FROM sales_branches
    WHERE city = city_name;
END;
