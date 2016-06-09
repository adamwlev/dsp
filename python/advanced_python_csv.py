import pandas as pd

data = pd.read_csv('faculty.csv')
data.columns = [i.strip() for i in data.columns]

data.email.to_csv('emails.csv',index=False)