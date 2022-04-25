'''
子算法2 基于异步装载的最优MT-ONU组合
过载子系统X的MT-ONU存储在集合S中，轻载子系统Y1和Y2能提供匹配带宽的波长存储在集合Q中
仿真中有1个过载子系统，2个轻载子系统，每个子系统有16个ONU
'''
Ronu=[410,400,380,360,310,300,280,250,240,200,160,140,120,80,50,20]
a=min(Ronu)
#C=[700,1000]
#C=[200,350,500,650]
C=[100,170,240,310,380,500]
#C=[630,900]
#C=[180,315,450,585]
#C=[90,153,216,279,342,450]
K={}
m=len(C)
n=len(Ronu)
for j in range(0,m):
    print("j=,Ronu", j,Ronu)
    K[j] = 1
    for i in range(0,n):
        for d in range(i+1,n):
            if C[j] - Ronu[i] == 0:
                K[j] = 1
                C[j] = C[j] - Ronu[i]
                Ronu[i] = 0
                print("i的位置,k的次数,剩余的带宽数", i, K, C[j])
                break
            if C[j]-Ronu[i]>=Ronu[d] and C[j]>a:
                print("j的位置，i的位置,d的位置",j,i,d)
                print("k的次数,剩余的带宽数", K, C[j])
                C[j] = C[j]-Ronu[i]
                Ronu[i]=0
                K[j] = K[j]+1
                i = d
                C[j]=C[j]-Ronu[i]
                Ronu[i] = 0
                print("k的次数,剩余的带宽数",  K, C[j])
    Ronu = sorted(Ronu, reverse=True)
    print("修改后Ronu", Ronu)
    print("每个波长分配的最少装载数目", K)
    print("每个波长剩余的带宽数", C)


# C=[700,1000]
# for j in range(0,m):
#     for i in range(0,n):
#         if  K[j] >=1 and C[j]>=min(Ronu):
#             print("剩余的带宽数", C[j])
#             C[j] = C[j] - Ronu[i]
#             print("剩余的带宽数", C
#             continue[j])
# #         else:
#         break
# print("每个波长剩余的带宽数", C)






            









