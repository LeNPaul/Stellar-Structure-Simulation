import numpy as np
import csv
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

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
x_value = 9
y_value = 10

class_colours = ['slategrey', 'crimson', 'mediumseagreen', 'dodgerblue', 'salmon', 'darkorchid', 'sienna', 'orangered']

for row in csv_f:
    if row[x_value] == '' or row[y_value] == '':
        pass
    else:
        x_data.append(float(row[x_value]))
        y_data.append(float(row[y_value]))

plt.scatter(x_data, y_data, marker='o', s=point_size,c='dodgerblue', edgecolor='none')

#plt.title('')
#plt.xlabel('')
#plt.ylabel('')

#coefficients = np.polyfit(x_data, y_data, 1) #before: 3
#polynomial = np.poly1d(coefficients)
#x_data.sort()
#ys = polynomial(x_data)

#plt.plot(x_data,ys, c='black')

#plt.grid(b=True, which='both', color='0.25',linestyle='-')

plt.show()
