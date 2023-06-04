import csv

# open the csv file and read it into a list of dictionaries
with open('timings2.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [dict(row) for row in reader]

# sort the list of dictionaries based on the 'input' column
data_sorted = sorted(data, key=lambda x: int(x['input']))

# write the sorted data back to a new csv file
with open('sortedTimings.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data_sorted[0].keys())
    writer.writeheader()
    writer.writerows(data_sorted)
