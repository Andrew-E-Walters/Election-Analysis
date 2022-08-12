import csv 
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

   # Write three counties to the file.
         # Write three counties to the file.
     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Find total votes
total_votes = 0 
candidate_options =[]
candidate_votes = {}



# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here. 
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
 # Print the header row.
    headers = next(file_reader)
    print(headers)

        # Print each row in the CSV file.
    for row in file_reader:
       # print(row)
        # 2. Add to the total vote count
        total_votes += 1 
# Print the candidate name from each row
        candidate_name = row[2]
               # If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options: 
     # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

        # 2. Begin tracking that candidate's vote count.
        candidate_votes[candidate_name] = += 1



# Print the candidate list.
print(candidate_votes)
# 3. Print the total votes. 

#The Data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of canidates who recieved votes
# 3. The percentage of votes each candidatewon
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
