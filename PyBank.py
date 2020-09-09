import os
import csv

csvpath = os.path.join(r"C:\Users\arkha\Desktop\bootcamp\nu-chi-data-pt-02-2020-u-c\Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv") 

with open(csvpath, "r")as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    firstrow = next(csvreader)
    total_months = 1
    total_profit = int(firstrow[1])
    monthly_profit_change = int(firstrow[1])
    average = 0
    month_of_change = []
    monthly_list = []
    prev_net = int(firstrow[1])
    net_change = 0

    net_change_list = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999]
    total_net = 0


 
    
    # for row in csvreader:
    #     totatl_months = sum(row[0]).count()
    #     print(total_months)

    for row in csvreader:
        total_profit += int(row[1])
        total_months += 1
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change


    average_profit_change = sum(net_change_list)/len(net_change_list)
    print("average", round(average , 2))

    

# Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average  Change: ${average_profit_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease}\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open("pybank.txt", "w") as txt_file:
    txt_file.write(output)





   

    

   
       


