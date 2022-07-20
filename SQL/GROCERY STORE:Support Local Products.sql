/* Order by number of products, descending.

products table schema
id
name
price
stock
producer
country
results table schema
products
country */

-- Replace with your SQL Query
SELECT COUNT(*) as products, country
FROM products p
WHERE country IN ('United States of America', 'Canada') 
group by country
order by products desc