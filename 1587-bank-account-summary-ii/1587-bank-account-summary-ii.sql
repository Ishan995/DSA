# Write your MySQL query statement below

select u.name,
coalesce(sum(t.amount),0) as balance
from users u 
inner join transactions t 
on u.account=t.account
group by u.name 
having balance>10000
