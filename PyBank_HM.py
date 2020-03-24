import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath, "rw")as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    total_months = []
    total_profit = []
    monthly_profit_change = []
    average = 0
    
    for row in csvreader:
        totatl_months = sum("month").value()
        print(total_months)

    for row in csvreader:
        total_profit = sum(row[1]).count()
        print(total_profit)

    for row in csvreader:
        average_profit_change = sum(monthly_profit_change)/len(row[1])
        print("average", round(average , 2))

    for row in csvreader:
        monthly_profit_change.append(monthly_profit_change[row+1]-total_profit[row])
        print(max_increase_value = max(monthly_profit_change))
        print(max_decrease_value = min(monthly_profit_change))







