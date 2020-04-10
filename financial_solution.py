import os
import csv
month_count = 0
total = 0
changelist = []
previous = 0
max_value = ["", 0]
min_value = ["", 999999]
# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
#The total number of months included in the dataset
    for e in csv_reader:
        month_count = month_count + 1


#The net total amount of "Profit/Losses" over the entire period
        total = total + int(e[1])
#The average of the changes in "Profit/Losses" over the entire period
        change = int(e[1]) - previous 
        previous = int(e[1]) #867884, 984655
        changelist.append(change)#[867884, 116771]
        length = len(changelist)-1
    
#The greatest increase in profits (date and amount) over the entire period 
        if change > max_value[1]:
            max_value[0] = e[0]
            max_value[1] = change
        if change < min_value[1]:
            min_value[0] = e[0]
            min_value[1] = change
    avg_change = sum(changelist[1:]) / length
#The greatest decrease in losses (date and amount) over the entire period
print("Financial Analysis")
print("******************") 
print("Total Months: " + str(month_count))
#print(month_count)
print("Total: " + str(total))
print("Average  Change: " + str(avg_change)) 
print("Greatest Increase in Profits: " + str(max_value)) 
print("Greatest Decrease in Profits: " + str(min_value))