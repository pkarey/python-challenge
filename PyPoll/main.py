#Import os
import os

#Import csv
import csv

#Define file paths
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
txtpath = os.path.join('..','PyPoll','Analysis','poll_analysis.txt')

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
with open(csvpath) as csv_poll:

    csvreader = csv.reader(csv_poll, delimiter=',')
    csv_header = next(csvreader)

#Establish variables and placeholders before looping
    stockham = 'Charles Casper Stockham'
    stockham_votes = 0
    degette = 'Diana DeGette'
    degette_votes = 0
    doane = 'Raymon Anthony Doane'
    doane_votes = 0
    total_votes = 0

#Loop through CSV
    for row in csvreader:
        if row[2] == stockham:
            stockham_votes+= 1
        elif row[2] == degette:
            degette_votes+= 1
        else:
            doane_votes+= 1
#Find total number votes
    total_votes = stockham_votes + degette_votes + doane_votes

#Stockham results
    stockham_percentage = str(round(stockham_votes/total_votes,5)*100)
    stockham_doane = (round(stockham_votes/total_votes,5)*100)
    stockham_percentage_entry = str(stockham_percentage + "%")
    stockham_vote_total = str(stockham_votes)
    stockham_print_votes = str("(" + stockham_vote_total + ")")
    stockham_entry = str(stockham + ":")
    
#Degette results
    degette_percentage = str(round(degette_votes/total_votes,5)*100)
    degette_doane = (round(degette_votes/total_votes,5)*100)
    degette_percentage_entry = str(degette_percentage + "%")
    degette_vote_total = str(degette_votes)
    degette_print_votes = str("(" + degette_vote_total + ")")
    degette_entry = str(degette + ":")

#Doane results
    doane_percentage = str(round(100 - (degette_doane + stockham_doane), 5))
    doane_percentage_entry = str(doane_percentage + "%")
    doane_vote_total = str(doane_votes)
    doane_print_votes = str("(" + doane_vote_total + ")")
    doane_entry = str(doane + ":")

#Create dictionary for candidate vote counts
    vote_count_dict = {stockham: stockham_votes, degette : degette_votes, doane : doane_votes}

#Print Text Header
    print("Election Results")

#Insert formatting
    separate_spacer()

#Print total votes
    print(f"Total Votes: ", total_votes)

#Insert formatting
    separate_spacer()

#Print candidate results with formatting
    print(stockham_entry, stockham_percentage_entry, stockham_print_votes)
    spacer()
    print(degette_entry, degette_percentage_entry, degette_print_votes)
    spacer()
    print(doane_entry, doane_percentage_entry, doane_print_votes)
    separate_spacer()

#Print winning candidate
    max = max(vote_count_dict, key = vote_count_dict.get)
    print(f"Winner: ", max)
    separate_spacer()