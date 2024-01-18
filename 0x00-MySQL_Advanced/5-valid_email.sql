-- create a trigger
-- this trigger triggers an operation when a sql execution occurs

DELIMITER $$
CREATE TRIGGER valid_trg BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;
$$

