import csv
import sys

file_path = sys.argv[1]

for row in csv.DictReader(open(file_path)):
    row["Video ID"]
