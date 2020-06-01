import gmpy2
import pyecm
from random import randint
from math import pi


N = 10 ** 50
M = 1000
S = 0

def Func_isSquareFree(n):
    multipliers_list = list(pyecm.factors(n, False, True, 8, 1))
    for i in range(len(multipliers_list) - 1):
        if multipliers_list[i] == multipliers_list[i + 1]:
            return False
    return True



for i in range(M):
    a = randint(1, N)
    print(a)
    if Func_isSquareFree(a):
        S += 1
    else:
        S += 0

print()
print("Answer: " + str(S / M))
print("Teorethical:  " + str(6 / pi ** 2))
