#create files across operating systems, module for reading CSVs
import os
import csv

# Store the file path associated with the file
csvpath = os.path.join('Resources/election_data.csv')

# Define variables
vote_count = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0


# Read CSV using module
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #count total votes and sum total
        vote_count += 1
        
        #add votes to respective candidate vote counters
        if row[2] == "Khan":
            Khan_votes = Khan_votes + 1
        elif row[2] =="Correy":
            Correy_votes = Correy_votes + 1    
        elif row[2] =="Li":
            Li_votes = Li_votes + 1
        else:
            OTooley_votes = OTooley_votes + 1

#compute percentages
Khan_percent = Khan_votes / vote_count
Correy_percent = Correy_votes / vote_count
Li_percent = Li_votes / vote_count
OTooley_percent = OTooley_votes / vote_count

#find winning candidate
candidate_list = ["Khan","Correy","Li","OTooley"]
vote_count_list =  [Khan_votes, Correy_votes, Li_votes, OTooley_votes]

max_votes = max(vote_count_list)
matching_list = [(x,y) for x,y in zip(candidate_list, vote_count_list)]
winner = [x for x,y in matching_list if y ==max_votes]

#print outputs
print("Election Results")
print("----------------------------")
print(f'Total Votes: {vote_count}')
print("----------------------------")
print(f'Khan Votes: {Khan_percent}, {Khan_votes}')
print(f'Correy Votes: {Correy_percent}, {Correy_votes}')
print(f'Li Votes: {Li_percent}, {Li_votes}')
print(f'OTooley Votes: {OTooley_percent}, {OTooley_votes}')
print("----------------------------")
print(f'Winner: {winner}')
print("----------------------------")

