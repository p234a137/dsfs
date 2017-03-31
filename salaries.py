# Salaries and Experience

import pprint

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

print(len(salaries_and_tenures))
pprint.pprint(salaries_and_tenures)


# Make a plot
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
# use matplotlib
import matplotlib.pyplot as plt
y,x = zip(*salaries_and_tenures)
fig, ax = plt.subplots( nrows=1, ncols=1  )  # create figure & 1 axis
ax.scatter(x, y)
fig.savefig('sal1.png')   # save the figure to file
plt.close(fig)    # close the figure


# keys are years, values are lists of the salaries for each tenure
from collections import defaultdict
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
    
# keys are years, each value is the average salary for that tenure
average_salary_by_tenure = {
        tenure: sum(salaries) / len(salaries)
        for tenure, salaries in salary_by_tenure.items()
        }

print("\nAverage Salary by Tenure Year:")
pprint.pprint(average_salary_by_tenure)


# It is probably better to bucket the tenures
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# keys are tenure buckets, values are average salary for that bucket
average_salary_by_tenure_bucket = {
        tenure_bucket: sum(salaries) / len(salaries)
        for tenure_bucket, salaries in salary_by_tenure_bucket.items()
        }

print("\nAverage Salary by Tenure Bucket:")
pprint.pprint(average_salary_by_tenure_bucket)
