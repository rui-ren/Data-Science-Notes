--aggregating data
/**
aggregating data is creating sort of total from a number of records
-- Sum, min, max, count, and average
**/

-- count the total rows
SELECT COUNT(*) AS record_count FROM station_data;

-- count the total rows and filtering use WHERE
SELECT year, month, COUNT(*) AS record_count FROM station_data
WHERE tornado = 1
GROUP BY year, month;

--count the total rows and filtering use WHERE -- use 1, 2 and specify the year and month
SELECT year, month, COUNT(*) AS record_count FROM station_data
WHERE tornado = 1
GROUP BY 1, 2

--ORDER BY DESC OR ASCENTING ORDER

SELECT year, month, COUNT(*) AS record_count FROM station_data
WHERE tornado = 1
GROUP BY 1, 2
ORDER BY 1 DESC, 2


-- Aggregate Functions
SELECT month, AVG(temp) as avg_temp
FROM station_data
WHERE year >= 2000
GROUP BY month;

-- SUM function

SELECT year,
SUM(snow_depth) as total_snow,
SUM(precipitation) as total_precipitation,
MAX(precipitation) as max_precipitation
FROM station_data
WHERE year > 2000
GROUP BY year


-- Having for filtering out the aggregating result

SELECT year,
SUM(precipitation) as total_precipitation
FROM station_data
GROUP BY year
HAVING total_precipitation > 30;

