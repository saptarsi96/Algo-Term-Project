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
        