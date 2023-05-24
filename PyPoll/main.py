
#Import Modules
import os
import csv

#Define path to csv file
poll_data = os.path.join("..","Pypoll", "Resources", "election_data.csv")

#Open csv file
with open(poll_data) as poll_file:

#Set csv as dictionary ready to search by header
    csvreader = csv.DictReader(poll_file, delimiter= ',')

#Set Variables and Lists    
    rowcount = 0
    voteCount = [] 
    votes = []  

#Start loop to count total votes and add candidates to list   
    for row in csvreader:

        rowcount+= 1

        voteCount.append(row['Candidate'])

#Count how many votes per candidate from voteCount list
charles  = voteCount.count('Charles Casper Stockham')
diana = voteCount.count('Diana DeGette') 
raymon = voteCount.count('Raymon Anthony Doane')  

#Add number of votes per candidate to votes list
votes.append(charles)
votes.append(diana)
votes.append(raymon)

#Calculate Percentage of votes each candidate won
charlesPerc = (charles/rowcount) * 100
dianaPerc = (diana/rowcount) * 100
raymonPerc = (raymon/rowcount) * 100

#Determine max number of votes 
highVotes = max(votes)

#Run Conditional Statement to determine Winner
if highVotes == charles:
    winner = 'Charles Casper Stockham'

elif highVotes == diana:
    winner = 'Diana DeGette'

elif highVotes == raymon:
    winner = 'Raymon Anthony Doane'

#Print to terminal to double check work    
print('Election Results')
print('------------------------')
print(f'Total Votes: {rowcount}')  
print('------------------------')    
print(f'Charles Casper Stockham: {"%.3f" % charlesPerc}% ({charles})')
print(f'Diana DeGette: {"%.3f" % dianaPerc}% ({diana})')
print(f'Raymon Anthony Doane: {"%.3f" % raymonPerc}% ({raymon})')
print('------------------------')
print(f'Winner: {winner}')
print('------------------------')

#Export data to .txt file
analysis_data = os.path.join("..", "PyPoll", "Analysis", "analysis_data.txt")
with open(analysis_data, 'w') as analysis_out:
    analysis_out.write('Election Results\n')
    analysis_out.write('------------------------\n')
    analysis_out.write(f'Total Votes: {rowcount}\n')
    analysis_out.write('------------------------\n')
    analysis_out.write(f'Charles Casper Stockham: {"%.3f" % charlesPerc}% ({charles})\n')
    analysis_out.write(f'Diana DeGette: {"%.3f" % dianaPerc}% ({diana})\n')
    analysis_out.write(f'Raymon Anthony Doane: {"%.3f" % raymonPerc}% ({raymon})\n')
    analysis_out.write('------------------------\n')
    analysis_out.write(f'Winner: {winner}\n')
    analysis_out.write('------------------------')
