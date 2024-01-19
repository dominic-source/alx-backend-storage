-- create a view
-- This will create a view for a table

CREATE
OR REPLACE
VIEW need_meeting
AS SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL OR TIMESTAMPDIFF(MONTH, last_meeting, CURDATE()) > 1)

