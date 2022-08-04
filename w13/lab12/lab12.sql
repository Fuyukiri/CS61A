.read data.sql 

CREATE TABLE bluedog AS
SELECT
  color,
  pet
FROM
  students
Where
  color = "blue"
  AND pet = "dog";

CREATE TABLE bluedog_songs AS
SELECT
  color,
  pet,
  song
FROM
  students
Where
  color = "blue"
  AND pet = "dog";

CREATE TABLE smallest_int AS
SELECT
  time,
  smallest
FROM
  students
Where
  smallest > 2
Order by
  smallest
limit
  20;

CREATE TABLE matchmaker AS
SELECT
  a.pet,
  a.song,
  a.color,
  b.color
FROM
  students as a,
  students as b
WHERE
  a.time < b.time
  AND a.pet = b.pet
  AND a.song = b.song;

CREATE TABLE sevens AS
SELECT
  students.seven
FROM
  students,
  numbers
WHERE
  students.number = 7
  AND students.time = numbers.time
  AND numbers.'7' = 'True';