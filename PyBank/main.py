import csv
import pandas as pd
import numpy as np

data_file = "data/budget_data_1.csv"
df = pd.read_csv(data_file)
total_months = len(df)
total_revenue = 0
last_revenue = 0
revenue_change = []
greatest_increase = 0
greatest_decrease = 0
print()

for i in range(total_months):
	total_revenue = total_revenue + df.iloc[i, 1]
	curr_revenue_change = df.iloc[i, 1] - last_revenue
	last_revenue = df.iloc[i, 1]
	revenue_change.append(curr_revenue_change)

	if greatest_increase < curr_revenue_change:
		greatest_increase = curr_revenue_change

	if greatest_decrease > curr_revenue_change:
		greatest_decrease = curr_revenue_change

average_revenue_change = sum(revenue_change) / len(revenue_change)

print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + str('${:,.2f}'.format(total_revenue)))
print("Average Revenue Change: " + str('${:,.2f}'.format(average_revenue_change)))
print("Greatest Increase in Revenue: " + str('${:,.2f}'.format(greatest_increase)))
print("Greatest Decrease in Revenue: " + str('${:,.2f}'.format(greatest_decrease)))
print()