
-- =====================================================
-- DAY 8: SQL FUNDAMENTALS
-- Database: day8_database
-- Tool: MySQL using XAMPP/phpMyAdmin
-- =====================================================

-- Query 1: Retrieve all customer records.
-- Explanation: Displays all columns and rows from Customers.
SELECT *
FROM Customers;

-- Query 2: Retrieve specific customer details.
-- Explanation: Displays only customer IDs and names.
SELECT CustomerID, CustomerName
FROM Customers;

-- Query 3: Filter customers by city.
-- Explanation: Retrieves customers who live in Pune.
SELECT *
FROM Customers
WHERE City = 'Pune';

-- Query 4: Sort products by price.
-- Explanation: Displays products from highest to lowest price.
SELECT ProductName, Price
FROM Products
ORDER BY Price DESC;

-- Query 5: Retrieve unique customer cities.
-- Explanation: Displays each city only once.
SELECT DISTINCT City
FROM Customers;

-- Query 6: Filter products by price.
-- Explanation: Retrieves products costing more than 1000.
SELECT ProductName, Price
FROM Products
WHERE Price > 1000;

-- Query 7: Use column aliases.
-- Explanation: Assigns readable temporary column names.
SELECT ProductName AS Item_Name,
       Price AS Product_Price
FROM Products;

-- Query 8: Identify missing email values.
-- Explanation: Finds customers whose email is NULL.
SELECT *
FROM Customers
WHERE Email IS NULL;

-- Query 9: Filter sales by quantity.
-- Explanation: Retrieves sales with quantity of at least five.
SELECT *
FROM Sales
WHERE Quantity >= 5;

-- Query 10: Apply multiple filtering conditions.
-- Explanation: Both conditions must be satisfied.
SELECT *
FROM Sales
WHERE Quantity >= 5
  AND TotalAmount > 1000;

-- Query 11: Filter products within a price range.
-- Explanation: Includes prices from 500 to 2000.
SELECT ProductName, Price
FROM Products
WHERE Price BETWEEN 500 AND 2000;

-- Query 12: Retrieve the five highest-priced products.
-- Explanation: Sorts prices descending and returns five rows.
SELECT ProductName, Price
FROM Products
ORDER BY Price DESC
LIMIT 5;

-- Query 13: Retrieve customers with available email values.
-- Explanation: Excludes customers whose email is NULL.
SELECT CustomerID, CustomerName, Email
FROM Customers
WHERE Email IS NOT NULL;
