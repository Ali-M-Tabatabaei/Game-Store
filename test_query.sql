SELECT customer.username, customer.id, SUM(receipt.total_price) as spent
    FROM (SELECT customer.id, receipt.total_price
        FROM customer, receipt
        WHERE customer.id = receipt.receiptid  & DATEDIFF(curdate(), receipt.date) < 7 )
        GROUP BY customer.username
        ORDER BY DESC spent LIMIT 10


    SELECT product.name, count(*) as count
        FROM product, receipt
        WHERE DATEDIFF(curdate(), receipt.date) < 7 & product.isSold = 1 & product.receipt_receiptid = receipt.receiptid
        GROUP BY product.name
        ORDER BY DESC count 


SELECT name, SUM(sell_price) AS sold FROM
    (SELECT * FROM products WHERE receipt_id IS NOT NULL) AS sold_products
GROUP BY name ORDER BY sold DESC;

SELECT * FROM products WHERE receipt_id IS NOT NULL

SELECT * FROM receipts,
(SELECT * FROM products WHERE receipt_id IS NOT NULL) AS sold_products
WHERE (sold_products.receipt_id = receipts.receipt_id) & (DATEDIFF(CURDATE(), receipts.date) < 7)

SELECT name, SUM(sell_price) AS sold FROM
    (SELECT name, sell_price FROM receipts,
        (SELECT * FROM products WHERE receipt_id IS NOT NULL ) AS sold_products
    WHERE (sold_products.receipt_id = receipts.receipt_id) & (DATEDIFF(CURDATE(), receipts.date) < 7)
    ) AS weekly_products
GROUP BY name ORDER BY sold DESC;

SELECT name, SUM(sell_price) AS sold FROM
    (SELECT name, sell_price FROM receipts,
        (SELECT * FROM products WHERE receipt_id IS NOT NULL ) AS sold_products
    WHERE (sold_products.receipt_id = receipts.receipt_id) & (DATEDIFF(CURDATE(), receipts.date) < 30)
    ) AS weekly_products
GROUP BY name ORDER BY sold DESC;