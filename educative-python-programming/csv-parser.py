import csv

file="/home/nagp/programming/projects/educative-python-programming/hw_200.csv"
with open(file, "r") as csv_file:
    csvReader = csv.reader(csv_file)
    headers = next(csvReader)
    print(headers)
    body = []
    for i in range(1, 10):
        body.append(next(csvReader))
    print(body)
