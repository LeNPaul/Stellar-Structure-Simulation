import numpy as np
import csv
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

#   http://exoplanetarchive.ipac.caltech.edu/cgi-bin/IcePlotter/nph-icePlotInit?mode=demo&set=confirmed

f = open('open_exoplanet_catalogue_kepler.csv')
csv_f = csv.reader(f)

#Skip header
next(csv_f)

x_data = []
y_data = []
point_size = 10
x_value = 4
y_value = 3

class_colours = ['slategrey', 'crimson', 'mediumseagreen', 'dodgerblue', 'salmon', 'darkorchid', 'sienna', 'orangered']

for row in csv_f:
    if row[0][0] == '#':
        pass
    else:
        x_data.append(row[x_value])
        y_data.append(row[y_value])

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
