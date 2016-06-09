import pandas as pd

data = pd.read_csv('faculty.csv')
data.columns = [i.strip() for i in data.columns]

last_names = set(i.split()[-1] for i in data.name)
dict_q6 = {}
for last_name in last_names:
	for index, entry in data[[True if i.split()[-1]==last_name else False for i in data.name]].iterrows():
		dict_q6[last_name] = dict_q6.get(last_name,[]) + [entry.degree.strip(),' '.join(entry.title.split()[:-2]),entry.email]

print {key:dict_q6[key] for key in dict_q6.keys()[:3]}
