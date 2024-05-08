# Write your MySQL query statement below
with all_days as (
    select visited_on, sum(amount) as total
    from customer
    group by visited_on
), 
rolling as (
    select visited_on, 
           round(sum(total) over (order by visited_on rows between 6 preceding and current row), 2) as amount,
           round(avg(total) over (order by visited_on rows between 6 preceding and current row), 2) as average_amount
    from all_days
    group by visited_on
    order by visited_on
)

select *
from rolling
where visited_on >= (select visited_on from customer order by visited_on limit 1) + 6
