import csv,time,os

storage1 = [0]*(10**8)

def find(storage1,query):
    flag = False
    ans = []
    count = 0
    val = hash(query)%(10**8)
    if storage1[val] == 1:
        flag = True
        count += 1
    return flag,ans,count

with open('url.csv', encoding="utf-8") as csvfile1:
    reader = csv.reader(csvfile1) 
    for row in reader:
        val = hash(row[2])%(10**8)
        storage1[val] = 1
    csvfile1.close()

os.system("shuf -n 800000 url.csv > test.csv")

#query = input()
start_time = time.time()
with open('test.csv', encoding="utf-8") as tester:
    reader = csv.reader(tester) 
    for row in reader:
    	query = row[2]
    	flag,ans,count = find(storage1,query)
print("The runtime of the program is : %s" %(time.time()-start_time))
        
