# Salaries and Experience

import pprint

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

print(len(salaries_and_tenures))
pprint.pprint(salaries_and_tenures)

""" tried with bashplotlib without success
with open('/tmp/tmp1', 'w') as f:
    for item in salaries_and_tenures:
        withcomma = "%d, %d\n" % (item[0], item[1])
        f.write(withcomma)

# draw on the command line
from bashplotlib.scatterplot import plot_scatter
#from bashplotlib.scatterplot import plot_scatter
#with open('/tmp/tmp1','r') as f:
#    plot_scatter(f)
plot_scatter('/tmp/tmp1')
"""

import matplotlib.pyplot as plt

y,x = zip(*salaries_and_tenures)
fig, ax = plt.subplots( nrows=1, ncols=1  )  # create figure & 1 axis
ax.scatter(x, y)
fig.savefig('sal1.png')   # save the figure to file
plt.close(fig)    # close the figure
