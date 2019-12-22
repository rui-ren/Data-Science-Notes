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