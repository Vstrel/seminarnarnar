import numpy as np
def mnk(x, y):
    x = np.array(x)
    y = np.array(y)
    k = ((x*y).mean() - x.mean()*y.mean()) / ((x**2).mean() - (x.mean())**2)
    b = y.mean() - k * x.mean()
    print(k, b)


x = list(map(int, input().split()))
y = list(map(int, input().split()))
mnk(x, y)
