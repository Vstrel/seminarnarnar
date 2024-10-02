N = int(input())

def simple(n):
    fl = 1
    if n == 1 or n == 2:
        fl = 1
    else:
        for l in range(2, n // 2 + 1):
            if n % l == 0:
                fl += 1
    return fl


for i in range(2, N + 1):
    if simple(i) == 1 and N % i == 0:
        a = N
        while a % i == 0:
            print(i, end=" ")
            a = a // i