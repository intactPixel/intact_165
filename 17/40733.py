f = open('40733.txt')
a = [int(i) for i in f]
count = 0
mx = 0
s = 0
n = 0
for i in range(len(a)):
    if (a[i] % 2 == 0):
        s += a[i]
        n += 1
x = s / n
for i in range(len(a) - 1):
    if ((a[i] % 3 == 0) or (a[i + 1] % 3 == 0)) and ((a[i] < x) or (a[i + 1] < x)):
        count += 1
        mx = max(mx, a[i] + a[i + 1])
print(count, mx)