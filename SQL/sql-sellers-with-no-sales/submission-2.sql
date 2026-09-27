-- Write your query below
select seller_name
from seller
where seller_id not in (select s.seller_id
from orders o
join seller s
on o.seller_id = s.seller_id
where Extract(YEAR from o.sale_date) = 2020) 
-- and
-- seller_name not in
-- (select seller_name
-- from seller s
-- join orders o
-- on o.seller_id = s.seller_id
-- where Extract(YEAR from sale_date) = 2020)

order by seller_name
