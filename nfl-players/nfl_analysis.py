import numpy as np
import csv
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

#   http://stackoverflow.com/questions/20105364/how-can-i-make-a-scatter-plot-colored-by-density-in-matplotlib
#   http://stackoverflow.com/questions/24119920/how-to-plot-a-density-map-in-python

f = open('nfl_data.csv')
csv_f = csv.reader(f)

#Skip header
next(csv_f)

#weight: 2
#snatch: 6
#total: 11
#clean & jerk: 10

x_data = []
y_data = []
point_size = 20
x_value = 9 #Height: 4
y_value = 10 #Weight:5, Vert jump: 9, Broad jump: 10

class_colours = ['slategrey', 'crimson', 'mediumseagreen', 'dodgerblue', 'salmon', 'darkorchid', 'sienna', 'orangered']

for row in csv_f:
    if row[x_value] == '' or row[y_value] == '':
        pass
    else:
        x_data.append(float(row[x_value]))
        y_data.append(float(row[y_value]))

# Calculate the point density
xy = np.vstack([x_data,y_data])
z = gaussian_kde(xy)(xy)

plt.scatter(x_data, y_data, marker='o', s=point_size,c=z, edgecolor='none')

plt.title('Vertical Jump vs. Broad Jump of NFL Athletes')
plt.xlabel('Vertical Jump (in)')
plt.ylabel('Broad Jump (in)')

#coefficients = np.polyfit(x_data, y_data, 1) #before: 3
#polynomial = np.poly1d(coefficients)
#x_data.sort()
#ys = polynomial(x_data)

#plt.plot(x_data,ys, c='black')

#plt.grid(b=True, which='both', color='0.25',linestyle='-')

plt.show()
