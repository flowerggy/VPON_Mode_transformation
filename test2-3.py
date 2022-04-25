#没有实现装载的情况
#从一根波长开始分析起，假设现在只有一跟波长，带宽为700，申请的onu有16个，怎么组合是使得装载数量最少，剩余带宽最少的
import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('每个波长的最小装载ONU模型下的组合及其剩余带宽',cell_overwrite_ok=True )
header = ["第i的ONU","第d的ONU","RONU[i]","RONU[d]","剩余的带宽"]

for i in range(0, 5):
    worksheet.write(0, i, header[i])

Ronu=[410,400,380,360,310,300,280,250,240,200,160,140,120,80,50,20]
#匹配带宽为1700
#C=[700,1000]
C=[200,350,500,650]
#C=[100,170,240,310,380,500]
#匹配带宽为1530
#C=[630,900]
#C=[180,315,450,585]
#C=[90,153,216,279,342,450]
#匹配带宽为1360
#C=[560,800]
#C=[160,280,400,520]
#C=[80,136,192,248,304,400]


K={}
m=len(C)
n=len(Ronu)

#第一步我实现了每个波长的最少装载数目
for j in range(0,m):
    K[j]=1
    for i in range(0,n):
        for d in range(i+1,n):
            if C[j] - Ronu[i] == 0:
                C[j] = C[j] - Ronu[i]
                break
            if C[j]-Ronu[i]>=Ronu[d]:
                C[j] = C[j] - Ronu[i]
                K[j]=K[j]+1
                i = d
                C[j]=C[j] - Ronu[i]

#第二步，要实现K个组合的最后剩余带宽是最少的
#匹配带宽为1700
#C=[700,1000]
C=[200,350,500,650]
#C=[100,170,240,310,380,500]
#匹配带宽为1530
#C=[630,900]
#C=[180,315,450,585]
#C=[90,153,216,279,342,450]
#匹配带宽为1360
#C=[560,800]
#C=[160,280,400,520]
#C=[80,136,192,248,304,400]

minC_remain={}
print("波长为:",j,"最少装载ONU个数k:", K)
C_remain={}

for j in range(0,m):
    x = 1
    C_remain[j] = C[j]
    if K[j] == 1:
        for i in range(0,n):
            if C[j] - Ronu[i] == 0:
                C_remain[j] = C[j] - Ronu[i]
                del Ronu[i]
                print("j,i,x,最小剩余带宽", j, i, x, C_remain[j])
                break

    if K[j]>1:
        minC_remain[j]=C[j]
        for i in range(0,len(Ronu)):
            C_remain[j]=C[j]
            x = 1
            for d in range(i+1,len(Ronu)):
               if  C_remain[j]-Ronu[i]>=Ronu[d]:
                   x = x + 1
                   C_remain[j]=C_remain[j]-Ronu[i]
                   b=i+1
                   print("j,x,i,d,RONUi,RONUd,剩余带宽", j,x, i, d,Ronu[i],Ronu[d], C_remain[j]-Ronu[d])

                   if j==0:
                      worksheet.write(b, 0, i)
                      worksheet.write(b, 2, Ronu[i])
                      worksheet.write(b, 4, C_remain[j] - Ronu[d])

                   if j>0:
                       worksheet.write(b+16*j, 0, i)
                       # worksheet.write(b, 1, d)
                       worksheet.write(b+16*j, 2, Ronu[i])
                       # worksheet.write(b, 3, Ronu[d])
                       worksheet.write(b+16*j, 4, C_remain[j] - Ronu[d])

                   a=i
                   i = d
                   if x >= K[j]:
                      C_remain[j] = C_remain[j] - Ronu[i]
                      break

    #提取第J个波长里的剩余带宽，得出最小带宽




workbook.save('每个波长的最小装载ONU模型下的组合及其剩余带宽.xls')