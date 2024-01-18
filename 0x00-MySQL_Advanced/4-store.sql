-- create a trigger
-- this trigger triggers an operation when a sql execution occurs

CREATE TRIGGER firs_trg AFTER INSERT ON orders
FOR EACH ROW
UPDATE items  SET items.quantity = items.quantity - NEW.number
WHERE NEW.item_name = items.name;

