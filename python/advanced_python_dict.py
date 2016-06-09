import pandas as pd

data = pd.read_csv('faculty.csv')
data.columns = [i.strip() for i in data.columns]

last_names = set(i.split()[-1] for i in data.name)
dict_q6 = {}
for last_name in last_names:
	for index, entry in data[[True if i.split()[-1]==last_name else False for i in data.name]].iterrows():
		dict_q6.setdefault(last_name,[]).append([entry.degree.strip(),' '.join(entry.title.split()[:-2]),entry.email])

print {key:dict_q6[key] for key in dict_q6.keys()[:3]}

## check to make sure there aren't two people with the same first and last name in which case the dict comprehension would fail
assert len(set((row['name'].split()[0],row['name'].split()[-1]) for index,row in data.iterrows()))==len([(row['name'].split()[0],row['name'].split()[-1]) for index,row in data.iterrows()])
dict_q7 = {(row['name'].split()[0],row['name'].split()[-1]):[row['degree'].strip(),' '.join(row['title'].split()[:-2]),row['email']] for index,row in data.iterrows()}

print {key:dict_q7[key] for key in dict_q7.keys()[:3]}

for key in sorted(dict_q7,key=lambda x: x[1]):
	print key,dict_q7[key]