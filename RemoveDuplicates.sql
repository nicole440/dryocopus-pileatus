CREATE OR REPLACE FUNCTION remove_duplicates()
RETURNS void AS 
$$
BEGIN
    -- Create: temporary table to hold unique observations
    CREATE TEMP TABLE temp_unique_observations AS
    SELECT DISTINCT ON (submission_id, observation_date, common_name) *
    FROM recent_observations
    ORDER BY observation_date, common_name DESC;

    -- Clear: original table and re-insert unique observations
    DELETE FROM recent_observations;
    INSERT INTO recent_observations SELECT * FROM temp_unique_observations;

    -- Clean up: drop the temporary table
    DROP TABLE temp_unique_observations;
END;
$$
LANGUAGE plpgsql;