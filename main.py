k=0
for x in range(1000,10000):
    s=str(x)

    sp={s[0],s[1],s[2],s[3]}
    a1='13579'
    a0='02468'
    fl=True
    for x in range(3):
        if s[x] in a1 and s[x+1] in a1 or s[x] in a0 and s[x+1] in a0:
            fl=False
    if len(sp)==4 and fl==True: k+=1
print(k)