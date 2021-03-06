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

-- refactor

SELECT COUNT( name) AS products, country 
FROM products
WHERE country IN ('United States of America', 'Canada')
GROUP BY country
ORDER BY 1 DESC;


SELECT name, greeting, SUBSTRING(greeting, LOCATE('#', greeting) + 1, LENGHT(greeting))
FROM greetings;