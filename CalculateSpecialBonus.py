# Write your MySQL query statement below
# Bonus : odd number and name does not start 'M'
select employee_id, CASE when employee_id%2=1 and name not like 'M%' then salary else 0 END AS BONUS from EMployees order by employee_id