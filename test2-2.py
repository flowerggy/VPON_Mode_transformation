list1 = [410,400,380,360,310,300,280,250,240,200,160,140,120,80,50,20]
list2 = [90]

num = len(list1)
for x1 in range(0,num):
    temp1 = 1000 - list1[x1]
    print("temp1",temp1)
    for x2 in range(x1+1,num):
        temp2 = temp1 - list1[x2]
        print("temp2", temp2)
        for x3 in range(x2+1,num):
            if(temp2>list1[x3]):
                list2.append(temp2-list1[x3])
                break

list2.sort()
for x in range(len(list2)):
    if (x%8==0):
        print("")
    print(list2[x],end="\t")
