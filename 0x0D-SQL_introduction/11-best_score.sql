-- specialized list sorted by a requirement.
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score
DESC, name;
