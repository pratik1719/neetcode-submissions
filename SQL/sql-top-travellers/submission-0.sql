-- Write your query below
select u.name , COALESCE(sum(distance),0) as travelled_distance
from rides as r
right join users as u
on r.user_id = u.id
group by u.name
order by travelled_distance desc, u.name asc



