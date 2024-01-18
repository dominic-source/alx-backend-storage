-- Create a table named user
-- This is the users table containing the id, email and name of users

CREATE
OR REPLACE 
VIEW my_v3
AS SELECT band_name, IF (split IS NOT NULL, split - formed, 2022 - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
SELECT * FROM my_v3;

