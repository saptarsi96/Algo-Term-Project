#!/usr/bin/python
# -*- coding: utf-8 -*-
from bloomfilter import BloomFilter
from random import shuffle
from bf2 import MultiBF
import csv
import time

mlbf = MultiBF(2,12000)
#print("number of layers",mlbf.layers)
#print("number of hash functions determined",mlbf.hash_count)
with open('Dataset/updated_urls3.csv', encoding="utf-8") as csvfile1:
    reader = csv.reader(csvfile1)
    i=0
    for row in reader:
        query = row[7]
        mlbf.add(query)

#print("Enter the name of the movie you want to search: ")
query = input()
start_time = time.time()
if mlbf.check(query):
	print("'{}' is probably present".format(query))
else:
	print("'{}' is definitely not present".format(query))
print("The runtime of the program is : %s" %(time.time()-start_time))
