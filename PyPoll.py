import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data )
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]
    
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # 4. Print the candidate name and percentage of votes.
            print(f"{candidate_name}: received {vote_percentage}% of the vote.")

            # Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
# Print the candidate list.
print(winning_candidate)

# Close the file.
election_data.close()



