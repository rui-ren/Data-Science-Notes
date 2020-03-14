-- CASE statements

-- A CASE statement allows to map one or more condition to a 
-- corresponding value for each condition

SELECT report_code, year, month, day, wind_speed,

-- CASE is kind of like a conditional if loop
CASE
	WHEN wind_speed >= 40 THEN 'HIGH'
	WHEN wind_speed >= 30 AND wind_speed < 40 THEN 'MODERATE'
	ELSE 'LOW'
END as wind_severity

FROM station_data

-- the same syntax for the calculation

SELECT report_code, year, month, day, wind_speed,

-- CASE is kind of like a conditional if loop
CASE
	WHEN wind_speed >= 40 THEN 'HIGH'
	WHEN wind_speed >= 30 THEN 'MODERATE'
	ELSE 'LOW'
END as wind_severity

FROM station_data

-- CASE 

SELECT year, month,
SUM(precipitation) as tornado_precipitation
FROM state_data
WHERE tornado = 1
GROUP BY year, month

-- CASE

SELECT year, month,
SUM(precipitation) as tornado_precipitation
FROM station_data
WHERE tornado = 1
GROUP BY year, month

-- CASE II

SELECT year, month,
SUM(precipitation) as non_tornado_precipitation
FROM station_data
WHERE tornado = 0
GROUP BY year, month


-- CASE
SELECT year, month,
SUM(CASE WHEN tornado = 1 THEN precipitation ELSE 0 END) as tornado_precipitation,
SUM(CASE WHEN tornado = 0 THEN precipitation ELSE 0 END) as non_tornado_precipitation

FROM station_data
GROUP BY year, month

-- CASE
SELECT year,

MAX(CASE WHEN tornado = 0 THEN precipitation ELSE NULL END) as
	max_non_tornado_precipitation,

MAX(CASE WHEN tornado = 1 THEN precipitation ELSE NULL END) as
	max_tornado_precipitation

FROM station_data
GROUP BY year


SELECT month,

AVG(CASE WHEN rain OR hail THEN temperature ELSE NULL END)
AS avg_precipitation_temp,

AVG(CASE WHEN NOT(rain OR hail) THEN temperature ELSE NULL END)
AS avg_non_precipitation_temp

FROM station_data
WHERE year > 2000
GROUP BY month











