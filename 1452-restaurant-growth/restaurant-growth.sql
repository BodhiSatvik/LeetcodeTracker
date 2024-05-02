# Write your MySQL query statement below
with all_amt as (
    select visited_on, sum(amount) total
    from customer
    group by visited_on
    ),
rolling as (
    select  visited_on,
            round(sum(total) over (order by visited_on rows between 6 preceding and current row), 2) as amount,
            round(avg(total) over (order by visited_on rows between 6 preceding and current row), 2) as average_amount
    from all_amt
)

select * 
from rolling
where visited_on >= (select visited_on from customer order by visited_on limit 1) + 6
order by visited_on