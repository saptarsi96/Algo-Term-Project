import csv,time,os

def find(storage,query):
    flag = False
    ans = []
    count = 0
    for i in storage:
        if query.lower() == i.lower():
            flag = True
            ans.append(i)
            count += 1
    return flag,ans,count

with open('url.csv', encoding="utf-8") as csvfile1:
    reader = csv.reader(csvfile1)
    storage1 = list()
    for row in reader:
        storage1.append(row[2])
    csvfile1.close()


os.system("shuf -n 100 url.csv > test.csv")

start_time = time.time()
with open('test.csv', encoding="utf-8") as tester:
    reader = csv.reader(tester) 
    for row in reader:
    	query = row[2]
    	flag,ans,count = find(storage1,query)
print("The runtime of the program is : %s" %(time.time()-start_time))
        
