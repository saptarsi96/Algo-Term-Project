import csv,time,os,math

#storage1 = [0]*(10**8)

def get_size(n, p):
    m = -(n * math.log(p))/(math.log(2)**2)
    return int(m)

total_length = len(open("url.csv",'r').readlines())

size = get_size(total_length,0.05)
print(size)
storage1 = [0]*(size)
def find(storage1,query):
    flag = False
    ans = []
    count = 0
    val = hash(query)%(size)
    if storage1[val] == 1:
        flag = True
        count += 1
    return flag,ans,count
start_time_insert = time.time()
with open('url.csv', encoding="utf-8") as csvfile1:
    reader = csv.reader(csvfile1) 
    for row in reader:
        val = hash(row[1])%(size)
        storage1[val] = 1
    csvfile1.close()
print("The insertion time of the hash is : %s" %(time.time()-start_time_insert))

os.system("shuf -n 800000 url.csv > test.csv")

#query = input()
start_time = time.time()
with open('test.csv', encoding="utf-8") as tester:
    reader = csv.reader(tester) 
    for row in reader:
    	query = row[1]
    	flag,ans,count = find(storage1,query)
print("The query time of the hash is : %s" %(time.time()-start_time))
        
