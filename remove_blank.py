import csv

input = open('input.csv', 'rb')
output = open('output.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if any(row):
	writer.writerow(row)
input.close()
output.close()
