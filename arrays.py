import csv,time

def find(storage,query):
    flag = False
    ans = []
    count = 0
    for i in storage:
        if query.lower() in i.lower():
            flag = True
            ans.append(i)
            count += 1
    return flag,ans,count

with open('Dataset/netflix_titles.csv', encoding="utf-8") as csvfile1:
    reader = csv.reader(csvfile1)
    storage1 = list()
    for row in reader:
        storage1.append(row[2])
    csvfile1.close()

with open('Dataset/tmdb_5000_movies.csv', encoding="utf-8") as csvfile2:
    reader2 = csv.reader(csvfile2)
    storage2 = list()
    for row in reader2:
        storage2.append(row[6])
    csvfile2.close()

    final_storage = storage1 + storage2

    print("Enter the name of the movie you want to search: ")
    query = input()
    start_time = time.time()
    flag,ans,count = find(final_storage,query)
    if(flag):
        print("%s number of occurences found!" %count)
        for i in ans:
            print(i)
    if(not flag):
        print("No occurence found!")
    print("The runtime of the program is : %s" %(time.time()-start_time))
        