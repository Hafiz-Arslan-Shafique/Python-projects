## find Unique number of a list and there count
name =["bcdef", "abcdefg", "bcde", "bcdef"]
newlist=[]

for i in range(0, len(name)):
    if name[i] not in newlist: 
        newlist.append(name[i])
print(len(newlist))

for j in newlist:
        print (name.count(j))