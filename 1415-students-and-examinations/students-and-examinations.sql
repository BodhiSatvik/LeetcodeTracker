# Write your MySQL query statement below
select s.student_id, s.student_name, u.subject_name, count(e.subject_name) attended_exams
from Students s
join Subjects u
left join Examinations e on s.student_id=e.student_id and u.subject_name=e.subject_name
group by student_id, subject_name
order by student_id, subject_name