SELECT remove_duplicates();

SELECT *
FROM recent_observations;

SELECT *
FROM recent_observations
WHERE common_name LIKE 'Pileated Woodpecker'
ORDER BY submission_id;

SELECT common_name, COUNT(common_name), submission_id
FROM recent_observations AS recent
GROUP BY recent.submission_id, recent.common_name
ORDER BY COUNT(common_name) DESC;

SELECT common_name, COUNT(submission_id)
FROM recent_observations AS recent
WHERE common_name LIKE 'Pileated Woodpecker'
GROUP BY submission_id, recent.common_name;

SELECT *
FROM recent_observations
WHERE submission_id LIKE 'S147816246'