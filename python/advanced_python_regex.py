import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import os

data = pd.read_csv('faculty.csv')
data.columns = [i.strip() for i in data.columns]


def plot_a_counter (c,label=''):
	x_labels = [key for key in c]
	freq_series = pd.Series.from_array([c.get(key) for key in c])

	fig = plt.figure(figsize=(12, 8))
	ax = freq_series.plot(kind='bar')
	ax.set_title('%s%s' % ('Frequency of each ',label))
	ax.set_xlabel(label)
	ax.set_ylabel("Frequency")
	ax.set_xticklabels(x_labels,rotation='horizontal')

	rects = ax.patches

	for rect, label in zip(rects, freq_series):
	    height = rect.get_height()
	    ax.text(rect.get_x() + rect.get_width()/2, height, label, ha='center', va='bottom')
	
	return fig

def print_a_plot (fig,filename):
	wd = os.getcwd() ## should be .../dsp/python
	dsp_dir = '/'.join(wd.split('/')[:-1])
	img_dir = '%s%s' % (dsp_dir,'/img')
	if not os.path.exists('%s%s' % (img_dir,'/advanced_python_plots')):
		os.makedirs('%s%s' % (img_dir,'/advanced_python_plots'))
	path = '%s%s' % (img_dir,'/advanced_python_plots/')
	complete_name = '%s%s' % (path,filename)
	plt.savefig(complete_name)
	plt.close()

data.degree = [i.strip().replace('.','') for i in data.degree]
data.degree.iloc[data[data.degree=='0'].index] = np.nan
degrees = [j for i in data.degree if pd.notnull(i) for j in i.split()]
deg_freq = Counter(degrees)
fig = plot_a_counter(deg_freq,'Degree')
print_a_plot(fig,'degree_hist.png')

titles = [' '.join(i.split()[:-2]) for i in data.title]
titles_freq = Counter(titles)
fig = plot_a_counter(titles_freq,'Title')
print_a_plot(fig,'title_hist.png')

print data.email.tolist()

domains = [i.split('@')[1] for i in data.email]
print pd.unique(domains)
