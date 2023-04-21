import os
import csv

outfile = os.path.join("Resources", "election_analysis.txt")
csvpath = os.path.join("Resources", "election_data.csv")

# Total vote counter
total_votes = 0

# Candidate options and vote counts
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker
winner = ""
win_count = 0

with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     csv_header = next(csvreader)
     for row in csvreader:
          total_votes = total_votes + 1
          # Extract candidate_name
          name = row[2]

          if name not in candidate_options:
               candidate_options.append(name)
               candidate_votes[name] = 0

          candidate_votes[name] = candidate_votes[name] + 1
          
with open(outfile, "w") as txt_file:

    # Print final vote
    election_results = (
         f"\n\nElection Results\n"
         f"---------------------\n"
         f"Total Votes: {total_votes}\n"
         f"-------------------------\n"
    )
    print(election_results)

    # Save to txt file:
    txt_file.write(election_results)

    for candidate in candidate_votes:
        # Find the vote count and percentage
        votes = candidate_votes[candidate]
        percent = float(votes) / float(total_votes) * 100

        # Determine winnig candidate and vote count
        if (votes > win_count):
            win_count = votes
            winner = candidate

        # Print each candidates vote count and percentage
        output = f"{candidate}: {percent:.3f}% ({votes})\n"
        print(output)
    
        # Save each candidates data to txt file
        txt_file.write(output)

    # Print the winner
    winning_candidate = (
         f"-------------------\n"
         f"Winner: {winner}\n"
         f"-------------------------------"
    )
    print(winning_candidate)

    # Save winner to txt file
    txt_file.write(winning_candidate)

