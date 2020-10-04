import pandas as pd

df = pd.read_csv("glassdoor_opm.csv")

#salary parsing (remove 'glassdoor est', k and $, average the range)
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split("(")[0])
noK_dollaSign = salary.apply(lambda x: x.replace("K", "").replace("$", ""))
min_salary = noK_dollaSign.apply(lambda x: int (x.split("-")[0]))
df['min_salary'] = min_salary
df['max_salary'] = noK_dollaSign.apply(lambda x: int (x.split("-")[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

df['job_state'] = df.apply(lambda x: x["Location"][-2:], axis=1)