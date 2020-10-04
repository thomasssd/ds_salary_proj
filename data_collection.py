import glassdoor_scraper as gs
import pandas as pd

path = "/Users/thomass/Desktop/ds_salary_proj/chromedriver"

df = gs.get_jobs('amazon operations manager', 500, False, path, 15)
df.to_csv('glassdoor_opm.csv')