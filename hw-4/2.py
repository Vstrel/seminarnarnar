n, l = map(str, input().split())
a = int(n)
q = ""
for i in range(0, len(l), a):
    k = l[i:i+a]
    q += k[::-1]
print(q)