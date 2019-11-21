import csv

with open('budget_data.csv','r') as file:
    my_reader = csv.reader(file, delimiter= ',')
    data = list(my_reader)
    row_count = len(data)

    print(row_count)