-- Write your query below


select m.student_id, min(e.exam_id) as exam_id, m.score
from (select student_id , max(score) as score
from exam_results
group by student_id) as m
left join exam_results as e
on m.student_id = e.student_id and e.score = m.score 
group by m.student_id, m.score
order by student_id






