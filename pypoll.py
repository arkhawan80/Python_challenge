import os
import csv
from collections import Counter

csvpath = os.path.join(r"C:\Users\arkha\Desktop\bootcamp\nu-chi-data-pt-02-2020-u-c\Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv")

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    candidates = []
    num_votes = []
    percent_votes = []
    total_votes = 0
    
    for row in csvreader:
        total_votes += 1
        candidates.append(row[2])

    print (Counter(candidates).keys())
    print (Counter(candidates).values())

    for key,value in Counter(candidates).items():
        print(f"{key} {value} {value/total_votes*100:.2f}")

print(f"total_votes={total_votes}")

    



    
    


