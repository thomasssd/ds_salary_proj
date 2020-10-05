import pandas as pd

df = pd.read_csv("glassdoor_opm.csv")

#salary parsing (remove 'glassdoor est', k and $, average the range)
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split("(")[0])
df['Salary Estimate'] = salary
noK_dollaSign = salary.apply(lambda x: x.replace("K", "").replace("$", ""))
#replace per hour(ph) and employer provided salary(eps)
noPH_EPS = noK_dollaSign. apply(lambda x: x.lower().replace("per hour", "").replace("employer provided salary:", ""))
min_salary = noPH_EPS.apply(lambda x: int (x.split("-")[0]))
df['min_salary'] = min_salary
df['max_salary'] = noPH_EPS.apply(lambda x: int (x.split("-")[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#organize by state 
df['job_state'] = df.apply(lambda x: x["Location"][-2:], axis=1)
print(df.job_state.value_counts())

df.to_csv('cleaned_opm500.csv')
