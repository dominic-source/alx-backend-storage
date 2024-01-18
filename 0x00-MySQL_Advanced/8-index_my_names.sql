-- create index
-- An index for a table creation

CREATE INDEX idx_name_first ON names (name);
UPDATE idx_name_first SET idx_name_first.name = LEFT(idx_name_first.name, 1);

