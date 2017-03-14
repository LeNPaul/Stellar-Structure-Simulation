import numpy as np
import csv
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

#   http://stackoverflow.com/questions/7744697/how-to-show-two-figures-using-matplotlib
#   http://stackoverflow.com/questions/27083051/matplotlib-xticks-not-lining-up-with-histogram

f1 = open('wl_data_male_2000-2016.csv')
csv_f1 = csv.reader(f1)

f2 = open('wl_data_female_2000-2016.csv')
csv_f2 = csv.reader(f2)

#Skip header
next(csv_f1)
next(csv_f2)

#weight: 2
#snatch: 6
#total: 11
#clean & jerk: 10
class_colours = ['slategrey', 'crimson', 'mediumseagreen', 'dodgerblue', 'salmon', 'darkorchid', 'sienna', 'orangered']

s_data = []
cj_data = []
s_value = 6
cj_value = 10
binwidth = 1
point_size = 20

for row in csv_f1:
    s_data.append(float(row[s_value]))
    cj_data.append(float(row[cj_value]))

s_bin_size = np.arange(min(s_data), max(s_data) + binwidth, binwidth)
cj_bin_size = np.arange(min(cj_data), max(cj_data) + binwidth, binwidth)

fig1, ax1 = plt.subplots(2, 1)
ax1[0].hist(s_data, bins=s_bin_size, color='dodgerblue', edgecolor='white')
ax1[0].set_title('Distribution of Final Successful Snatch for Males at the Olympics (2000 - 2016)')
ax1[0].set_xlabel('Weight (Kg)')
ax1[0].set_ylabel('Number of Lifts')
ax1[1].hist(cj_data, bins=cj_bin_size+0.5, color='dodgerblue', edgecolor='white')
ax1[1].set_title('Distribution of Final Successful Clean & Jerk for Males at the Olympics (2000 - 2016)')
ax1[1].set_xlim(100,270)
ax1[1].set_xlabel('Weight (Kg)')
ax1[1].set_ylabel('Number of Lifts')

s_data = []
cj_data = []

for row in csv_f2:
    s_data.append(float(row[s_value]))
    cj_data.append(float(row[cj_value]))

s_bin_size = np.arange(min(s_data), max(s_data) + binwidth, binwidth)
cj_bin_size = np.arange(min(cj_data), max(cj_data) + binwidth, binwidth)

fig2, ax2 = plt.subplots(2, 1)
ax2[0].hist(s_data, bins=s_bin_size+0.5, color='dodgerblue', edgecolor='white')
ax2[0].set_xlim(45,155)
ax2[0].set_title('Distribution of Final Successful Snatch for Females at the Olympics (2000 - 2016)')
ax2[0].set_xlabel('Weight (Kg)')
ax2[0].set_ylabel('Number of Lifts')
ax2[1].hist(cj_data, bins=cj_bin_size+0.5, color='dodgerblue', edgecolor='white')
ax2[1].set_xlim(60,195)
ax2[1].set_title('Distribution of Final Successful Clean & Jerk for Females at the Olympics (2000 - 2016)')
ax2[1].set_xlabel('Weight (Kg)')
ax2[1].set_ylabel('Number of Lifts')


plt.show()
