select e.name from Employee e
where e.id in (select managerId
from Employee
where managerId is not null
group by managerId
having count(managerId) >= 5)