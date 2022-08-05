-- 2.1
SELECT
    name
FROM
    records
WHERE
    Supervisor = "Oliver Warbucks";

-- 2.2
SELECT
    *
FROM
    records
WHERE
    Supervisor = name;

-- 2.3
SELECT
    name
FROM
    records
WHERE
    salary > 50000
Order by
    name;

-- 3.1
SELECT
    day,
    time
FROM
    records,
    meetings
WHERE
    Supervisor = "Oliver Warbucks";

-- 3.2
SELECT
    r1.name,
    r2.name
FROM
    records AS r1,
    records AS r2,
    meetings AS m1,
    meetings AS m2
WHERE
    r1.division = m1.division
    AND r2.division = m2.division
    AND m1.time = m2.time
    AND m1.day = m2.day
    AND r1.name < r2.name;

-- 3.3
-- No - if a department has multiple meetings, then all pairs of individuals within that
-- department will be listed multiple times. To avoid this, we can use the DISTINCT
-- keyword.

-- 3.4
SELECT
    r1.name
FROM
    records AS r1,
    records AS r2
WHERE
    r1.supervisor = r2.name
    AND r1.division != r2.division;

-- 4.1
SELECT
    supervisor,
    SUM(salary)
FROM
    records
GROUP BY
    supervisor;

-- 4.2
SELECT
    m.day
FROM
    records AS r,
    meetings AS m
WHERE
    r.division = m.division
GROUP BY
    m.day
HAVING
    COUNT(*) < 5;

-- 4.3
SELECT
    r1.division
FROM
    records AS r1,
    records AS r2
WHERE
    r1.name != r2.name
    AND r1.division = r2.division
GROUP BY
    r1.division
HAVING
    MAX(r1.salary + r2.salary) < 100000;

-- 15 rows
-- 5.1
CREATE TABLE num_taught AS
SELECT
    professor,
    course,
    count(*) AS times
FROM
    courses
GROUP BY
    professor,
    course;

-- 5.2
SELECT
    n1.professor,
    n2.professor,
    n1.course
FROM
    num_taught AS n1,
    num_taught AS n2
WHERE
    n1.professor < n2.professor
    AND n1.course = n2.course
    AND n1.times = n2.times;

-- 5.3
SELECT
    c1.professor,
    c2.professor
FROM
    courses AS c1,
    courses AS c2
WHERE
    c1.professor < c2.professor
    AND c1.semester = c2.semester
    and c1.course = c2.course
GROUP BY
    c1.course,
    c1.professor,
    c2.professor
HAVING
    COUNT(*) > 1;