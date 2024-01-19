-- create a procedures
-- this trigger triggers an operation when a sql execution occurs

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE aver INT;
	
	SELECT SUM(weight) INTO aver FROM projects;

	UPDATE users u
	SET u.average_score = (
        SELECT SUM(corrections.score * projects.weight / aver)
        FROM corrections 
	INNER JOIN projects
        ON corrections.project_id = projects.id
        WHERE u.id = corrections.user_id
        GROUP BY corrections.user_id
);
END;
$$
DELIMITER ;

