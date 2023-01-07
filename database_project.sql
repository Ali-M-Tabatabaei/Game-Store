--Queries:
--1- show the list of products:
	--query:
SELECT name FROM products;
--2- show the list of customers
	--query: 
SELECT username FROM customers;
--3- show the list game types:
	--query:
SELECT DISTINCT game_type FROM products;
--4- show the list of receipts
	--query: 
SELECT * FROM receipts;
--5- show the top 10 customers of the week:
	--query:
SELECT customer_id, username, spent FROM customers,
    (SELECT customer_id, SUM(total_price) AS spent FROM 
    (SELECT * FROM receipts WHERE DATEDIFF(curdate(), date) < 7) AS T
    GROUP BY customer_id ORDER BY spent DESC LIMIT 10) AS top_customers
WHERE customers.id = top_customers.customer_id;
--5- show the top 10 customers of the month:
	--query:
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
    ) AS weekly_products
GROUP BY name ORDER BY sold DESC;

--7- show the list of special offers that have discount of over 15 percent 
    SELECT product.name , product.id 
        FROM discount, products
        WHERE discount.productid = product.product_code & discount.percentage > 15

--8- show the provider of a given product
    create procedure showProvider (productName)
    begin
        SELECT products.provider_name
        FROM product 
        WHERE product.name = productName 
    end
    

--9- show the list of chipest seller of a given product
     	creat proceduer showChipestProvider (productName)
     	begin
     		SELECT products.provider_name, product.sell_price as sell
		FROM product
		WHERE product.name = productName
		ORDER BY DESC sell
	end
     
     

--10- show the list of products category
      SELECT distinc game_type FROM products (TEKRARI)

--11- show the last 10 receits of a user
      SELECT product_code , products.name, receiptid , total_price, customer.id
	FROM products, customer, receipt
	WHERE (products.receipt_receiptid = receipt.receiptid) & (receipt.customerid = customer.id) 
	GROUP BY customer.id
	LIMIT 10
 
--12- show the list of comment of a given product
      creat proceduer showcomments (productName)
      begin
      SELECT comment.content, product.name
      FROM products, comment, product_has_comment
      WHERE(comment.commentid = product_has_comment.comment_commentid) & (product_has_comment.product_code = products.product_code) & (product.name = productName)
      end


--13- show the top 3 comments that gave the highest point to the product

      SELECT comment.content, product.name, product_has_comment.score as score
      FROM products, comment, product_has_comment
      WHERE(comment.commentid = product_has_comment.comment_commentid) & (product_has_comment.product_code = products.product_code) & (product.name = '')
      ORDER BY DESC score LIMIT 3


--14- show the top 3 comments that gave the lowest point to the product
      SELECT comment.content, product.name, product_has_comment.score as score
      FROM products, comment, product_has_comment
      WHERE(comment.commentid = product_has_comment.comment_commentid) & (product_has_comment.product_code = products.product_code) & (product.name = '')
      ORDER BY score LIMIT 3

--15- show the total amount of sold products
      
      SELECT SUM(products.sell_price) as totalAmount
      FROM products
      WHERE product.name  = '' & product.isSold = 1 & DATEDIFF(curdate(), product.sold_date) < 30

--16- show the avr income od sold products

      SELECT avg (products.sell_price) as totalAmount
      FROM products
      WHERE product.isSold = 1 & DATEDIFF(curdate(), product.sold_date) < 30

--17- show the name of all customers in the given city
       
     SELECT customer.name, customer.city
     FROM customer
     WHERE customer.city=''

--18-show the providers of the product in the given city
     
     SELECT product.provider_name
     FROM product, compny 
     WHERE product.provider_name= compny.name & compny.city='' & product.namm=''
   
__
        
      