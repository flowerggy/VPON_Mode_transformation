Rexceed=3700
i=0
for a in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]:
    i=i+1
    Rmatch = a * Rexceed
    x1=(0.4)* Rmatch
    x2=(0.6)* Rmatch

    y1=(0.1)* Rmatch
    y2=(0.2)* Rmatch
    y3=(0.3)* Rmatch
    y4=(0.4)* Rmatch

    z1=(0.06)* Rmatch
    z2=(0.1)* Rmatch
    z3=(0.14)* Rmatch
    z4=(0.18)* Rmatch
    z5=(0.22)* Rmatch
    z6=(0.3)* Rmatch

    print(i)
    print(Rmatch)
    print(x1,x2)
    print(y1,y2,y3,y4)
    print(z1,z2,z3,z4,z5,z6)