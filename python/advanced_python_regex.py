import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import os

data = pd.read_csv('faculty.csv')

data.columns = [i.strip() for i in data.columns]
data.degree = [i.strip().replace('.','') for i in data.degree]
data.iloc[data[data.degree=='0'].index] = np.nan

degrees = [j for i in data.degree if pd.notnull(i) for j in i.split()]
deg_freq = Counter(degrees)

x_labels = [key for key in deg_freq]
freq_series = pd.Series.from_array([deg_freq.get(key) for key in deg_freq])

plt.figure(figsize=(12, 8))
ax = freq_series.plot(kind='bar')
ax.set_title('Frequency of each Degree')
ax.set_xlabel('Degree')
ax.set_ylabel("Frequency")
ax.set_xticklabels(x_labels)

rects = ax.patches

for rect, label in zip(rects, freq_series):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height, label, ha='center', va='bottom')

wd = os.getcwd() ## should be .../dsp/python
dsp_dir = '/'.join(wd.split('/')[:-1])
img_dir = '%s%s' % (dsp_dir,'/img')
if not os.path.exists('/advanced_python_plots'):
	os.makedirs('%s%s' % (img_dir,'/advanced_python_plots'))
path = '%s%s' % (img_dir,'/advanced_python_plots/')
filename = 'degrees_hist.png'
complete_name = '%s%s' % (path,filename)
plt.savefig(complete_name)
plt.close()

#plt.savefig('advanced_python_regex.png')