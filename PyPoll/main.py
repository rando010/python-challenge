import csv
with open('election_data.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    
    data = [l for l in csv_reader]
    number_of_votes_cast = len(data)
print("Election Results")
print("__________________")
print("Total Votes:" + str(number_of_votes_cast))
print("__________________")   
