/* Write your PL/SQL query statement below */

select Customers.name as "Customers" from Customers where Customers.id not in ( select customerid from orders)