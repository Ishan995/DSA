# Write your MySQL query statement below
select p.product_id,p.product_name
from product p
where p.product_id in(
    select s.product_id 
    from sales s 
    where s.sale_date between '2019-01-01' and '2019-03-31'
)
and p.product_id not in (
    select s.product_id
    from sales s
    where s.sale_date<'2019-01-01' or s.sale_date>'2019-03-31'
)