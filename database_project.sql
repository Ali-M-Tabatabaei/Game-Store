--Queries:
--1- show the list of products:
	--query:
     select name from products
--2- show the list of customers
	--query: 
    select username from customers
--3- show the list game types:
	--query:
     select distinct game_type from products
--4- show the list of receits 
	--query: 
    select product_code, products.name, receiptid, total_price, customer.id
		from products, customer, receipt
		where (products.receipt_receiptid = receipt.receiptid) & (receipt.customerid = customer.id)
		group by customer.id
--5- show the top 10 customers of the week:
	--query:
    select customer.username, customer.id, sum(receipt.total_price) as spent
		from (select customer.id, receipt.total_price
            from customer, receipt
			where customer.id = receipt.receiptid  & datediff(curdate(), receipt.date) < 7 )
            group by customer.username
            order by desc spent limit 10
    select customer.username, customer.id, sum(receipt.total_price) as spent
		from (select customer.id, receipt.total_price
            from customer, receipt
			where customer.id = receipt.receiptid  & datediff(curdate(), receipt.date) < 30 )
            group by customer.username
            order by desc spent limit 10

--6- show the most sold products of the week 
    select product.name, count(*) as count
        from product, receipt
        where datediff(curdate(), receipt.date) < 7 & product.isSold = 1 & product.receipt_receiptid = receipt.receiptid
        group by product.name
        order by desc count 

--7- show the list of special offers that have discount of over 15 percent 
    select product.name , product.id 
        from discount, products
        where discount.productid = product.product_code & discount.percentage > 15

--8- show the provider of a given product
    create procedure showProvider (productName)
    begin
        select products.provider_name
        from product 
        where product.name = productName 
    end
    

--9- show the list of chipest seller of a given product
     	creat proceduer showChipestProvider (productName)
     	begin
     		select products.provider_name, product.sell_price as sell
		from product
		where product.name = productName
		order by desc sell
	end
     
     

--10- show the list of products category
      select distinc game_type from products (TEKRARI)

--11- show the last 10 receits of a user
      select product_code , products.name, receiptid , total_price, customer.id
	from products, customer, receipt
	where (products.receipt_receiptid = receipt.receiptid) & (receipt.customerid = customer.id) 
	group by customer.id
	limit 10
 
--12- show the list of comment of a given product
      creat proceduer showcomments (productName)
      begin
      select comment.content, product.name
      from products, comment, product_has_comment
      where(comment.commentid = product_has_comment.comment_commentid) & (product_has_comment.product_code = products.product_code) & (product.name = productName)
      end


--13- show the top 3 comments that gave the highest point to the product

      select comment.content, product.name, product_has_comment.score as score
      from products, comment, product_has_comment
      where(comment.commentid = product_has_comment.comment_commentid) & (product_has_comment.product_code = products.product_code) & (product.name = '')
      order by desc score limit 3


--14- show the top 3 comments that gave the lowest point to the product
      select comment.content, product.name, product_has_comment.score as score
      from products, comment, product_has_comment
      where(comment.commentid = product_has_comment.comment_commentid) & (product_has_comment.product_code = products.product_code) & (product.name = '')
      order by score limit 3

--15- show the total amount of sold products
      
      select sum(products.sell_price) as totalAmount
      from products
      where product.name  = '' & product.isSold = 1 & datediff(curdate(), product.sold_date) < 30

--16- show the avr income od sold products

      select avg (products.sell_price) as totalAmount
      from products
      where product.isSold = 1 & datediff(curdate(), product.sold_date) < 30

--17- show the name of all customers in the given city
       
     select customer.name, customer.city
     from customer
     where customer.city=''

--18-show the providers of the product in the given city
     
     select product.provider_name
     from product, compny 
     where product.provider_name= compny.name & compny.city='' & product.namm=''
   
__
        
      