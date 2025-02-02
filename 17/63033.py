#63033 тип 17

a = [int(s) for s in open('63033.txt')]
a123 = max([x for x in a if x % 1000 == 123])


count = 0
s3 = []

for i in range (len(a)-2):
    if ((a[i]+a[i+1]+a[i+2])>a123):
        if ((a[i]%3==0) + (a[i+1]%3==0) + (a[i+2]%3==0)) == 1:
            if (((len(str(a[i]))==5)+(len(str(a[i+1]))==5)+(len(str(a[i+2]))==5))) > 1:
                 s3.append(a[i]+a[i+1]+a[i+2])

print(len(s3),max(s3))

