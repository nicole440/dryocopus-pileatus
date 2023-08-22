SELECT remove_duplicates();

SELECT *
FROM recent_observations
WHERE common_name LIKE 'Pileated Woodpecker';

SELECT common_name, COUNT(common_name), submission_id
FROM recent_observations
GROUP BY recent_observations.submission_id, recent_observations.common_name;

SELECT common_name, COUNT(submission_id)
FROM recent_observations
WHERE common_name LIKE 'Pileated Woodpecker'
GROUP BY submission_id, recent_observations.common_name;

SELECT *
FROM recent_observations
WHERE submission_id LIKE 'S147816246'