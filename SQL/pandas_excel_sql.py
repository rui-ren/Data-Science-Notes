
import sqlite3
import pandas as pd

# transfer excel data to sql
# name of the xlsx. 
filename = 'workbook'
con = sqlite3.ocnnect(filename+'.db')
wb = pd.read_excel(filename+'.xlsx', sheetname=None)

for sheet in wb:
    wb[sheet].to_sql(sheet, con, index=False)
  
con.commit()
con.close()


## query the information
## query sql data to python

"""
SELECT
    country
FROM
    Population
WHERE

    population > 500000;
"""

conn = sqlite3.connect('filename'+'.db')
df = pd.read_sql_query(query, conn)

