/* Write your PL/SQL query statement below */

select name as "Customers" from Customers left outer join Orders on (Customers.id = Orders.customerId) where Orders.customerId is null