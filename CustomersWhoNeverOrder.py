select Name as Customers from Customers where id not in (select customerid from Orders)
