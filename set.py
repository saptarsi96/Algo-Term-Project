import csv,time

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

with open('Dataset/netflix_titles.csv', encoding="utf-8") as csvfile1:
    reader = csv.reader(csvfile1) 
    for row in reader:
        val = hash(row[2])%(10**8)
        storage1[val] = 1
    csvfile1.close()

with open('Dataset/tmdb_5000_movies.csv', encoding="utf-8") as csvfile2:
    reader2 = csv.reader(csvfile2)
    for row in reader2:
        val = hash(row[6])%(10**8)
        storage1[val] = 1
    csvfile2.close()

    print("Enter the name of the movie you want to search: ")
    query = input()
    start_time = time.time()
    flag,ans,count = find(storage1,query)
    if(flag):
        print("%s number of occurences found!" %count)
        for i in ans:
            print(i)
    if(not flag):
        print("No occurence found!")
    print("The runtime of the program is : %s" %(time.time()-start_time))
        