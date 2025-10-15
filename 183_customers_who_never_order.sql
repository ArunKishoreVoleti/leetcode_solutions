-- Retrieve customers who have never placed an order
-- The subquery selects all customer IDs present in the 'orders' table
-- The outer query filters out those IDs from the 'customers' table using NOT IN
-- This returns only customers who do not appear in the 'orders' list

SELECT 
    name AS Customers
FROM 
    customers
WHERE 
    id NOT IN (
        SELECT 
            customerId 
        FROM 
            orders
    );
