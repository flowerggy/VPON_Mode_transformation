#最终完整版本
#还有两种情况要考虑，一个是没有满足的了。一个是不能满足两个的
#C=[700,1000]
#C=[200,350,500,650]
#C=[100,170,240,310,380,500]
#匹配带宽为1530
#C=[630,900]
#C=[180,315,450,585]
#C=[90,153,216,279,342,450]
#匹配带宽为1360
#C=[560,800]
#C=[160,280,400,520]
#C=[80,136,192,248,304,400]
#匹配带宽为1190
# C=[490,700]
#C=[140,245,350,455]
#C=[70,119,168,217,266,350]
#匹配带宽为1020
#C=[420,600]
#C=[120,210,300,390]
#C=[60,102,144,186,228,300]
#匹配贷带宽为850
#C=[350,500]
#=[100,175,250,325]
#C=[50,85,120,155,190,250]
#匹配带宽为680
#C=[280,400]
#C=[80,140,200,260]
#C=[40,68,96,124,152,200]
#匹配带宽为510
#C=[210,300]
#C=[60,105,150,195]
C=[30,51,72,93,114,150]
#匹配带宽为340
#C=[140,200]
#C=[40,70,100,130]
#C=[20,34,48,62,76,100]
#匹配带宽为170
#C=[70,100]
#C=[20,35,50,65]
#C=[10,17,24,31,38,50]



Ronu=[410,400,380,360,310,300,280,250,240,200,160,140,120,80,50,20]
K={}
m=len(C)
n=len(Ronu)


#第一步我实现了每个波长的最少装载数目
C_remian1={}
minC_remain1={}

for j in range(0,m):
    K[j]=1
    C_remian1[j] = C[j]
    minC_remain1[j] = C[j]

    for i in range(0,n):

        if C[j] - Ronu[i] == 0:
            C[j] = C[j] - Ronu[i]
            minC_remain1[j]=0
            K[j] = 1
            break

        if C[j] - Ronu[i] > 0:
             if C[j]-Ronu[i] < min(Ronu):
                 C_remian1[j]=C[j]-Ronu[i]
                 minC_remain1[j] = C_remian1[j]
                 break

        for d in range(i+1,n):
            if  C_remian1[j]-Ronu[i] >= Ronu[d]:
                 C_remian1[j]= C_remian1[j] - Ronu[i]
                 K[j]=K[j]+1
                 i = d
                 C_remian1[j]=C_remian1[j] - Ronu[i]
                 if C_remian1[j] <= min(Ronu):
                    minC_remain1[j] = C_remian1[j]
                 break

print("最少装载ONU个数k:",K)

#C=[700,1000]
#C=[200,350,500,650]
#C=[100,170,240,310,380,500]
#匹配带宽为1530
#C=[630,900]
#C=[180,315,450,585]
#C=[90,153,216,279,342,450]
#匹配带宽为1360
#C=[560,800]
#C=[160,280,400,520]
#C=[80,136,192,248,304,400]
#匹配带宽为1190
#C=[490,700]
#C=[140,245,350,455]
#C=[70,119,168,217,266,350]
#匹配带宽为1020
#C=[420,600]
#C=[120,210,300,390]
#C=[60,102,144,186,228,300]
#匹配贷带宽为850
#C=[350,500]
#C=[100,175,250,325]
#C=[50,85,120,155,190,250]
#匹配带宽为680
#C=[280,400]
#C=[80,140,200,260]
#C=[40,68,96,124,152,200]
#匹配带宽为510
#C=[210,300]
#C=[60,105,150,195]
C=[30,51,72,93,114,150]
#匹配带宽为340
#C=[140,200]
#C=[40,70,100,130]
#C=[20,34,48,62,76,100]
#匹配带宽为170
#C=[70,100]
#C=[20,35,50,65]
#C=[10,17,24,31,38,50]


C_remain = {}
minC_remain = {}

for j in range(0, m):

        print("j,", j, C[j])

        list1 = []
        list2 = []
        x = 1
        C_remain[j] = C[j]
        print("更新后的RONU", Ronu)

        if K[j] == 1:
            for i in range(0, len(Ronu)):

                if C_remain[j] -Ronu[i] == 0:
                    C_remain[j] = C_remain[j] - Ronu[i]
                    minC_remain[j]=C_remain[j]
                    del Ronu[i]
                    print("j,", j, minC_remain[j])
                    break

                if C[j] - Ronu[i] > 0:
                    if C[j] - Ronu[i] <= min(Ronu):
                        C_remain[j] = C[j] - Ronu[i]
                        minC_remain[j] = C_remain[j]
                        print("j", j, minC_remain[j])
                        del Ronu[i]
                        break


        elif K[j] > 1:
            minC_remain[j] = C[j]


            for i in range(0, len(Ronu)):
                 C_remain[j]=C[j]
                 x=1

                 if C_remain[j] - Ronu[i] > 0 and C_remain[j] - Ronu[i] < min(Ronu):
                    x1=len(Ronu)-1
                    print("更新后的ONU已经无法满足波长j最小装载数")
                    # print("C_remain[j],Ronu[i]",C_remain[j],Ronu[i])
                    C_remain[j] = C_remain[j] - Ronu[i]
                    print("i,C_remain[j],Ronu[i]", i,C_remain[j], Ronu[i])
                    minC_remain[j] = C_remain[j]
                    list1.append([i,x1, Ronu[i], Ronu[x1], C_remain[j]])
                    list2.append(C_remain[j])
                    K[j]=K[j]-1
                    break

                 if C_remain[j]<min(Ronu):
                     minC_remain[j] = C_remain[j]
                     K[j] = 0
                     list1.append([0, 0, 0, 0, minC_remain[j]])
                     list2.append(minC_remain[j])
                     break

                 for d in range(i + 1, len(Ronu)):
                     if C_remain[j] - Ronu[i] >= Ronu[d]:
                         x = x + 1
                         C_remain[j] = C_remain[j] - Ronu[i]
                         print("j,x,i,d,减前C_remain[j]，Ronu[i],Ronu[d],减后C_remain[j]", j, x,  i,d,C_remain[j],Ronu[i],Ronu[d],C_remain[j]-Ronu[d])
                         a = i
                         i = d
                         if x == K[j]:
                            C_remain[j] = C_remain[j] - Ronu[d]
                            list1.append([a,d,Ronu[a],Ronu[d],C_remain[j]])
                            list2.append(C_remain[j])
                            break

            flag1 = list2.index(min(list2))
            print(list2[flag1], "\t", list1[flag1])
            # print(list1[flag1][0], list1[flag1][1])
            # print("满足最小剩余带宽的i,d,Ronu[i],Ronu[d]=", list1[flag1][0], list1[flag1][1], list1[flag1][2],list1[flag1][3])
            if K[j] >=1:
               del Ronu[list1[flag1][0]]
            if K[j]>1:
               del Ronu[list1[flag1][1] - 1]
            list2.sort()
            print("j最小剩余带宽", j, list2[0])
            minC_remain[j] = list2[0]



print("最小剩余带宽", minC_remain)
print("更新后的RONU", Ronu)
