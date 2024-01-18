-- Create a table named user
-- This is the users table containing the id, email and name of users

CREATE 
OR REPLACE
VIEW my_v2 
AS SELECT origin, sum(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
SELECT * FROM my_v2;

