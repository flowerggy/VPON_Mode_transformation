#第三步，隐枚举法求最小值

Ronu=[380, 360, 300, 280, 240, 160, 140, 120, 50]
C=[0, 20, 10, 0]
m=len(C)
n=len(Ronu)

print ("原始列表 : ", Ronu)
print("C最大值 : ", max(C))

for i in range(0,n):
    if Ronu[i]>max(C):

        Ronu[i]=0
print("删除后Ronu : ", Ronu)

Ronu=[380, 360, 300, 280, 240, 160, 140, 120, 50]
C=[0, 20, 10, 0]

for j in range(0,m):
    print(min(Ronu))
    print(C[j])
    if min(Ronu)>C[j]:
        C[j] = 0
print("删除后C : ", C)

