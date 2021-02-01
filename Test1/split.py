import csv
import sys
import os
import random
import pandas as pd
from bf2 import MultiBF

# example usage: python split.py example.csv 200
# above command would split the `example.csv` into smaller CSV files of 200 rows each (with header included)
# if example.csv has 401 rows for instance, this creates 3 files in same directory:
#   - `example_1.csv` (row 1 - 200)
#   - `example_2.csv` (row 201 - 400)
#   - `example_3.csv` (row 401)

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
filename = sys.argv[1]

full_file_path = os.path.join(CURRENT_DIR, filename)
file_name = os.path.splitext(full_file_path)[0]

rows_per_csv = int(sys.argv[2]) if len(sys.argv) > 2 else 5000

with open(filename) as infile:
    reader = csv.DictReader(infile)
    header = reader.fieldnames
    rows = [row for row in reader]
    pages = []

    row_count = len(rows)
    start_index = 0
    # here, we slice the total rows into pages, each page having [row_per_csv] rows
    while start_index < row_count:
        pages.append(rows[start_index: start_index+rows_per_csv])
        start_index += rows_per_csv

    for i, page in enumerate(pages):
        with open('{}_{}.csv'.format(file_name, i+1), 'w+') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=header)
            writer.writeheader()
            for row in page:
                writer.writerow(row)

        print('DONE splitting {} into {} files'.format(filename, len(pages)))

os.system("shuf -n 800000 url.csv > test.csv") #to generate random permuations for Part C

'''
We need to test if C is present in A and B at the same time or not.
As all the values are unique. 
If it is present in both at the same time it is obviously a false positive!
'''
false_positive = 0

mlbf1 = MultiBF(2,800000)
print("number of layers",mlbf1.layers)
print("number of hash functions determined",mlbf1.hash_count)
with open('url_1.csv', encoding="utf-8") as csvfile1:
    reader = csv.reader(csvfile1)
    i=0
    for row in reader:
        query = row[1]
        mlbf1.add(query)

mlbf2 = MultiBF(2,800000)
print("number of layers",mlbf2.layers)
print("number of hash functions determined",mlbf2.hash_count)
with open('url_2.csv', encoding="utf-8") as csvfile1:
    reader = csv.reader(csvfile1)
    i=0
    for row in reader:
        query = row[1]
        mlbf2.add(query)

with open('test.csv', encoding="utf-8") as csvfile1:
    reader = csv.reader(csvfile1)
    i=0
    for row in reader:
        query = row[1]
        if mlbf1.check(query) and mlbf2.check(query) == True:
            false_positive += 1

print("The total number of false positives are : "+str(false_positive))






