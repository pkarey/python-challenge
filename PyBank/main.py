#Import os
import os

#Import csv
import csv

#Define file path to locate csv
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
#Declare functions for formatting
def separator():
    print("--------------------------")
def spacer():
    print()
def separate_spacer():
    spacer()
    separator()
    spacer()

#Open csv and enable reader, store header row
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
#Store Profit/Loss values & Month values as separate lists
    rows = [[row[0], int(row[1])] for row in csvreader if row]
    months = [row[0] for row in rows]

#Edit month list to remove first value
    dict_month = months[1:]

#Establish variable for total months
    total_months = len(months)

#Create list for profit/loss as integers
    data = [int(row[1]) for row in rows]

#Calculate find differences between profit/loss values and find sum
    deltas = [x - data[i - 1] for i, x in enumerate(data)][1:]
    total = sum(data)

#Create min and max variables for profit/loss lists before zipping
    max_val = max(deltas)
    min_val = min(deltas)

#Zip edited month list and change profit/loss list
#Find months with greatest profit/loss
    delta_dict = dict(zip(dict_month, deltas))
    max = (max(delta_dict, key = delta_dict.get))
    min = (min(delta_dict, key = delta_dict.get))

#Establish variables to print data in string
    total_print = str(total)
    sum_deltas = sum(deltas)
    avg_deltas = round(sum_deltas / len(deltas),2)
    avg_deltas_print = str(avg_deltas)
    max_mo = str(max)
    min_mo = str(min)
    max_val_print = str(max_val)
    min_val_print = str(min_val)
    print_max = str('(' + max_val_print + ')')
    print_min = str('(' + min_val_print + ')')

#Define file path to locate and write in txt file 
    txtpath = os.path.join('PyBank', 'Analysis', 'analysis_profitloss')
    with open(txtpath, "w") as txtfile:

#Print analysis with to txtfile
        print("Financial Analysis", file = txtfile)
        print(f"Total Months: ", total_months, file = txtfile)
        print("Total: " + "$" + total_print, file = txtfile)
        print("Average Change: " + "$" + avg_deltas_print, file = txtfile)
        print("Greatest Increase in Profits: " + max_mo + " ($" + max_val_print + ")", file = txtfile)
        print("Greatest Decrease in Profits: " + min_mo + " ($" + min_val_print + ")", file = txtfile)

#Print analysis with formatting to terminal
    print("Financial Analysis")
    separate_spacer()
    print(f"Total Months: ", total_months)
    spacer()
    print("Total: " + "$" + total_print)
    spacer()
    print("Average Change: " + "$" + avg_deltas_print)
    spacer()
    print("Greatest Increase in Profits: " + max_mo + " ($" + max_val_print + ")")
    spacer()
    print("Greatest Decrease in Profits: " + min_mo + " ($" + min_val_print + ")")
    spacer()