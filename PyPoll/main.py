
import csv
import os

filepath = os.path.join("PyPoll", "Resources","election_data.csv")
print (filepath)

def get_results(myList):
    # Define variables
    total_voters = 0
    voter_ID = []
    candidate_count = []
    specific_candidate = []
    percent = []

    #Number of total votes
    for row in myList:
        total_voters = total_voters + 1

        #Find the candidates who received votes
        if row[2] not in specific_candidate:
            specific_candidate.append(row[2])
    
        voter_ID.append(row[2])

    #Calculate the percentage
    for candidate in specific_candidate:
        candidate_count.append(voter_ID.count(candidate))
        percent.append(round((voter_ID.count(candidate)/total_voters)*100,3))

    #Find the winner
    winner=specific_candidate[candidate_count.index(max(candidate_count))]

    #Print the results
    print("Election Results")
    print("----------------------------")
    print("Total Number of Votes Cast: " + str(total_voters))
    print("----------------------------")
    for A in range(len(specific_candidate)):
        print(f'{specific_candidate[A]}: {percent[A]}% {candidate_count[A]}')
    print("----------------------------")
    print("Winner:" + str(winner))

    #Exit path
    PyPoll_output=os.path.join("PyPoll Result.txt")

    #Write out results to a text file
    with open(PyPoll_output,"w") as txtfile:
        txtfile.write("Election Results" + "\n")
        txtfile.write("----------------------------" + "\n")
        txtfile.write("Total Number of Votes Cast: " + str(total_voters) + "\n")
        txtfile.write("----------------------------" + "\n")
        for A in range(len(specific_candidate)):
            txtfile.write (f'{specific_candidate[A]}: {percent[A]}% ({candidate_count[A]}) \n')
        txtfile.write("----------------------------" + "\n")
        txtfile.write("Winner:" + str(winner))


with open(filepath, newline='') as file:
    csvreader = csv.reader(file, delimiter=',')

    # adjust for header
    csv_header = next(csvreader)
    
    # use function
    get_results(csvreader)

