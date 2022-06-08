# Write your MySQL query statement below

#find cancellation rate, compute by dividing the number of cancelled requests by client or driver by total number of requests on that day.

#exclude banned users, find rate for each day between '2013-10-01' and '2013-10-03', round cancellation rate to 2 decimal


with notbanned__users as
(
 SELECT users_id
 FROM users
 where banned = "No"
 )

SELECT  t.request_at as Day,
ROUND(SUM(
CASE
WHEN status != "completed" THEN 1
ELSE 0
END)/COUNT(*), 2) as "Cancellation Rate"
FROM Trips as t
WHERE t.request_at between '2013-10-01' and '2013-10-03' and t.client_id in (select * from notbanned__users)
and t.driver_id in (select * from notbanned__users)
GROUP BY t.request_at
