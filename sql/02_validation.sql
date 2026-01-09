-- 1) Duplicates (should return 0 rows)
SELECT order_id, COUNT(*) AS cnt
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;

-- 2) Missing required fields (should return 0 rows)
SELECT *
FROM orders
WHERE order_id IS NULL OR TRIM(order_id) = ''
    OR customer_id IS NULL OR TRIM(customer_id) = ''
    OR order_date IS NULL OR TRIM(order_date) = ''
    OR product_name IS NULL OR TRIM(product_name) = ''
    OR product_category IS NULL OR TRIM(product_category) = ''
    OR city IS NULL OR TRIM(city) = ''
    OR channel IS NULL OR TRIM(channel) = '';

-- 3) Invalid numbers (should return 0 rows)
SELECT *
FROM orders
WHERE quantity <= 0 OR unit_price < 0 OR amount < 0;

-- 4) Amount mismatch (should return 0 rows)
SELECT order_id, quantity, unit_price, amount,
       ROUND(quantity * unit_price, 2) AS expected_amount
FROM orders
WHERE ABS(ROUND(quantity * unit_price, 2) - ROUND(amount, 2)) > 0.01;

-- 5) Date format sanity (should return 0 rows)
SELECT order_id, order_date
FROM orders
WHERE LENGTH(order_date) != 10;
