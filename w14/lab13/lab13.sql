.read data.sql 
CREATE TABLE average_prices AS
SELECT
  category,
  avg(MSRP) AS average_price
FROM
  products
GROUP BY
  category;

CREATE TABLE lowest_prices AS
SELECT
  store,
  item,
  min(price) AS lowest_price
FROM
  inventory
GROUP BY
  item;

CREATE TABLE shopping_list AS
SELECT
  item,
  store
FROM
  lowest_prices,
  products
WHERE
  name = item
GROUP BY
  category
Having
  min(MSRP / rating);


CREATE TABLE total_bandwidth AS
SELECT
  sum(mbs)
FROM
  shopping_list AS A, stores AS B
WHERE
  A.store=B.Store;