# Import module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('PyPoll','Resources', 'election_data.csv')

#Initialize Variables
total_votes=0
candidate_list=[]
candidate_votes={}
winning_count=0
winners=[]

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # Count total votes
        total_votes += 1
        #Add candidates to dictionary and count individual votes
        candidate_name=row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name]=0
        
        candidate_votes[candidate_name]=candidate_votes[candidate_name]+1

# Export to text file
output_path = os.path.join("PyPoll", "analysis", "election_analysis.txt")

# Ensure the directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write to text file
with open(output_path, "w") as txt_file:
        election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")

        print(election_results)
        txt_file.write(election_results)

        for name in candidate_votes:
            votes=candidate_votes.get(name)
            percent_votes=votes/total_votes*100

            if votes > winning_count:
                winning_count=votes
                winners=[name]
            elif votes == winning_count:
                winners.append(name)

            voter_results = (
                f"{name}: {percent_votes:.2f}% ({votes})\n"
            )

            print(voter_results)
            txt_file.write(voter_results)

        winner_string = ", ".join(winners)
        
        winner_results = (
            f"-------------------------\n"
            f"Winner: {winner_string}\n"
            f"-------------------------\n")

        print(winner_results)
        txt_file.write(winner_results)