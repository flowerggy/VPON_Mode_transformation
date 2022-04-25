'''
子算法1，去除无法被装载的ONU以及无法装载ONU的波长
过载子系统X的MT-ONU存储在集合S中，轻载子系统Y1和Y2能提供匹配带宽的波长存储在集合Q中
仿真中有1个过载子系统，2个轻载子系统，每个子系统有16个ONU
'''

#第一种情况，匹配带宽1700，只有两个波长，一个700，一个1000
Ronu=[1010,410,400,380,360,310,300,280,250,240,200,160,140,120,80,50,20]
C=[700,1000]
m=len(C)
n=len(Ronu)

print ("原始列表 : ", Ronu)
print("C最大值 : ", max(C))

for i in range(0,n):
    if Ronu[i]>max(C):
        Ronu[i]=0
print("删除后Ronu : ", Ronu)


for j in range(0,m):
    if min(Ronu)>C[j]:
        C[j]=0
print("删除后C : ", C)

