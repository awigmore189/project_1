# Project 1
# Step 1: Open the sat_scores.csv file. Investigate the data, and answer the questions below.
# 1. What does the data describe?
# The data describes SAT verbal/math scores on a state by state basis as well as the % of students who take the test
# 2. Does the data look complete? Are there any obvious issues with the observations?
#The data looks complete & I do not see any issues
# 3. Create a data dictionary for the dataset.
#The csv file lists the State, the rate of test participation, the verbal scores, and the math scores in that order and is sorted by the rate of student participation

# Step 2: Load the data.
import csv
import numpy as np
import seaborn as sb
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import plotly.plotly as py

# 4. Load the data into a list of lists
listFull = []
with open('sat_scores.csv', 'U') as f:
    reader = csv.reader(f)
    for row in reader:
        listFull.append(row)

# 5. Print the data
print listFull

# 6. Extract a list of the labels from the data, and remove them from the data.
listFull.pop(0)
print listFull

# 7. Create a list of State names extracted from the data. (Hint: use the list of labels to index on the State column)
listStates = []
for i in listFull:
    listStates.append(i[0])
print listStates

#8. Print the types of each column
states = [row[0] for row in listFull]
rates = [row[1] for row in listFull]
verbal = [row[2] for row in listFull]
math = [row[3] for row in listFull]

print type(states[0])
print type(rates[0])
print type(verbal[0])
print type(math[0])

# 9. Do any types need to be reassigned? If so, go ahead and do it.
#the rates & scores should be reassinged to integer values
rates = [int(rates[rates.index(i)]) for i in rates]
verbal = [int(verbal[verbal.index(i)]) for i in verbal]
math = [int(math[math.index(i)]) for i in math]

# 10. Create a dictionary for each column mapping the State to its respective value for that column.
statesRates = dict(zip(states, rates))
statesVerbal = dict(zip(states, verbal))
statesMath = dict(zip(states, math))

# Step 3: Describe the data
# 12. Print the min and max of each column
print "max value of rates: %d" %max(rates)
print "min value of rates: %d" %min(rates)

print "max value of Verbal Scores: %d" %max(verbal)
print "min value of Verbal Scores: %d" %min(verbal)

print "max value of Math Scores: %d" %max(math)
print "min value of Math Scores: %d" %min(math)

# 13. Write a function using only list comprehensions, no loops, to compute Standard Deviation. Print the Standard Deviation of each numeric column.

def listDeviations(testList):
    l = list(testList)
    listVar = [(i - np.mean(l))**2 for i in l]
    return np.sqrt(np.average(listVar))

print "standard deviation of rates: ",
print listDeviations(rates)

print "standard deviation of Verbal: ",
print listDeviations(verbal)

print "standard deviation of Math: ",
print listDeviations(math)


# Step 4: Visualize the data
# 14. Using MatPlotLib and PyPlot, plot the distribution of the Rate using histograms.

h = sorted(rates)
plt.hist(h, bins=10)
plt.title("Distribution of Rates")
plt.xlabel("% useage by students in States")
plt.ylabel("# of States")
plt.axis([0, 100, 0, 20])
plt.show()

# 15. Plot the Math distribution

g = sorted(math)
plt.hist(g, bins=10)
plt.title("Distribution of Math Scores")
plt.xlabel("Scores")
plt.ylabel("#")
plt.axis([400, 700, 0, 15])
plt.show()

# 16. Plot the Verbal distribution

i = sorted(verbal)
plt.hist(i, bins=10)
plt.title("Distribution of Verbal Scores")
plt.xlabel("Scores")
plt.ylabel("#")
plt.axis([450, 600, 0, 10])
plt.show()

# 17. What is the typical assumption for data distribution?

# 18. Does that distribution hold true for our data?

# 19. Plot some scatterplots. BONUS: Use a PyPlot figure to present multiple plots at once.

plt.figure()
plt.scatter(rates, math)
plt.title("Math Scores by Rate")

plt.scatter(rates, verbal)
plt.title("Verbal Scores by Rate")
plt.show()

plt.scatter(verbal, math)
plt.title("Verbal & Math Scores")
plt.show()

# 20. Are there any interesting relationships to note?

# 21. Create box plots for each variable.

plt.boxplot(rates)
plt.title("boxplot - rates")
plt.show()

plt.boxplot(math)
plt.title("boxplot - math")
plt.show()

plt.boxplot(verbal)
plt.title("boxplot - verbal")
plt.show()
