import numpy as np
import csv
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

#   http://stackoverflow.com/questions/7744697/how-to-show-two-figures-using-matplotlib
#   http://stackoverflow.com/questions/27083051/matplotlib-xticks-not-lining-up-with-histogram

f = open('wl_data_female_2000-2016.csv')
csv_f = csv.reader(f)

#Skip header
next(csv_f)

#weight: 2
#snatch: 6
#total: 11
#clean & jerk: 10

s_data = []
cj_data = []
s_value = 6
cj_value = 10
binwidth = 1
point_size = 20

weight_classes = [ '105+' , '105' , '94' , '85' , '77' , '69' , '62' , '56' ]
class_colours = ['slategrey', 'crimson', 'mediumseagreen', 'dodgerblue', 'salmon', 'darkorchid', 'sienna', 'orangered']

for row in csv_f:
    s_data.append(float(row[s_value]))
    cj_data.append(float(row[cj_value]))

s_bin_size = np.arange(min(s_data), max(s_data) + binwidth, binwidth)
cj_bin_size = np.arange(min(cj_data), max(cj_data) + binwidth, binwidth)

'''
fig, ax = plt.subplots(2, 1)
ax[0].hist(s_data, bins=s_bin_size, color='dodgerblue', edgecolor='white')
ax[0].set_title('Snatch')
ax[1].hist(cj_data, bins=cj_bin_size, color='dodgerblue', edgecolor='white')
ax[1].set_title('Clean & Jerk')
'''

plt.hist(s_data, bins=s_bin_size, color='dodgerblue', edgecolor='white')

plt.show()
