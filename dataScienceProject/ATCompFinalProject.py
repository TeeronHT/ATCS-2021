'''
AT Computer Science
Data Science Semester #1 Final Project

By Teeron Hajebi
Date: December 8th, 2021

Description: a simple collection of various data displays
including line graphs, pie charts, and scatter plots. Using data
compiled by TeeronHajebi (yours truly), hoping to minimize the use
of magic numbers. However, some were needed in instances where it
was difficult for me to code due to a lack of knowledge (I don't
know all that much).
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn

# read in main csv file
df = pd.read_csv("Data Science Final Project - Teeron Hajebi - Main Sheet.csv")

# a line plot displaying the minimum wage over the
# last 50 years
p1 = plt.figure(1)
seaborn.set_theme(style="ticks", palette="pastel")
seaborn.lineplot(x="Year", y="Federal Minimum Wage", data=df)
seaborn.despine()

# pie chart displaying the proportions of presidents responsible
# for increases in the federal minimum wage
p2 = plt.figure(2)
data = [5, 8]
labels = ['Democrat', 'Republican']
colors = seaborn.color_palette('pastel')[0:2]
plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')

# calculating correlation between minimum wage and percent of population
# in poverty and graphing least squares regression line
minimumWage = df["Federal Minimum Wage"]
percentOfPopInPoverty = df["Percentage of population in poverty"]
correlation1 = minimumWage.corr(percentOfPopInPoverty)
pd.set_option('display.max_columns', None)
print(df.corr())
print(correlation1)

p3 = plt.figure(3)
seaborn.regplot(x="Federal Minimum Wage", y="Percentage of population in poverty", data=df, x_jitter=0.5)
seaborn.despine()

# line graph showing the percentage of population in poverty over time
p4 = plt.figure(4)
seaborn.set_theme(style="ticks", palette="pastel")
seaborn.lineplot(x="Year", y="Percentage of population in poverty", data=df)
seaborn.despine()

# graphing the consumer price index
p5 = plt.figure(5)
seaborn.set_theme(style="ticks", palette="pastel")
seaborn.lineplot(x="Year", y="Consumer Price Index", data=df)
seaborn.despine()

plt.show()

