--NO.1 SELECT
-- query
SELECT PRODUCT_ID,
DESCRIPTION,
PRICE AS UNITAXED_PRICE,
round(PRICE*1.07) AS TAXED_PRICE
FROM PRODUCT;

-- text concatenation
SELECT NAME,
STREET_ADDRESS|| ',' || CITY || ',' || STATE AS LOCATION
FROM CUSTOMER;

-- select statement retrieves and transforms data from a table
-- without affecting the table itself

-- NO.2 WHERE --> A method of filtering
SELECT * FROM station_data;
SELECT * FROM station_data
WHERE year = 2010

SELECT * FROM station_data
WHERE year != 2010

SELECT * FROM station_data
WHERE year <> 2010

SELECT * FROM station_data
WHERE year BETWEEN 2005 and 2010

-- Multiple solution
SELECT * FROM station_data
WHERE MONTH = 3
OR MONTH = 6
OR MONTH = 9
OR MONTH = 12

SELECT * FROM station_data
WHERE MONTH IN (3, 6, 9, 12)

SELECT * FROM station_data
WHERE MONTH NOT IN (3, 6, 9, 12)

-- we can also add mathmatical formula into where

SELECT * FROM station_data
WHERE MONTH % 3 = 0

SELECT * FROM station_data
WHERE report_code IN ('513A63','1F8A7B','EF616A')

SELECT * FROM station_data
WHERE length(report_code) != 6

--% is any number of character
SELECT * FROM station_data
WHERE report_code LIKE 'A%'

--_ is a only one number of character
SELECT * FROM station_data
WHERE report_code LIKE 'B_C%'

-- WORK ON Boolean data
SELECT * FROM station_data
WHERE tornado = true AND hail = true


SELECT * FROM station_data
WHERE tornado AND hail

SELECT * FROM station_data
WHERE tornado = 0 AND hail = 1

SELECT * FROM station_data
WHERE NOT tornado AND hail;


SELECT * FROM station_data
WHERE precipitation IS NULL OR precipitation <= 0.5

SELECT * FROM station_data
WHERE coalesce(precipitation, 0) <= 0.5;






