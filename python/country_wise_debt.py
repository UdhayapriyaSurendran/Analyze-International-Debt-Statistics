import pandas as pd
import numpy as np

query = "select * from all_countries1 where Country_Code like '%AFG%' "
afg_ans = pd.read_sql(query, conn)

print("Number of Distinct Countries : ",len(afg_ans))

## From 1970 to 2028
debt_years = afg_ans.iloc[:,7:66]
debt_years.head()

year_by_year = debt_years.sum() 
pd.DataFrame(year_by_year).head()

## Total Debt
year_by_year.sum()