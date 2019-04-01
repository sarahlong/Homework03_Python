#create files across operating systems, module for reading CSVs
import os
import sys
import csv

# Store the file path associated with the file
csvpath = os.path.join('Resources/budget_data.csv')

# Define variables
months = 0
month_count = 0
total = 0
average_change = 0
change = 0

month_list = []
amount_list = []
amount1 = []
amount2 = []
change_list = []

# Read CSV using module
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #count total Months and sum total
        month_count += 1
        total += int(row[1])
        #add months and amounts to respective lists
        month_list.append(row[0])
        amount1.append(int(row[1]))
        amount2.append(int(row[1]))

    #edit the t0 and t1 lists to remove the first and last values
    del(amount2 [0])
    del(amount1 [(month_count)-1])

    #compute the changes between months and add to change list
    change_list = [x - y for x,y in zip(amount2,amount1)]


#compute final outputs
average_change = round(sum(change_list)/len(change_list),2)

max_increase = max(change_list)
max_decrease = min(change_list)

del(month_list [0])
matching_list = [(x,y) for x,y in zip(month_list, change_list)]

max_increase_month = [x for x,y in matching_list if y ==max_increase]
max_decrease_month = [x for x,y in matching_list if y ==max_decrease]


#print outputs in terminal
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {month_count}\n')
print(f"Total: ${total}")
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_increase_month} {max_increase}\n')
print(f'Greatest Decrease in Profits: {max_decrease_month} {max_decrease}\n')


#write results to text file
sys.stdout = open('pybank_outputs.txt', 'w+')
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {month_count}\n')
print(f"Total: ${total}")
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_increase_month} {max_increase}\n')
print(f'Greatest Decrease in Profits: {max_decrease_month} {max_decrease}\n')
sys.stdout.close()
sys.stdout=sys.__stdout__
#kernel needs to be restarted
