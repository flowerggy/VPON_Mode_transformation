#C=[700,1000]
C=[200,350,500,650]
#C=[100,170,240,310,380,500]
#匹配带宽为1530
#C=[630,900]
#C=[180,315,450,585]
#C=[90,153,216,279,342,450]
#匹配带宽为1360
#=[560,800]
#C=[160,280,400,520]
#C=[80,136,192,248,304,400]

Ronu=[410,400,380,360,310,300,280,250,240,200,160,140,120,80,50,20]
K={}
m=len(C)
n=len(Ronu)
list1=[]
list2=[]

#第一步我实现了每个波长的最少装载数目
C_remian1={}
minC_remain1={}

for j in range(0,m):
    K[j]=1
    C_remian1[j] = C[j]
    minC_remain1[j] = C[j]

    for i in range(0,n):

        if C_remian1[j]- Ronu[i] == 0:
            C_remian1[j] = C_remian1[j] - Ronu[i]
            minC_remain1[j]=0
            K[j] = 1
            break

        #这一步判断是否存在一个ONU，使得剩余带宽比最小值还小
        if C_remian1[j] - Ronu[i] > 0:
             if C_remian1[j]-Ronu[i] <= min(Ronu):
                 C_remian1[j]=C_remian1[j]-Ronu[i]
                 minC_remain1[j] = C_remian1[j]
                 break

    #第三种情况，此时装载个数一定大于2，那么就
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