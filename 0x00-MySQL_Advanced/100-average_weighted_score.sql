-- create a trigger
-- this trigger triggers an operation when a sql execution occurs

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE weight_avg FLOAT;
	DECLARE aver INT;
	
	SELECT SUM(weight) INTO aver FROM projects;
	SELECT SUM(derived.score * derived.weigh / aver) INTO weight_avg
	FROM (
		SELECT corrections.score AS score, projects.weight AS weigh
		FROM corrections INNER JOIN projects
		ON corrections.project_id = projects.id
		WHERE user_id = corrections.user_id
		GROUP BY corrections.score, projects.weight
	) AS derived;
	UPDATE users SET users.average_score = weight_avg WHERE users.id = user_id;
END;
$$
DELIMITER ;

