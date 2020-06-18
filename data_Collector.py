import web_glassDoor_Scrapper as gs
import pandas as pd

path = "/Users/aakasharora1/Desktop/ChromeDriverEXE/chromedriver"

df = gs.get_jobs('data scientist', 100, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index=False)

print(df)
