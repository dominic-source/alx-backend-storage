-- create function
-- To create a function

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE div_val FLOAT;
	IF b = 0 THEN
		SET div_val = 0;
		RETURN div_val;
	END IF;
	SET div_val = a / b;
	RETURN div_val;
END $$
DELIMITER ;

