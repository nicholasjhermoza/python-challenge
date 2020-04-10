import os
import csv
poll_csv = os.path.join("Resources", "election_data.csv")

#function
def result(data):

    #variables
    all_votes = 0
    votes = []
    candidatetally = []
    Candidates = []
    percent = []
    
    for r in data:

        # total number of votes cast
        all_votes = all_votes + 1

        # add name to list of candidates
        if r[2] not in Candidates:
            Candidates.append(r[2])

        # list votes to candidate
        votes.append(r[2])

    # populate the candidatetally with votes
    for e in Candidates:
        candidatetally.append(votes.count(e))
        percent.append(round(votes.count(e)/all_votes*100,3))

    # ID winner
    winner = Candidates[candidatetally.index(max(candidatetally))]
   
    #print(candidatetally)
    #print(Candidates)
    #print(percent)
    #print(winner)
    # display result
    print('Election Result')
    print('***************************')
    print('Total Votes')
    print(all_votes)
    print('***************************')
    print(Candidates)
    print('number of votes')
    print(candidatetally)
    print('percent of total votes')
    print(percent)
    print('***************************')
    print('Winner')
    print(winner)


# read in the CSV file
with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    # exc fx
    result(csvreader)