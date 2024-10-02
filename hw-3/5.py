
import numpy as np
def spiral(N, M):
    A = np.zeros((N, M))
    a = 1
    top = 0
    buttom = N - 1
    left = 0
    right = M - 1
    while top <= buttom and left <= right:
        for i in range(left, right + 1):
            A[top][i] = a
            a += 1
        top += 1
        for i in range(top, buttom + 1):
            A[i][right] = a
            a += 1
        right -= 1
        if top <= buttom:
            for i in range(right, left - 1, -1):
                A[buttom][i] = a
                a += 1
            buttom -= 1
        if left <= right:
            for i in range(buttom, top - 1, -1):
                A[i][left] = a
                a += 1
            left += 1
    for i in range(N):  
        for q in range(M):
            A[i][q] *= i
    print(A)