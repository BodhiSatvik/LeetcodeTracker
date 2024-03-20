# Write your MySQL query statement below
# query quality = avg (query rating : position)
# poor query percentage = % queries with rating < 3

select query_name, round(avg(rating/position), 2) quality, round((sum(rating < 3) / count(*)) * 100, 2) poor_query_percentage
from Queries
where query_name is not null
group by query_name


