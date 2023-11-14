#Import os
import os

#Import csv
import csv

csvpath = os.path.join('..', 'Pybank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"Csv Header:{csv_header}")
    
    for row in csvreader:
        print(row)

