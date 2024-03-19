# Write your MySQL query statement below
with start as (
    select activity_type a, machine_id m, process_id p, timestamp t
    from Activity
    where activity_type = 'start'
), 
end as (
    select activity_type a, machine_id m, process_id p, timestamp t
    from Activity
    where activity_type = 'end'
)

select start.m machine_id, round(sum(end.t - start.t) / count(start.m), 3) processing_time from start
join end
on start.m=end.m and start.p=end.p
group by start.m