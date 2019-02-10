import os
import csv

#create the path
csvpath = os.path.join("..","Resources","election_data.csv")

# open and read
with open(csvpath,newline="", encoding="utf-8)") as election_data:
    csvreader = csv.reader(election_data,delimiter=",")

# read the header
    csvheader = next(csvreader)

#set variable
    candidate = []

    for row in csvreader:
        candidate.append(row[2])

    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]
    
    votes = []
    name = []
    
    #iterate 
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])
    # adding the information to the candidate
    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

#set winner variable
    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       
            
total_votes = len(candidate)

correy_total = candidate.count('Correy')
correy_percent = int(correy_total) / int(total_votes)

o_tooley_total = candidate.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

li_total = candidate.count('Li')
li_percent = li_total / total_votes

khan_total = candidate.count('Khan')
khan_percent = khan_total / total_votes

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')

