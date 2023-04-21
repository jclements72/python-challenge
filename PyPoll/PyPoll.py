import os
import csv


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
          
with open(outfile, "w") as file:
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percent = votes / total_votes * 100

    if (votes > win_count):
         win_count = votes
         winner = candidate

    # Print each candidates vote count and percentage
    output = f"{candidate}: {percent:.3f}% ({votes})\n"
    

  
# Print the Analysis
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(total_votes)) 
print("-------------------------")
for i in range(len(candidate_options)):
            print(candidate_options[i] + ": " + str(candidate_votes[name]) +"% (" + str(total_votes)+ ")")
print("-------------------------")
print("Winner: " + winner)


# Export Analysis to .txt file
with open('election_results.txt', 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("---------------------------------------\n")
    outfile.write("Total Vote: " + str(total_votes) + "\n")
    outfile.write("---------------------------------------\n")
    for i in range(len(set(candidate_options))):
        outfile.write(candidate_options[i] + ": " + str(candidate_votes[name]) +"% (" + str(total_votes) + ")\n")
    outfile.write("---------------------------------------\n")
    outfile.write("Winner: " + winner + "\n")