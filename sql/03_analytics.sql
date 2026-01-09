-- Total orders + revenue
SELECT COUNT(*) AS total_orders,
       ROUND(SUM(amount), 2) AS total_revenue
FROM orders;

-- Revenue by day
SELECT order_date,
       ROUND(SUM(amount), 2) AS revenue
FROM orders
GROUP BY 1
ORDER BY 1;

-- Top products by revenue
SELECT product_name,
       ROUND(SUM(amount), 2) AS revenue
FROM orders
GROUP BY 1
ORDER BY revenue DESC
LIMIT 10;

-- Revenue by city
SELECT city,
        ROUND(SUM(amount), 2) AS revenue
FROM orders
GROUP BY 1
ORDER BY revenue DESC;

-- Average order value
SELECT ROUND(AVG(amount), 2) AS avg_order_value
FROM orders;

-- Orders by channel
SELECT channel, COUNT(*) AS orders
FROM orders
GROUP BY 1
ORDER BY orders DESC;
