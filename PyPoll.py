import os
import csv


csvpath = os.path.join("..", "Resources", ["election_data.csv"])

with open(csvpath, "rw")as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    candidates = []
    num_votes = []
    percent_votes = []
    total_votes = 0
    
    
    
    for votes in num_votes:
        total_vote = sum("voter_id").value()
        print(total_vote)
    
    for row in candidates:
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append
        else:
            index = candidates.index(row[2])
            num_votes[index] +=1
    
    for votes in num_votes:
        percent_votes = (votes/total_votes) * 100
        percent_votes.append(votes)
        total_vote = (num_votes.[candidates].count)

    for winner in num_votes: 
        winner = max(num_votes)
        print(winner)



    



    
    


