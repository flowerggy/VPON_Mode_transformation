#h这是第二版算法，没有实现最小装载

Ronu=[410,400,380,360,310,300,280,250,240,200,160,140,120,80,50,20]
#匹配带宽为1700
#C=[700,1000]
#C=[200,350,500,650]
#C=[100,170,240,310,380,500]
#匹配带宽为1530
#C=[630,900]
#C=[180,315,450,585]
C=[90,153,216,279,342,450]
#匹配带宽为1360
#=[560,800]
#C=[160,280,400,520]
#C=[80,136,192,248,304,400]


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
        for d in range(i+1,n):

            if C[j] - Ronu[i] == 0  :
                C[j] = C[j] - Ronu[i]
                break

            if C_remian1[j]-Ronu[i]>=Ronu[d] :
                C_remian1[j]= C_remian1[j] - Ronu[i]
                K[j]=K[j]+1
                i = d
                C_remian1[j]=C_remian1[j] - Ronu[i]


#在已知装载的情况下，寻求异步的，最小剩余带宽的组合
print("波长为:",j,"最少装载ONU个数k:", K)
C_remain={}
minC_remain={}

for j in range(0,m):
    x = 1
    C_remain[j] = C[j]

    if K[j] == 1:
        for i in range(0,n):
            if C[j] - Ronu[i] == 0:
                C_remain[j] = C[j] - Ronu[i]
                del Ronu[i]
                # print("j,i,x,最小剩余带宽", j, i, x, C_remain[j])
                break

    if K[j]>1:
        minC_remain[j]=C[j]
        for i in range(0,len(Ronu)):
            C_remain[j]=C[j]
            for d in range(i+1,len(Ronu)):

               # print("j,x,i,d,剩余带宽,Ronu[i],Ronu[d]", j,x,i,d,C_remain[j],Ronu[i],Ronu[d])

               if  C_remain[j]-Ronu[i]>=Ronu[d]:
                   x = x + 1
                   C_remain[j]=C_remain[j]-Ronu[i]
                   # print("j,i,x,d,剩余带宽", j, i, x, d, C_remain[j])
                   a=i
                   # del Ronu[i]
                   i = d
                   if x >=K[j]:
                      C_remain[j] = C_remain[j] - Ronu[d]
                      # del Ronu[d-1]
                      print("j,i,x,d,剩余带宽", j, i, x, d, C_remain[j])
                      if C_remain[j]<minC_remain[j]:
                            minC_remain[j]=C_remain[j]
                            # print("j,i,x,d,最小剩余带宽", j, i, x, d, minC_remain[j])


        # print("波长为j,最小剩余带宽:",j,minC_remain)




