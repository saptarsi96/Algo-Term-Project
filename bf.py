from bloomfilter import BloomFilter
from random import shuffle
import csv, time
n = 7000 #no of items to add
p = 0.05 #false positive probability

bloomf = BloomFilter(n,p)
print("Size of bit array:{}".format(bloomf.size))
print("False positive Probability:{}".format(bloomf.fp_prob))
print("Number of hash functions:{}".format(bloomf.hash_count))


with open('Dataset/netflix_titles.csv', encoding="utf-8") as csvfile1:
	reader = csv.reader(csvfile1) 
	for row in reader:
		bloomf.add(row[2])
		
print("Enter the name of the movie you want to search: ")
query = input()
start_time = time.time()
if bloomf.check(query):
	print("'{}' is probably present".format(query))
else:
	print("'{}' is definitely not present".format(query))
print("The runtime of the program is : %s" %(time.time()-start_time))

