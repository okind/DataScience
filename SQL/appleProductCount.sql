# Find the number of Apple product users and the number of total users with a device and group the counts by language.
# Assume Apple products are only MacBook-Pro, iPhone 5s, and iPad-air. Output the language along with the total number of Apple users and users with any device. Order your results based on the number of total users in descending order.

select u.language ,count(distinct u.user_id) ,
count(distinct case when device in ('macbook pro','iphone 5s', 'ipad air') 
               then u.user_id 
               else NULL 
               end)
from playbook_users u
join playbook_events e
on u.user_id = e.user_id
group by u.language