SELECT remove_duplicates();

SELECT *
FROM recent_observations;

-- Shows all Pileated Woodpecker observations in DB
SELECT *
FROM recent_observations
WHERE common_name LIKE 'Pileated Woodpecker'
ORDER BY submission_id;

-- Shows where there are duplicate observations based on the name and submission id
SELECT common_name, COUNT(common_name), submission_id
FROM recent_observations AS recent
GROUP BY recent.submission_id, recent.common_name
ORDER BY COUNT(common_name) DESC;

-- Shows where there are duplicates of a Pileated Woodpecker recorded observations
SELECT common_name, COUNT(submission_id)
FROM recent_observations AS recent
WHERE common_name LIKE 'Pileated Woodpecker'
GROUP BY submission_id, recent.common_name;

-- Shows all records with same submission id
SELECT *
FROM recent_observations
WHERE submission_id LIKE 'S147816246'