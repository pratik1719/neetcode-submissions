-- Write your query below
SELECT 
    c.customer_id, 
    c.customer_name
FROM customers c
JOIN orders o 
    ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, 
    c.customer_name
HAVING 
    BOOL_OR(o.product_name = 'A')
    AND BOOL_OR(o.product_name = 'B') 
    AND NOT BOOL_OR(o.product_name = 'C')
ORDER by c.customer_name

